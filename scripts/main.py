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
    # Creating new machine for each node and add adding it to the dict "routers"
    try:
        routers.update({f"{node[0]}" : lab.new_machine(f"{node[0].lower()}", **{"image": "kathara/frr"})})
    except Exception as e:
        # Changing the name of the machine to an accepted one 
        routers.update({f"{node[0]}" : lab.new_machine(f"{functions.invalid_to_valid_name(node[0].lower())}", **{"image": "kathara/frr"})})   

collision_domain = 0

for edge in graph.edges(data=True):
    if edge[2]["pseudonode"]:
        # Adding machines to collision domain with more than two routers connected
        try:
            edge[2]["lsa"]["localNode"]["pseudonode"]
            
            r1 = routers[f"{edge[0]}"]
            r1_ip = edge[2]["lsa"]["lsattribute"]["node"]["localRouterId"]
            lab.connect_machine_to_link(r1.name, functions.numbers_to_words(collision_domain))
            lab.update_file_from_string(content=f"/sbin/ifconfig eth{r1.interfaces.__len__()-1} {r1_ip}/30 up\n", dst_path=f"{r1.name}.startup")

            r2 = routers[f"{edge[1]}"]
            lab.connect_machine_to_link(r2.name, functions.numbers_to_words(collision_domain))

        except:
            try:
                r1 = routers[f"{edge[1]}"]
                r1_ip = edge[2]["lsa"]["lsattribute"]["node"]["localRouterId"]
                lab.connect_machine_to_link(r1.name, functions.numbers_to_words(collision_domain))
                lab.update_file_from_string(content=f"/sbin/ifconfig eth{r1.interfaces.__len__()-1} {r1_ip}/30 up\n", dst_path=f"{r1.name}.startup")

                r2 = routers[f"{edge[0]}"]
                lab.connect_machine_to_link(r2.name, functions.numbers_to_words(collision_domain)) 

                try:
                    lab.update_file_from_list(
                        lines=[
                            f"{r1.name}[{r1.interfaces.__len__()-1}]=\"{functions.numbers_to_words(collision_domain)}\"",
                            f"{r2.name}[{r2.interfaces.__len__()-1}]=\"{functions.numbers_to_words(collision_domain)}\"",
                        ],
                        dst_path="lab.conf")
                except:
                    lab.create_file_from_list(
                        lines=[
                            f"{r1.name}[{r1.interfaces.__len__()-1}]=\"{functions.numbers_to_words(collision_domain)}\"",
                            f"{r2.name}[{r2.interfaces.__len__()-1}]=\"{functions.numbers_to_words(collision_domain)}\"",
                        ],
                        dst_path="lab.conf")
            except:
                r1 = routers[f"{edge[1]}"]
                if r1.name=="pe1" : print(r1.interfaces)
                r1_ip = edge[2]["lsa"]["linkDescriptor"]["interfaceAddrIpv4"]
                lab.connect_machine_to_link(r1.name, functions.numbers_to_words(collision_domain))
                if r1.name=="pe1" : print(r1.interfaces)
                lab.update_file_from_string(content=f"/sbin/ifconfig eth{r1.interfaces.__len__()-1} {r1_ip}/30 up\n", dst_path=f"{r1.name}.startup")
                
                r2 = routers[f"{edge[0]}"]
                lab.connect_machine_to_link(r2.name, functions.numbers_to_words(collision_domain)) 
                

                try:
                    lab.update_file_from_list(
                        lines=[
                            f"{r1.name}[{r1.interfaces.__len__()-1}]=\"{functions.numbers_to_words(collision_domain)}\"",
                            f"{r2.name}[{r2.interfaces.__len__()-1}]=\"{functions.numbers_to_words(collision_domain)}\"",
                        ],
                        dst_path="lab.conf")
                except:
                    lab.create_file_from_list(
                        lines=[
                            f"{r1.name}[{r1.interfaces.__len__()-1}]=\"{functions.numbers_to_words(collision_domain)}\"",
                            f"{r2.name}[{r2.interfaces.__len__()-1}]=\"{functions.numbers_to_words(collision_domain)}\"",
                        ],
                        dst_path="lab.conf")
                
    else:    
        try:
            # Starting the process to connect the first router of the edge to new collision domain
            r1=routers[f"{edge[1]}"]
            r1_ip = edge[2]["lsa"]["linkDescriptor"]["interfaceAddrIpv4"]
            
            # Connecting first router
            lab.connect_machine_to_link(r1.name, functions.numbers_to_words(collision_domain))
            
            # Updating (or creating if it doesn't exist) the startup file for the first router
            lab.update_file_from_string(content=f"/sbin/ifconfig eth{r1.interfaces.__len__()-1} {r1_ip}/30 up\n", dst_path=f"{r1.name}.startup")
        except: 
            pass

        try:        
            # Starting the process to connect the second router of the edge to the same collision domain
            r2=routers[f"{edge[0]}"]
            r2_ip = edge[2]["lsa"]["linkDescriptor"]["neighborAddrIpv4"]

            # Connecting second router 
            lab.connect_machine_to_link(r2.name, functions.numbers_to_words(collision_domain))
            
            # Updating (or creating if it doesn't exist) the startup file for the second router
            lab.update_file_from_string(content=f"/sbin/ifconfig eth{r2.interfaces.__len__()-1} {r2_ip}/30 up\n", dst_path=f"{r2.name}.startup")
        except:
            pass

        try:
            lab.update_file_from_list(
                lines=[
                    f"{r1.name}[{r1.interfaces.__len__()-1}]=\"{functions.numbers_to_words(collision_domain)}\"",
                    f"{r2.name}[{r2.interfaces.__len__()-1}]=\"{functions.numbers_to_words(collision_domain)}\"",
                ],
                dst_path="lab.conf")
        except:
            lab.create_file_from_list(
                lines=[
                    f"{r1.name}[{r1.interfaces.__len__()-1}]=\"{functions.numbers_to_words(collision_domain)}\"",
                    f"{r2.name}[{r2.interfaces.__len__()-1}]=\"{functions.numbers_to_words(collision_domain)}\"",
                ],
                dst_path="lab.conf")
            
    collision_domain += 1 # Update the name for the next domain

