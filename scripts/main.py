from Kathara.model.Lab import Lab
from Kathara.manager.Kathara import Kathara
import bgp_ls_vis.proto as proto
import bgp_ls_vis.graphing as graphing
import networkx as nx
import os
from fs import open_fs
from fs.copy import copy_fs
import functions
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="the absolute path of the file .yaml to load")
parser.add_argument("-d", "--directory", help="the directory where you want to save the fs of the lab")
args = parser.parse_args()

# Create lab
lab = Lab("digital_twin")

# To load a BGP-LS table from file instead of a gRPC connection, `connect` param is set false
rpc = proto.GoBGPQueryWrapper(connect=False)

# Calling get_lsdb with param `filename` set will trigger loading from file instead of RPC
if args.file:
    lsdb = rpc.get_lsdb(filename=fr"{args.file}")
else:
    # correct way but now does't work
    lsdb = rpc.get_lsdb(os.path.join(os.getcwd(),"dumps","18-node-isis-w-bcast-segment.yaml"))
    # lsdb = rpc.get_lsdb(r"C:\Users\lolli\Desktop\kathara_digital_twin\dumps\18-node-isis-w-bcast-segment.yaml")

# Create a graph from the lsdb
graph = graphing.build_nx_from_lsdb(lsdb).to_undirected()

# All routers of the lab, the dict is defined like: {"name_of_the_machine": kathara_machine}
routers = {}

for node in graph.nodes(data=True):
    if node[1]["lsa"]!=None:
        # Creating new machine for each node and add adding it to the dict "routers"
        try:
            routers.update({f"{node[0]}" : lab.new_machine(f"{node[0].lower()}", **{"image": "kathara/frr"})})
        except Exception as e:
            # Changing the name of the machine to an accepted one 
            routers.update({f"{node[0]}" : lab.new_machine(f"{functions.invalid_to_valid_name(node[0].lower())}", **{"image": "kathara/frr"})})
        
collision_domain = 0

for edge in graph.edges(data=True):
    if edge[2]["lsa"]["linkDescriptor"]:
        
        # Starting the process to connect the two routers of the edge to the same collision domain
        r1=routers[f"{edge[1]}"]
        r1_ip = edge[2]["lsa"]["linkDescriptor"]["interfaceAddrIpv4"]
        r2=routers[f"{edge[0]}"]
        r2_ip = edge[2]["lsa"]["linkDescriptor"]["neighborAddrIpv4"]
        
        # Connecting first router
        lab.connect_machine_to_link(r1.name, functions.numbers_to_words(collision_domain))
        
        # Updating (or creating if it doesn't exist) the startup file for the first router
        lab.update_file_from_string(content=f"/sbin/ifconfig eth{r1.interfaces.__len__()-1} {r1_ip}/30 up\n", dst_path=f"{r1.name}.startup")
        
        # Connecting second router 
        lab.connect_machine_to_link(r2.name, functions.numbers_to_words(collision_domain))
        
        # Updating (or creating if it doesn't exist) the startup file for the second router
        lab.update_file_from_string(content=f"/sbin/ifconfig eth{r2.interfaces.__len__()-1} {r2_ip}/30 up\n", dst_path=f"{r2.name}.startup")
        
        collision_domain += 1 # Update the name for the next domain
  
for edge in graph.edges(data=True):
    if not edge[2]["lsa"]["linkDescriptor"]:
        # Adding machines to collision domain with more than two routers connected
        r = routers[f"{edge[1]}"]
        r_ip = edge[2]["lsa"]["lsattribute"]["node"]["localRouterId"]
        lab.connect_machine_to_link(r.name, functions.numbers_to_words(collision_domain))
        lab.update_file_from_string(content=f"/sbin/ifconfig eth{r.interfaces.__len__()-1} {r_ip}/30 up\n", dst_path=f"{r.name}.startup")

collision_domain += 1

for r in routers:
    # Creating new machine for each node and add adding it to the dict "routers"
    lab.update_file_from_string(content="/etc/init.d/frr start\n", dst_path=f"{routers[r].name}.startup")

    # Configuring the daemons
    routers[r].create_file_from_list(
        lines=[
        "zebra=yes",
        "isisd=yes"
        ],
        dst_path= "/etc/frr/daemons"
    )
    
    # Starting configuration of zebra
    routers[r].create_file_from_list(
        lines=[
        "hostname frr",
        "password frr",
        "enable password frr" 
        ],
        dst_path= "/etc/frr/zebra.conf"
    )
    # Looking for the ip addresses of the interfaces in the startup files of the fs
    with lab.fs.open(f"{routers[r].name}.startup") as file:
        for line in file:
            words_of_the_line = line.strip().split()
            # Update the zebra.conf file with the ip addresses
            functions.configure_zebra(routers[r], words_of_the_line)
    
    
if args.directory:
    # Copy the fs of the lab in the folder specified in command line (absolute path)           
    fs = open_fs(fr"osfs://{args.directory}")   
    copy_fs(lab.fs, fs)

# Deploy lab
#Kathara.get_instance().deploy_lab(lab=lab)

# Connecting to the machine P8 wich is connected to the collision domain 'I'
#Kathara.get_instance().connect_tty("p8", lab_name=lab.name)

# Undeploy lab
#Kathara.get_instance().undeploy_lab(lab=lab)

#print(routers["P7"])