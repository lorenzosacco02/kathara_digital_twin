from Kathara.model.Lab import Lab
from Kathara.manager.Kathara import Kathara
import bgp_ls_vis.proto as proto
import bgp_ls_vis.graphing as graphing

# Create lab
lab = Lab("18_nodes_twin")

# To load a BGP-LS table from file instead of a gRPC connection, `connect` param is set false
rpc = proto.GoBGPQueryWrapper(connect=False)

# Calling get_lsdb with param `filename` set will trigger loading from file instead of RPC
first_example_dir = r"C:/Users/lolli/Desktop/kathara_digital_twin/dumps"
lsdb = rpc.get_lsdb(filename=fr"{first_example_dir}/18-node-isis-w-bcast-segment.yaml")
graph = graphing.build_nx_from_lsdb(lsdb)

print(graph)

# Deploy lab
#Kathara.get_instance().deploy_lab(lab=lab)

# Undeploy lab
#Kathara.get_instance().undeploy_lab(lab=lab)