for r in routers:
    if (not graph.nodes.get(r)["lsa"]) or ("pseudonode" in graph.nodes.get(r)["lsa"]["localNode"].keys()):

        lab.update_file_from_list(
                lines=[
                    f"{routers[r].name}[image]=kathara/base",
                    f"{routers[r].name}[ipv6]=false",
                    f"{routers[r].name}[num_terms]=0",
                ],
                dst_path="lab.conf")
        
    else:    
        # updating startup files to allow frr starting
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
            "enable password frr",
            "" 
            ],
            dst_path= "/etc/frr/zebra.conf"
        )
        # Looking for the ip addresses of the interfaces in the startup files of the fs
        with lab.fs.open(f"{routers[r].name}.startup") as file:
            for line in file:
                words_of_the_line = line.strip().split()
                # Update the zebra.conf file with the ip addresses
                functions.configure_zebra(routers[r], words_of_the_line)
        
        igpRouterId = graph.nodes.get(r)["lsa"]["localNode"]["igpRouterId"]
        igpArea = graph.nodes.get(r)["lsa"]["lsattribute"]["node"]["isisArea"]

        # Starting configuration of isis
        routers[r].create_file_from_list(
            lines=[
            f"router isis {igpArea}",
            f" net 49.0000.{igpRouterId}.00"
            ],
            dst_path= "/etc/frr/isisd.conf"
        )
        for interface in routers[r].interfaces:
            routers[r].update_file_from_list(
                lines=[
                    "",
                    f"interface eth{interface}",
                    f" ip router isis {igpArea}",
                    ""
                ],
                dst_path= "etc/frr/isisd.conf")
            
        lab.update_file_from_list(
                lines=[
                    f"{routers[r].name}[image]=kathara/frr",
                    f"{routers[r].name}[ipv6]=false",
                    f"{routers[r].name}[num_terms]=0",
                ],
                dst_path="lab.conf")


lab.update_file_from_list(
            lines=[
                "wireshark[bridged]=true",
                "wireshark[port]=\"3000:3000\"",
                "wireshark[image]=\"lscr.io/linuxserver/wireshark\"",
                "wireshark[num_terms]=0",
            ],
            dst_path="lab.conf")


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