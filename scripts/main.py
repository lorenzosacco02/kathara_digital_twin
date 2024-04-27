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
#graphing.draw_pyplot_graph(graph)

routers = []

for node in graph.nodes(data=True):
    if node[1]["lsa"]!=None:
        routers.append(lab.new_machine(f"{node[0].lower()}", **{"image": "kathara/frr"}))
        print(f"aggiunto {node[0]} al lab")    
        neig = [n for n in graph.neighbors(node[0])]
        print(neig)
        break


#fs = open_fs(fr"osfs://C:\Users\lolli\Desktop\kathara_digital_twin\lab")
#copy_fs(lab.fs, fs)


"""for edge in graph.edges(data=True):
    if edge[2]["lsa"]["linkDescriptor"]:
        print(f"{edge[:2]}", edge[2]["lsa"]["linkDescriptor"])
"""

# Deploy lab
#Kathara.get_instance().deploy_lab(lab=lab)

# Undeploy lab
#Kathara.get_instance().undeploy_lab(lab=lab)