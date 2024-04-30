from Kathara.model.Lab import Lab
from Kathara.manager.Kathara import Kathara
import bgp_ls_vis.proto as proto
import bgp_ls_vis.graphing as graphing
import networkx as nx
from fs import open_fs
from fs.copy import copy_fs

# Create lab
lab = Lab("18_nodes_twin")

# To load a BGP-LS table from file instead of a gRPC connection, `connect` param is set false
rpc = proto.GoBGPQueryWrapper(connect=False)

# Calling get_lsdb with param `filename` set will trigger loading from file instead of RPC
first_example_dir = r"C:/Users/lolli/Desktop/kathara_digital_twin/dumps"
lsdb = rpc.get_lsdb(filename=fr"{first_example_dir}/18-node-isis-w-bcast-segment.yaml")

# Create a graph from the lsdb
graph = graphing.build_nx_from_lsdb(lsdb).to_undirected()

# All routers of the lab, the dict is defined like: {"name_of_the_machine": [machine, number_of_the_next_port_to_use]}
routers = {}

for node in graph.nodes(data=True):
    if node[1]["lsa"]!=None:
        # Creating new machine for each node and add adding it to the dict "routers"
        routers.update({f"{node[0]}" : [lab.new_machine(f"{node[0].lower()}", **{"image": "kathara/frr"}) , 0]})
        
ch = "I"

for edge in graph.edges(data=True):
    if edge[2]["lsa"]["linkDescriptor"]:
        
        # Starting the process to connect the two routers of the edge to the same collision domain
        r1=routers[f"{edge[1]}"]
        r1_ip = edge[2]["lsa"]["linkDescriptor"]["interfaceAddrIpv4"]
        r2=routers[f"{edge[0]}"]
        r2_ip = edge[2]["lsa"]["linkDescriptor"]["neighborAddrIpv4"]
        
        # Connecting first router
        lab.connect_machine_to_link(r1[0].name, ch)
        
        # Updating (or creating if it doesn't exist) the startup file for the first router
        lab.update_file_from_string(content=f"/sbin/ifconfig eth{r1[1]} {r1_ip} up\n", dst_path=f"{r1[0].name}.startup")
        r1[1] += 1 # Update the next free interface
        
        # Connecting second router 
        lab.connect_machine_to_link(r2[0].name, ch)
        
        # Updating (or creating if it doesn't exist) the startup file for the second router
        lab.update_file_from_string(content=f"/sbin/ifconfig eth{r2[1]} {r2_ip} up\n", dst_path=f"{r2[0].name}.startup")
        r2[1] += 1 # Update the next free interface
        
        ch += "I" # Update the name for the next domain
        
        #print(f"{edge[:2]}", edge[2]["lsa"]["linkDescriptor"]) 
  
for edge in graph.edges(data=True):
    if not edge[2]["lsa"]["linkDescriptor"]:
        # Adding machines to collision domain with more than two routers connected
        r = routers[f"{edge[1]}"]
        r_ip = edge[2]["lsa"]["lsattribute"]["node"]["localRouterId"]
        lab.connect_machine_to_link(r[0].name, ch)
        lab.update_file_from_string(content=f"/sbin/ifconfig eth{r[1]} {r_ip}/24 up\n", dst_path=f"{r[0].name}.startup")
        r[1] += 1

ch += "I"

for r in routers:
    # Creating new machine for each node and add adding it to the dict "routers"
    lab.update_file_from_string(content="/etc/init.d/frr start\n", dst_path=f"{routers[r][0].name}.startup")
    
           
fs = open_fs(fr"osfs://C:\Users\lolli\Desktop\kathara_digital_twin\lab")
copy_fs(lab.fs, fs)

# Deploy lab
Kathara.get_instance().deploy_lab(lab=lab)

# Connecting to the machine P8 wich is connected to the collision domain 'I'
Kathara.get_instance().connect_tty("p18", lab_name=lab.name)

# Undeploy lab
Kathara.get_instance().undeploy_lab(lab=lab)