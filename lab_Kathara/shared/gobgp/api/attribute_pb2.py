# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: attribute.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
import gobgp_pb2 as gobgp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x61ttribute.proto\x12\x05\x61pipb\x1a\x19google/protobuf/any.proto\x1a\x0bgobgp.proto\"!\n\x0fOriginAttribute\x12\x0e\n\x06origin\x18\x01 \x01(\r\"\x9e\x01\n\tAsSegment\x12#\n\x04type\x18\x01 \x01(\x0e\x32\x15.apipb.AsSegment.Type\x12\x0f\n\x07numbers\x18\x02 \x03(\r\"[\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06\x41S_SET\x10\x01\x12\x0f\n\x0b\x41S_SEQUENCE\x10\x02\x12\x16\n\x12\x41S_CONFED_SEQUENCE\x10\x03\x12\x11\n\rAS_CONFED_SET\x10\x04\"5\n\x0f\x41sPathAttribute\x12\"\n\x08segments\x18\x01 \x03(\x0b\x32\x10.apipb.AsSegment\"$\n\x10NextHopAttribute\x12\x10\n\x08next_hop\x18\x01 \x01(\t\"%\n\x16MultiExitDiscAttribute\x12\x0b\n\x03med\x18\x01 \x01(\r\"(\n\x12LocalPrefAttribute\x12\x12\n\nlocal_pref\x18\x01 \x01(\r\"\x1a\n\x18\x41tomicAggregateAttribute\"3\n\x13\x41ggregatorAttribute\x12\x0b\n\x03\x61sn\x18\x01 \x01(\r\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\"+\n\x14\x43ommunitiesAttribute\x12\x13\n\x0b\x63ommunities\x18\x01 \x03(\r\"#\n\x15OriginatorIdAttribute\x12\n\n\x02id\x18\x01 \x01(\t\"#\n\x14\x43lusterListAttribute\x12\x0b\n\x03ids\x18\x01 \x03(\t\"5\n\x0fIPAddressPrefix\x12\x12\n\nprefix_len\x18\x01 \x01(\r\x12\x0e\n\x06prefix\x18\x02 \x01(\t\"L\n\x16LabeledIPAddressPrefix\x12\x0e\n\x06labels\x18\x01 \x03(\r\x12\x12\n\nprefix_len\x18\x02 \x01(\r\x12\x0e\n\x06prefix\x18\x03 \x01(\t\"$\n\x11\x45ncapsulationNLRI\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\"@\n\x1dRouteDistinguisherTwoOctetASN\x12\r\n\x05\x61\x64min\x18\x01 \x01(\r\x12\x10\n\x08\x61ssigned\x18\x02 \x01(\r\">\n\x1bRouteDistinguisherIPAddress\x12\r\n\x05\x61\x64min\x18\x01 \x01(\t\x12\x10\n\x08\x61ssigned\x18\x02 \x01(\r\"A\n\x1eRouteDistinguisherFourOctetASN\x12\r\n\x05\x61\x64min\x18\x01 \x01(\r\x12\x10\n\x08\x61ssigned\x18\x02 \x01(\r\"8\n\x19\x45thernetSegmentIdentifier\x12\x0c\n\x04type\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\x0c\"\x85\x01\n\x08VPLSNLRI\x12 \n\x02rd\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\x12\r\n\x05ve_id\x18\x02 \x01(\r\x12\x17\n\x0fve_block_offset\x18\x03 \x01(\r\x12\x15\n\rve_block_size\x18\x04 \x01(\r\x12\x18\n\x10label_block_base\x18\x05 \x01(\r\"\x96\x01\n\x1e\x45VPNEthernetAutoDiscoveryRoute\x12 \n\x02rd\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\x12-\n\x03\x65si\x18\x02 \x01(\x0b\x32 .apipb.EthernetSegmentIdentifier\x12\x14\n\x0c\x65thernet_tag\x18\x03 \x01(\r\x12\r\n\x05label\x18\x04 \x01(\r\"\xbd\x01\n\x1b\x45VPNMACIPAdvertisementRoute\x12 \n\x02rd\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\x12-\n\x03\x65si\x18\x02 \x01(\x0b\x32 .apipb.EthernetSegmentIdentifier\x12\x14\n\x0c\x65thernet_tag\x18\x03 \x01(\r\x12\x13\n\x0bmac_address\x18\x04 \x01(\t\x12\x12\n\nip_address\x18\x05 \x01(\t\x12\x0e\n\x06labels\x18\x06 \x03(\r\"t\n&EVPNInclusiveMulticastEthernetTagRoute\x12 \n\x02rd\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x14\n\x0c\x65thernet_tag\x18\x02 \x01(\r\x12\x12\n\nip_address\x18\x03 \x01(\t\"\x7f\n\x18\x45VPNEthernetSegmentRoute\x12 \n\x02rd\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\x12-\n\x03\x65si\x18\x02 \x01(\x0b\x32 .apipb.EthernetSegmentIdentifier\x12\x12\n\nip_address\x18\x03 \x01(\t\"\xc7\x01\n\x11\x45VPNIPPrefixRoute\x12 \n\x02rd\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\x12-\n\x03\x65si\x18\x02 \x01(\x0b\x32 .apipb.EthernetSegmentIdentifier\x12\x14\n\x0c\x65thernet_tag\x18\x03 \x01(\r\x12\x11\n\tip_prefix\x18\x04 \x01(\t\x12\x15\n\rip_prefix_len\x18\x05 \x01(\r\x12\x12\n\ngw_address\x18\x06 \x01(\t\x12\r\n\x05label\x18\x07 \x01(\r\"j\n\x0e\x45VPNIPMSIRoute\x12 \n\x02rd\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x14\n\x0c\x65thernet_tag\x18\x02 \x01(\r\x12 \n\x02rt\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any\"V\n\x0cSRPolicyNLRI\x12\x0e\n\x06length\x18\x01 \x01(\r\x12\x15\n\rdistinguisher\x18\x02 \x01(\r\x12\r\n\x05\x63olor\x18\x03 \x01(\r\x12\x10\n\x08\x65ndpoint\x18\x04 \x01(\x0c\"q\n\x19LabeledVPNIPAddressPrefix\x12\x0e\n\x06labels\x18\x01 \x03(\r\x12 \n\x02rd\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x12\n\nprefix_len\x18\x03 \x01(\r\x12\x0e\n\x06prefix\x18\x04 \x01(\t\"J\n\x19RouteTargetMembershipNLRI\x12\x0b\n\x03\x61sn\x18\x01 \x01(\r\x12 \n\x02rt\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\"T\n\x10\x46lowSpecIPPrefix\x12\x0c\n\x04type\x18\x01 \x01(\r\x12\x12\n\nprefix_len\x18\x02 \x01(\r\x12\x0e\n\x06prefix\x18\x03 \x01(\t\x12\x0e\n\x06offset\x18\x04 \x01(\r\",\n\x0b\x46lowSpecMAC\x12\x0c\n\x04type\x18\x01 \x01(\r\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\"2\n\x15\x46lowSpecComponentItem\x12\n\n\x02op\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\x04\"N\n\x11\x46lowSpecComponent\x12\x0c\n\x04type\x18\x01 \x01(\r\x12+\n\x05items\x18\x02 \x03(\x0b\x32\x1c.apipb.FlowSpecComponentItem\"3\n\x0c\x46lowSpecNLRI\x12#\n\x05rules\x18\x01 \x03(\x0b\x32\x14.google.protobuf.Any\"X\n\x0fVPNFlowSpecNLRI\x12 \n\x02rd\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\x12#\n\x05rules\x18\x02 \x03(\x0b\x32\x14.google.protobuf.Any\"(\n\nOpaqueNLRI\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c\"\xac\x01\n\x10LsNodeDescriptor\x12\x0b\n\x03\x61sn\x18\x01 \x01(\r\x12\x11\n\tbgp_ls_id\x18\x02 \x01(\r\x12\x14\n\x0cospf_area_id\x18\x03 \x01(\r\x12\x12\n\npseudonode\x18\x04 \x01(\x08\x12\x15\n\rigp_router_id\x18\x05 \x01(\t\x12\x15\n\rbgp_router_id\x18\x06 \x01(\t\x12 \n\x18\x62gp_confederation_member\x18\x07 \x01(\r\"\xb3\x01\n\x10LsLinkDescriptor\x12\x15\n\rlink_local_id\x18\x01 \x01(\r\x12\x16\n\x0elink_remote_id\x18\x02 \x01(\r\x12\x1b\n\x13interface_addr_ipv4\x18\x03 \x01(\t\x12\x1a\n\x12neighbor_addr_ipv4\x18\x04 \x01(\t\x12\x1b\n\x13interface_addr_ipv6\x18\x05 \x01(\t\x12\x1a\n\x12neighbor_addr_ipv6\x18\x06 \x01(\t\"^\n\x12LsPrefixDescriptor\x12\x17\n\x0fip_reachability\x18\x01 \x03(\t\x12/\n\x0fospf_route_type\x18\x02 \x01(\x0e\x32\x16.apipb.LsOspfRouteType\"9\n\nLsNodeNLRI\x12+\n\nlocal_node\x18\x01 \x01(\x0b\x32\x17.apipb.LsNodeDescriptor\"\x99\x01\n\nLsLinkNLRI\x12+\n\nlocal_node\x18\x01 \x01(\x0b\x32\x17.apipb.LsNodeDescriptor\x12,\n\x0bremote_node\x18\x02 \x01(\x0b\x32\x17.apipb.LsNodeDescriptor\x12\x30\n\x0flink_descriptor\x18\x03 \x01(\x0b\x32\x17.apipb.LsLinkDescriptor\"s\n\x0eLsPrefixV4NLRI\x12+\n\nlocal_node\x18\x01 \x01(\x0b\x32\x17.apipb.LsNodeDescriptor\x12\x34\n\x11prefix_descriptor\x18\x02 \x01(\x0b\x32\x19.apipb.LsPrefixDescriptor\"s\n\x0eLsPrefixV6NLRI\x12+\n\nlocal_node\x18\x01 \x01(\x0b\x32\x17.apipb.LsNodeDescriptor\x12\x34\n\x11prefix_descriptor\x18\x02 \x01(\x0b\x32\x19.apipb.LsPrefixDescriptor\"\xa1\x01\n\x0cLsAddrPrefix\x12\x1f\n\x04type\x18\x01 \x01(\x0e\x32\x11.apipb.LsNLRIType\x12\"\n\x04nlri\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x0e\n\x06length\x18\x03 \x01(\r\x12(\n\x0bprotocol_id\x18\x04 \x01(\x0e\x32\x13.apipb.LsProtocolID\x12\x12\n\nidentifier\x18\x05 \x01(\x04\"U\n!MUPInterworkSegmentDiscoveryRoute\x12 \n\x02rd\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x0e\n\x06prefix\x18\x02 \x01(\t\"S\n\x1eMUPDirectSegmentDiscoveryRoute\x12 \n\x02rd\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\"\xfb\x01\n\x1fMUPType1SessionTransformedRoute\x12 \n\x02rd\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x19\n\rprefix_length\x18\x02 \x01(\rB\x02\x18\x01\x12\x0e\n\x06prefix\x18\x03 \x01(\t\x12\x0c\n\x04teid\x18\x04 \x01(\r\x12\x0b\n\x03qfi\x18\x05 \x01(\r\x12\x1f\n\x17\x65ndpoint_address_length\x18\x06 \x01(\r\x12\x18\n\x10\x65ndpoint_address\x18\x07 \x01(\t\x12\x1d\n\x15source_address_length\x18\x08 \x01(\r\x12\x16\n\x0esource_address\x18\t \x01(\t\"\x8c\x01\n\x1fMUPType2SessionTransformedRoute\x12 \n\x02rd\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x1f\n\x17\x65ndpoint_address_length\x18\x02 \x01(\r\x12\x18\n\x10\x65ndpoint_address\x18\x03 \x01(\t\x12\x0c\n\x04teid\x18\x04 \x01(\r\"m\n\x14MpReachNLRIAttribute\x12\x1d\n\x06\x66\x61mily\x18\x01 \x01(\x0b\x32\r.apipb.Family\x12\x11\n\tnext_hops\x18\x02 \x03(\t\x12#\n\x05nlris\x18\x03 \x03(\x0b\x32\x14.google.protobuf.Any\"\\\n\x16MpUnreachNLRIAttribute\x12\x1d\n\x06\x66\x61mily\x18\x01 \x01(\x0b\x32\r.apipb.Family\x12#\n\x05nlris\x18\x03 \x03(\x0b\x32\x14.google.protobuf.Any\"g\n\x1aTwoOctetAsSpecificExtended\x12\x15\n\ris_transitive\x18\x01 \x01(\x08\x12\x10\n\x08sub_type\x18\x02 \x01(\r\x12\x0b\n\x03\x61sn\x18\x03 \x01(\r\x12\x13\n\x0blocal_admin\x18\x04 \x01(\r\"l\n\x1bIPv4AddressSpecificExtended\x12\x15\n\ris_transitive\x18\x01 \x01(\x08\x12\x10\n\x08sub_type\x18\x02 \x01(\r\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x01(\t\x12\x13\n\x0blocal_admin\x18\x04 \x01(\r\"h\n\x1b\x46ourOctetAsSpecificExtended\x12\x15\n\ris_transitive\x18\x01 \x01(\x08\x12\x10\n\x08sub_type\x18\x02 \x01(\r\x12\x0b\n\x03\x61sn\x18\x03 \x01(\r\x12\x13\n\x0blocal_admin\x18\x04 \x01(\r\"7\n\x15LinkBandwidthExtended\x12\x0b\n\x03\x61sn\x18\x01 \x01(\r\x12\x11\n\tbandwidth\x18\x02 \x01(\x02\"#\n\x12ValidationExtended\x12\r\n\x05state\x18\x01 \x01(\r\"\x1e\n\rColorExtended\x12\r\n\x05\x63olor\x18\x01 \x01(\r\"$\n\rEncapExtended\x12\x13\n\x0btunnel_type\x18\x01 \x01(\r\"\x18\n\x16\x44\x65\x66\x61ultGatewayExtended\"6\n\x0eOpaqueExtended\x12\x15\n\ris_transitive\x18\x01 \x01(\x08\x12\r\n\x05value\x18\x03 \x01(\x0c\";\n\x10\x45SILabelExtended\x12\x18\n\x10is_single_active\x18\x01 \x01(\x08\x12\r\n\x05label\x18\x02 \x01(\r\"(\n\x13\x45SImportRouteTarget\x12\x11\n\tes_import\x18\x01 \x01(\t\">\n\x13MacMobilityExtended\x12\x11\n\tis_sticky\x18\x01 \x01(\x08\x12\x14\n\x0csequence_num\x18\x02 \x01(\r\" \n\x11RouterMacExtended\x12\x0b\n\x03mac\x18\x01 \x01(\t\"0\n\x13TrafficRateExtended\x12\x0b\n\x03\x61sn\x18\x01 \x01(\r\x12\x0c\n\x04rate\x18\x02 \x01(\x02\"9\n\x15TrafficActionExtended\x12\x10\n\x08terminal\x18\x01 \x01(\x08\x12\x0e\n\x06sample\x18\x02 \x01(\x08\"F\n\"RedirectTwoOctetAsSpecificExtended\x12\x0b\n\x03\x61sn\x18\x01 \x01(\r\x12\x13\n\x0blocal_admin\x18\x02 \x01(\r\"K\n#RedirectIPv4AddressSpecificExtended\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x13\n\x0blocal_admin\x18\x02 \x01(\r\"G\n#RedirectFourOctetAsSpecificExtended\x12\x0b\n\x03\x61sn\x18\x01 \x01(\r\x12\x13\n\x0blocal_admin\x18\x02 \x01(\r\"%\n\x15TrafficRemarkExtended\x12\x0c\n\x04\x64scp\x18\x01 \x01(\r\"I\n\x0bMUPExtended\x12\x10\n\x08sub_type\x18\x01 \x01(\r\x12\x13\n\x0bsegment_id2\x18\x02 \x01(\r\x12\x13\n\x0bsegment_id4\x18\x03 \x01(\r\"2\n\x0cVPLSExtended\x12\x15\n\rcontrol_flags\x18\x01 \x01(\r\x12\x0b\n\x03mtu\x18\x02 \x01(\r\".\n\x0fUnknownExtended\x12\x0c\n\x04type\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\x0c\"I\n\x1c\x45xtendedCommunitiesAttribute\x12)\n\x0b\x63ommunities\x18\x01 \x03(\x0b\x32\x14.google.protobuf.Any\"6\n\x10\x41s4PathAttribute\x12\"\n\x08segments\x18\x01 \x03(\x0b\x32\x10.apipb.AsSegment\"6\n\x16\x41s4AggregatorAttribute\x12\x0b\n\x03\x61sn\x18\x02 \x01(\r\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x01(\t\"M\n\x13PmsiTunnelAttribute\x12\r\n\x05\x66lags\x18\x01 \x01(\r\x12\x0c\n\x04type\x18\x02 \x01(\r\x12\r\n\x05label\x18\x03 \x01(\r\x12\n\n\x02id\x18\x04 \x01(\x0c\"=\n\x1eTunnelEncapSubTLVEncapsulation\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\x0e\n\x06\x63ookie\x18\x02 \x01(\x0c\"-\n\x19TunnelEncapSubTLVProtocol\x12\x10\n\x08protocol\x18\x01 \x01(\r\"\'\n\x16TunnelEncapSubTLVColor\x12\r\n\x05\x63olor\x18\x01 \x01(\r\"B\n\x1dTunnelEncapSubTLVSRPreference\x12\r\n\x05\x66lags\x18\x01 \x01(\r\x12\x12\n\npreference\x18\x02 \x01(\r\"C\n$TunnelEncapSubTLVSRCandidatePathName\x12\x1b\n\x13\x63\x61ndidate_path_name\x18\x01 \x01(\t\"/\n\x1bTunnelEncapSubTLVSRPriority\x12\x10\n\x08priority\x18\x01 \x01(\r\"C\n\x1dTunnelEncapSubTLVSRBindingSID\x12\"\n\x04\x62sid\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\";\n\x0cSRBindingSID\x12\x0e\n\x06s_flag\x18\x01 \x01(\x08\x12\x0e\n\x06i_flag\x18\x02 \x01(\x08\x12\x0b\n\x03sid\x18\x03 \x01(\x0c\"\x85\x01\n\x14SRv6EndPointBehavior\x12%\n\x08\x62\x65havior\x18\x01 \x01(\x0e\x32\x13.apipb.SRv6Behavior\x12\x11\n\tblock_len\x18\x02 \x01(\r\x12\x10\n\x08node_len\x18\x03 \x01(\r\x12\x10\n\x08\x66unc_len\x18\x04 \x01(\r\x12\x0f\n\x07\x61rg_len\x18\x05 \x01(\r\"\x8f\x01\n\x0eSRv6BindingSID\x12\x0e\n\x06s_flag\x18\x01 \x01(\x08\x12\x0e\n\x06i_flag\x18\x02 \x01(\x08\x12\x0e\n\x06\x62_flag\x18\x03 \x01(\x08\x12\x0b\n\x03sid\x18\x04 \x01(\x0c\x12@\n\x1b\x65ndpoint_behavior_structure\x18\x05 \x01(\x0b\x32\x1b.apipb.SRv6EndPointBehavior\"G\n\x17TunnelEncapSubTLVSRENLP\x12\r\n\x05\x66lags\x18\x01 \x01(\r\x12\x1d\n\x04\x65nlp\x18\x02 \x01(\x0e\x32\x0f.apipb.ENLPType\")\n\x08SRWeight\x12\r\n\x05\x66lags\x18\x01 \x01(\r\x12\x0e\n\x06weight\x18\x02 \x01(\r\"N\n\x0cSegmentFlags\x12\x0e\n\x06v_flag\x18\x01 \x01(\x08\x12\x0e\n\x06\x61_flag\x18\x02 \x01(\x08\x12\x0e\n\x06s_flag\x18\x03 \x01(\x08\x12\x0e\n\x06\x62_flag\x18\x04 \x01(\x08\"A\n\x0cSegmentTypeA\x12\"\n\x05\x66lags\x18\x01 \x01(\x0b\x32\x13.apipb.SegmentFlags\x12\r\n\x05label\x18\x02 \x01(\r\"\x81\x01\n\x0cSegmentTypeB\x12\"\n\x05\x66lags\x18\x01 \x01(\x0b\x32\x13.apipb.SegmentFlags\x12\x0b\n\x03sid\x18\x02 \x01(\x0c\x12@\n\x1b\x65ndpoint_behavior_structure\x18\x03 \x01(\x0b\x32\x1b.apipb.SRv6EndPointBehavior\"i\n\x1eTunnelEncapSubTLVSRSegmentList\x12\x1f\n\x06weight\x18\x01 \x01(\x0b\x32\x0f.apipb.SRWeight\x12&\n\x08segments\x18\x02 \x03(\x0b\x32\x14.google.protobuf.Any\"2\n\x1fTunnelEncapSubTLVEgressEndpoint\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\",\n\x1cTunnelEncapSubTLVUDPDestPort\x12\x0c\n\x04port\x18\x01 \x01(\r\"7\n\x18TunnelEncapSubTLVUnknown\x12\x0c\n\x04type\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\x0c\"B\n\x0eTunnelEncapTLV\x12\x0c\n\x04type\x18\x01 \x01(\r\x12\"\n\x04tlvs\x18\x02 \x03(\x0b\x32\x14.google.protobuf.Any\";\n\x14TunnelEncapAttribute\x12#\n\x04tlvs\x18\x01 \x03(\x0b\x32\x15.apipb.TunnelEncapTLV\"l\n\x1bIPv6AddressSpecificExtended\x12\x15\n\ris_transitive\x18\x01 \x01(\x08\x12\x10\n\x08sub_type\x18\x02 \x01(\r\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x01(\t\x12\x13\n\x0blocal_admin\x18\x04 \x01(\r\"K\n#RedirectIPv6AddressSpecificExtended\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x13\n\x0blocal_admin\x18\x02 \x01(\r\"L\n\x1fIP6ExtendedCommunitiesAttribute\x12)\n\x0b\x63ommunities\x18\x01 \x03(\x0b\x32\x14.google.protobuf.Any\"\"\n\x10\x41igpTLVIGPMetric\x12\x0e\n\x06metric\x18\x01 \x01(\x04\"-\n\x0e\x41igpTLVUnknown\x12\x0c\n\x04type\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\x0c\"3\n\rAigpAttribute\x12\"\n\x04tlvs\x18\x01 \x03(\x0b\x32\x14.google.protobuf.Any\"P\n\x0eLargeCommunity\x12\x14\n\x0cglobal_admin\x18\x01 \x01(\r\x12\x13\n\x0blocal_data1\x18\x02 \x01(\r\x12\x13\n\x0blocal_data2\x18\x03 \x01(\r\"G\n\x19LargeCommunitiesAttribute\x12*\n\x0b\x63ommunities\x18\x01 \x03(\x0b\x32\x15.apipb.LargeCommunity\"l\n\x0bLsNodeFlags\x12\x10\n\x08overload\x18\x01 \x01(\x08\x12\x10\n\x08\x61ttached\x18\x02 \x01(\x08\x12\x10\n\x08\x65xternal\x18\x03 \x01(\x08\x12\x0b\n\x03\x61\x62r\x18\x04 \x01(\x08\x12\x0e\n\x06router\x18\x05 \x01(\x08\x12\n\n\x02v6\x18\x06 \x01(\x08\"]\n\nLsIGPFlags\x12\x0c\n\x04\x64own\x18\x01 \x01(\x08\x12\x12\n\nno_unicast\x18\x02 \x01(\x08\x12\x15\n\rlocal_address\x18\x03 \x01(\x08\x12\x16\n\x0epropagate_nssa\x18\x04 \x01(\x08\"\'\n\tLsSrRange\x12\r\n\x05\x62\x65gin\x18\x01 \x01(\r\x12\x0b\n\x03\x65nd\x18\x02 \x01(\r\"d\n\x10LsSrCapabilities\x12\x16\n\x0eipv4_supported\x18\x01 \x01(\x08\x12\x16\n\x0eipv6_supported\x18\x02 \x01(\x08\x12 \n\x06ranges\x18\x03 \x03(\x0b\x32\x10.apipb.LsSrRange\"2\n\x0eLsSrLocalBlock\x12 \n\x06ranges\x18\x01 \x03(\x0b\x32\x10.apipb.LsSrRange\"\x92\x02\n\x0fLsAttributeNode\x12\x0c\n\x04name\x18\x01 \x01(\t\x12!\n\x05\x66lags\x18\x02 \x01(\x0b\x32\x12.apipb.LsNodeFlags\x12\x17\n\x0flocal_router_id\x18\x03 \x01(\t\x12\x1a\n\x12local_router_id_v6\x18\x04 \x01(\t\x12\x11\n\tisis_area\x18\x05 \x01(\x0c\x12\x0e\n\x06opaque\x18\x06 \x01(\x0c\x12\x30\n\x0fsr_capabilities\x18\x07 \x01(\x0b\x32\x17.apipb.LsSrCapabilities\x12\x15\n\rsr_algorithms\x18\x08 \x01(\x0c\x12-\n\x0esr_local_block\x18\t \x01(\x0b\x32\x15.apipb.LsSrLocalBlock\"\xd7\x02\n\x0fLsAttributeLink\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x17\n\x0flocal_router_id\x18\x02 \x01(\t\x12\x1a\n\x12local_router_id_v6\x18\x03 \x01(\t\x12\x18\n\x10remote_router_id\x18\x04 \x01(\t\x12\x1b\n\x13remote_router_id_v6\x18\x05 \x01(\t\x12\x13\n\x0b\x61\x64min_group\x18\x06 \x01(\r\x12\x19\n\x11\x64\x65\x66\x61ult_te_metric\x18\x07 \x01(\r\x12\x12\n\nigp_metric\x18\x08 \x01(\r\x12\x0e\n\x06opaque\x18\t \x01(\x0c\x12\x11\n\tbandwidth\x18\n \x01(\x02\x12\x1c\n\x14reservable_bandwidth\x18\x0b \x01(\x02\x12\x1c\n\x14unreserved_bandwidth\x18\x0c \x03(\x02\x12\x18\n\x10sr_adjacency_sid\x18\r \x01(\r\x12\r\n\x05srlgs\x18\x0e \x03(\r\"`\n\x11LsAttributePrefix\x12$\n\tigp_flags\x18\x01 \x01(\x0b\x32\x11.apipb.LsIGPFlags\x12\x0e\n\x06opaque\x18\x02 \x01(\x0c\x12\x15\n\rsr_prefix_sid\x18\x03 \x01(\r\"\\\n\x18LsBgpPeerSegmentSIDFlags\x12\r\n\x05value\x18\x01 \x01(\x08\x12\r\n\x05local\x18\x02 \x01(\x08\x12\x0e\n\x06\x62\x61\x63kup\x18\x03 \x01(\x08\x12\x12\n\npersistent\x18\x04 \x01(\x08\"b\n\x13LsBgpPeerSegmentSID\x12.\n\x05\x66lags\x18\x01 \x01(\x0b\x32\x1f.apipb.LsBgpPeerSegmentSIDFlags\x12\x0e\n\x06weight\x18\x02 \x01(\r\x12\x0b\n\x03sid\x18\x03 \x01(\r\"\xc4\x01\n\x19LsAttributeBgpPeerSegment\x12\x35\n\x11\x62gp_peer_node_sid\x18\x01 \x01(\x0b\x32\x1a.apipb.LsBgpPeerSegmentSID\x12:\n\x16\x62gp_peer_adjacency_sid\x18\x02 \x01(\x0b\x32\x1a.apipb.LsBgpPeerSegmentSID\x12\x34\n\x10\x62gp_peer_set_sid\x18\x03 \x01(\x0b\x32\x1a.apipb.LsBgpPeerSegmentSID\"\xbf\x01\n\x0bLsAttribute\x12$\n\x04node\x18\x01 \x01(\x0b\x32\x16.apipb.LsAttributeNode\x12$\n\x04link\x18\x02 \x01(\x0b\x32\x16.apipb.LsAttributeLink\x12(\n\x06prefix\x18\x03 \x01(\x0b\x32\x18.apipb.LsAttributePrefix\x12:\n\x10\x62gp_peer_segment\x18\x04 \x01(\x0b\x32 .apipb.LsAttributeBgpPeerSegment\">\n\x10UnknownAttribute\x12\r\n\x05\x66lags\x18\x01 \x01(\r\x12\x0c\n\x04type\x18\x02 \x01(\r\x12\r\n\x05value\x18\x03 \x01(\x0c\"\xc1\x01\n\x16SRv6StructureSubSubTLV\x12\x1c\n\x14locator_block_length\x18\x01 \x01(\r\x12\x1b\n\x13locator_node_length\x18\x02 \x01(\r\x12\x17\n\x0f\x66unction_length\x18\x03 \x01(\r\x12\x17\n\x0f\x61rgument_length\x18\x04 \x01(\r\x12\x1c\n\x14transposition_length\x18\x05 \x01(\r\x12\x1c\n\x14transposition_offset\x18\x06 \x01(\r\"\x1e\n\x0cSRv6SIDFlags\x12\x0e\n\x06\x66lag_1\x18\x01 \x01(\x08\",\n\x07SRv6TLV\x12!\n\x03tlv\x18\x01 \x03(\x0b\x32\x14.google.protobuf.Any\"\xea\x01\n\x15SRv6InformationSubTLV\x12\x0b\n\x03sid\x18\x01 \x01(\x0c\x12\"\n\x05\x66lags\x18\x02 \x01(\x0b\x32\x13.apipb.SRv6SIDFlags\x12\x19\n\x11\x65ndpoint_behavior\x18\x03 \x01(\r\x12\x42\n\x0csub_sub_tlvs\x18\x04 \x03(\x0b\x32,.apipb.SRv6InformationSubTLV.SubSubTlvsEntry\x1a\x41\n\x0fSubSubTlvsEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\x1d\n\x05value\x18\x02 \x01(\x0b\x32\x0e.apipb.SRv6TLV:\x02\x38\x01\"\x8a\x01\n\x10SRv6L3ServiceTLV\x12\x36\n\x08sub_tlvs\x18\x01 \x03(\x0b\x32$.apipb.SRv6L3ServiceTLV.SubTlvsEntry\x1a>\n\x0cSubTlvsEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\x1d\n\x05value\x18\x02 \x01(\x0b\x32\x0e.apipb.SRv6TLV:\x02\x38\x01\"\x8a\x01\n\x10SRv6L2ServiceTLV\x12\x36\n\x08sub_tlvs\x18\x01 \x03(\x0b\x32$.apipb.SRv6L2ServiceTLV.SubTlvsEntry\x1a>\n\x0cSubTlvsEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\x1d\n\x05value\x18\x02 \x01(\x0b\x32\x0e.apipb.SRv6TLV:\x02\x38\x01\"/\n\tPrefixSID\x12\"\n\x04tlvs\x18\x01 \x03(\x0b\x32\x14.google.protobuf.Any*\xf7\x01\n\x0fLsOspfRouteType\x12\x1e\n\x1aLS_OSPF_ROUTE_TYPE_UNKNOWN\x10\x00\x12!\n\x1dLS_OSPF_ROUTE_TYPE_INTRA_AREA\x10\x01\x12!\n\x1dLS_OSPF_ROUTE_TYPE_INTER_AREA\x10\x02\x12 \n\x1cLS_OSPF_ROUTE_TYPE_EXTERNAL1\x10\x03\x12 \n\x1cLS_OSPF_ROUTE_TYPE_EXTERNAL2\x10\x04\x12\x1c\n\x18LS_OSPF_ROUTE_TYPE_NSSA1\x10\x05\x12\x1c\n\x18LS_OSPF_ROUTE_TYPE_NSSA2\x10\x06*s\n\nLsNLRIType\x12\x13\n\x0fLS_NLRI_UNKNOWN\x10\x00\x12\x10\n\x0cLS_NLRI_NODE\x10\x01\x12\x10\n\x0cLS_NLRI_LINK\x10\x02\x12\x15\n\x11LS_NLRI_PREFIX_V4\x10\x03\x12\x15\n\x11LS_NLRI_PREFIX_V6\x10\x04*\xbb\x01\n\x0cLsProtocolID\x12\x17\n\x13LS_PROTOCOL_UNKNOWN\x10\x00\x12\x17\n\x13LS_PROTOCOL_ISIS_L1\x10\x01\x12\x17\n\x13LS_PROTOCOL_ISIS_L2\x10\x02\x12\x17\n\x13LS_PROTOCOL_OSPF_V2\x10\x03\x12\x16\n\x12LS_PROTOCOL_DIRECT\x10\x04\x12\x16\n\x12LS_PROTOCOL_STATIC\x10\x05\x12\x17\n\x13LS_PROTOCOL_OSPF_V3\x10\x06*\xed\x05\n\x0cSRv6Behavior\x12\x0c\n\x08RESERVED\x10\x00\x12\x07\n\x03\x45ND\x10\x01\x12\x10\n\x0c\x45ND_WITH_PSP\x10\x02\x12\x10\n\x0c\x45ND_WITH_USP\x10\x03\x12\x14\n\x10\x45ND_WITH_PSP_USP\x10\x04\x12\x08\n\x04\x45NDX\x10\x05\x12\x11\n\rENDX_WITH_PSP\x10\x06\x12\x11\n\rENDX_WITH_USP\x10\x07\x12\x15\n\x11\x45NDX_WITH_PSP_USP\x10\x08\x12\x08\n\x04\x45NDT\x10\t\x12\x11\n\rENDT_WITH_PSP\x10\n\x12\x11\n\rENDT_WITH_USP\x10\x0b\x12\x15\n\x11\x45NDT_WITH_PSP_USP\x10\x0c\x12\x11\n\rEND_B6_ENCAPS\x10\x0e\x12\n\n\x06\x45ND_BM\x10\x0f\x12\x0b\n\x07\x45ND_DX6\x10\x10\x12\x0b\n\x07\x45ND_DX4\x10\x11\x12\x0b\n\x07\x45ND_DT6\x10\x12\x12\x0b\n\x07\x45ND_DT4\x10\x13\x12\x0c\n\x08\x45ND_DT46\x10\x14\x12\x0b\n\x07\x45ND_DX2\x10\x15\x12\x0c\n\x08\x45ND_DX2V\x10\x16\x12\x0c\n\x08\x45ND_DT2U\x10\x17\x12\x0c\n\x08\x45ND_DT2M\x10\x18\x12\x15\n\x11\x45ND_B6_ENCAPS_Red\x10\x1b\x12\x10\n\x0c\x45ND_WITH_USD\x10\x1c\x12\x14\n\x10\x45ND_WITH_PSP_USD\x10\x1d\x12\x14\n\x10\x45ND_WITH_USP_USD\x10\x1e\x12\x18\n\x14\x45ND_WITH_PSP_USP_USD\x10\x1f\x12\x11\n\rENDX_WITH_USD\x10 \x12\x15\n\x11\x45NDX_WITH_PSP_USD\x10!\x12\x15\n\x11\x45NDX_WITH_USP_USD\x10\"\x12\x19\n\x15\x45NDX_WITH_PSP_USP_USD\x10#\x12\x11\n\rENDT_WITH_USD\x10$\x12\x15\n\x11\x45NDT_WITH_PSP_USD\x10%\x12\x15\n\x11\x45NDT_WITH_USP_USD\x10&\x12\x19\n\x15\x45NDT_WITH_PSP_USP_USD\x10\'\x12\x0e\n\nENDM_GTP6D\x10\x45\x12\x0f\n\x0b\x45NDM_GTP6DI\x10\x46\x12\x0e\n\nENDM_GTP6E\x10G\x12\x0e\n\nENDM_GTP4E\x10H*D\n\x08\x45NLPType\x12\x0c\n\x08Reserved\x10\x00\x12\t\n\x05Type1\x10\x01\x12\t\n\x05Type2\x10\x02\x12\t\n\x05Type3\x10\x03\x12\t\n\x05Type4\x10\x04\x42$Z\"github.com/osrg/gobgp/v3/api;apipbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'attribute_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\"github.com/osrg/gobgp/v3/api;apipb'
  _globals['_MUPTYPE1SESSIONTRANSFORMEDROUTE'].fields_by_name['prefix_length']._options = None
  _globals['_MUPTYPE1SESSIONTRANSFORMEDROUTE'].fields_by_name['prefix_length']._serialized_options = b'\030\001'
  _globals['_SRV6INFORMATIONSUBTLV_SUBSUBTLVSENTRY']._options = None
  _globals['_SRV6INFORMATIONSUBTLV_SUBSUBTLVSENTRY']._serialized_options = b'8\001'
  _globals['_SRV6L3SERVICETLV_SUBTLVSENTRY']._options = None
  _globals['_SRV6L3SERVICETLV_SUBTLVSENTRY']._serialized_options = b'8\001'
  _globals['_SRV6L2SERVICETLV_SUBTLVSENTRY']._options = None
  _globals['_SRV6L2SERVICETLV_SUBTLVSENTRY']._serialized_options = b'8\001'
  _globals['_LSOSPFROUTETYPE']._serialized_start=10953
  _globals['_LSOSPFROUTETYPE']._serialized_end=11200
  _globals['_LSNLRITYPE']._serialized_start=11202
  _globals['_LSNLRITYPE']._serialized_end=11317
  _globals['_LSPROTOCOLID']._serialized_start=11320
  _globals['_LSPROTOCOLID']._serialized_end=11507
  _globals['_SRV6BEHAVIOR']._serialized_start=11510
  _globals['_SRV6BEHAVIOR']._serialized_end=12259
  _globals['_ENLPTYPE']._serialized_start=12261
  _globals['_ENLPTYPE']._serialized_end=12329
  _globals['_ORIGINATTRIBUTE']._serialized_start=66
  _globals['_ORIGINATTRIBUTE']._serialized_end=99
  _globals['_ASSEGMENT']._serialized_start=102
  _globals['_ASSEGMENT']._serialized_end=260
  _globals['_ASSEGMENT_TYPE']._serialized_start=169
  _globals['_ASSEGMENT_TYPE']._serialized_end=260
  _globals['_ASPATHATTRIBUTE']._serialized_start=262
  _globals['_ASPATHATTRIBUTE']._serialized_end=315
  _globals['_NEXTHOPATTRIBUTE']._serialized_start=317
  _globals['_NEXTHOPATTRIBUTE']._serialized_end=353
  _globals['_MULTIEXITDISCATTRIBUTE']._serialized_start=355
  _globals['_MULTIEXITDISCATTRIBUTE']._serialized_end=392
  _globals['_LOCALPREFATTRIBUTE']._serialized_start=394
  _globals['_LOCALPREFATTRIBUTE']._serialized_end=434
  _globals['_ATOMICAGGREGATEATTRIBUTE']._serialized_start=436
  _globals['_ATOMICAGGREGATEATTRIBUTE']._serialized_end=462
  _globals['_AGGREGATORATTRIBUTE']._serialized_start=464
  _globals['_AGGREGATORATTRIBUTE']._serialized_end=515
  _globals['_COMMUNITIESATTRIBUTE']._serialized_start=517
  _globals['_COMMUNITIESATTRIBUTE']._serialized_end=560
  _globals['_ORIGINATORIDATTRIBUTE']._serialized_start=562
  _globals['_ORIGINATORIDATTRIBUTE']._serialized_end=597
  _globals['_CLUSTERLISTATTRIBUTE']._serialized_start=599
  _globals['_CLUSTERLISTATTRIBUTE']._serialized_end=634
  _globals['_IPADDRESSPREFIX']._serialized_start=636
  _globals['_IPADDRESSPREFIX']._serialized_end=689
  _globals['_LABELEDIPADDRESSPREFIX']._serialized_start=691
  _globals['_LABELEDIPADDRESSPREFIX']._serialized_end=767
  _globals['_ENCAPSULATIONNLRI']._serialized_start=769
  _globals['_ENCAPSULATIONNLRI']._serialized_end=805
  _globals['_ROUTEDISTINGUISHERTWOOCTETASN']._serialized_start=807
  _globals['_ROUTEDISTINGUISHERTWOOCTETASN']._serialized_end=871
  _globals['_ROUTEDISTINGUISHERIPADDRESS']._serialized_start=873
  _globals['_ROUTEDISTINGUISHERIPADDRESS']._serialized_end=935
  _globals['_ROUTEDISTINGUISHERFOUROCTETASN']._serialized_start=937
  _globals['_ROUTEDISTINGUISHERFOUROCTETASN']._serialized_end=1002
  _globals['_ETHERNETSEGMENTIDENTIFIER']._serialized_start=1004
  _globals['_ETHERNETSEGMENTIDENTIFIER']._serialized_end=1060
  _globals['_VPLSNLRI']._serialized_start=1063
  _globals['_VPLSNLRI']._serialized_end=1196
  _globals['_EVPNETHERNETAUTODISCOVERYROUTE']._serialized_start=1199
  _globals['_EVPNETHERNETAUTODISCOVERYROUTE']._serialized_end=1349
  _globals['_EVPNMACIPADVERTISEMENTROUTE']._serialized_start=1352
  _globals['_EVPNMACIPADVERTISEMENTROUTE']._serialized_end=1541
  _globals['_EVPNINCLUSIVEMULTICASTETHERNETTAGROUTE']._serialized_start=1543
  _globals['_EVPNINCLUSIVEMULTICASTETHERNETTAGROUTE']._serialized_end=1659
  _globals['_EVPNETHERNETSEGMENTROUTE']._serialized_start=1661
  _globals['_EVPNETHERNETSEGMENTROUTE']._serialized_end=1788
  _globals['_EVPNIPPREFIXROUTE']._serialized_start=1791
  _globals['_EVPNIPPREFIXROUTE']._serialized_end=1990
  _globals['_EVPNIPMSIROUTE']._serialized_start=1992
  _globals['_EVPNIPMSIROUTE']._serialized_end=2098
  _globals['_SRPOLICYNLRI']._serialized_start=2100
  _globals['_SRPOLICYNLRI']._serialized_end=2186
  _globals['_LABELEDVPNIPADDRESSPREFIX']._serialized_start=2188
  _globals['_LABELEDVPNIPADDRESSPREFIX']._serialized_end=2301
  _globals['_ROUTETARGETMEMBERSHIPNLRI']._serialized_start=2303
  _globals['_ROUTETARGETMEMBERSHIPNLRI']._serialized_end=2377
  _globals['_FLOWSPECIPPREFIX']._serialized_start=2379
  _globals['_FLOWSPECIPPREFIX']._serialized_end=2463
  _globals['_FLOWSPECMAC']._serialized_start=2465
  _globals['_FLOWSPECMAC']._serialized_end=2509
  _globals['_FLOWSPECCOMPONENTITEM']._serialized_start=2511
  _globals['_FLOWSPECCOMPONENTITEM']._serialized_end=2561
  _globals['_FLOWSPECCOMPONENT']._serialized_start=2563
  _globals['_FLOWSPECCOMPONENT']._serialized_end=2641
  _globals['_FLOWSPECNLRI']._serialized_start=2643
  _globals['_FLOWSPECNLRI']._serialized_end=2694
  _globals['_VPNFLOWSPECNLRI']._serialized_start=2696
  _globals['_VPNFLOWSPECNLRI']._serialized_end=2784
  _globals['_OPAQUENLRI']._serialized_start=2786
  _globals['_OPAQUENLRI']._serialized_end=2826
  _globals['_LSNODEDESCRIPTOR']._serialized_start=2829
  _globals['_LSNODEDESCRIPTOR']._serialized_end=3001
  _globals['_LSLINKDESCRIPTOR']._serialized_start=3004
  _globals['_LSLINKDESCRIPTOR']._serialized_end=3183
  _globals['_LSPREFIXDESCRIPTOR']._serialized_start=3185
  _globals['_LSPREFIXDESCRIPTOR']._serialized_end=3279
  _globals['_LSNODENLRI']._serialized_start=3281
  _globals['_LSNODENLRI']._serialized_end=3338
  _globals['_LSLINKNLRI']._serialized_start=3341
  _globals['_LSLINKNLRI']._serialized_end=3494
  _globals['_LSPREFIXV4NLRI']._serialized_start=3496
  _globals['_LSPREFIXV4NLRI']._serialized_end=3611
  _globals['_LSPREFIXV6NLRI']._serialized_start=3613
  _globals['_LSPREFIXV6NLRI']._serialized_end=3728
  _globals['_LSADDRPREFIX']._serialized_start=3731
  _globals['_LSADDRPREFIX']._serialized_end=3892
  _globals['_MUPINTERWORKSEGMENTDISCOVERYROUTE']._serialized_start=3894
  _globals['_MUPINTERWORKSEGMENTDISCOVERYROUTE']._serialized_end=3979
  _globals['_MUPDIRECTSEGMENTDISCOVERYROUTE']._serialized_start=3981
  _globals['_MUPDIRECTSEGMENTDISCOVERYROUTE']._serialized_end=4064
  _globals['_MUPTYPE1SESSIONTRANSFORMEDROUTE']._serialized_start=4067
  _globals['_MUPTYPE1SESSIONTRANSFORMEDROUTE']._serialized_end=4318
  _globals['_MUPTYPE2SESSIONTRANSFORMEDROUTE']._serialized_start=4321
  _globals['_MUPTYPE2SESSIONTRANSFORMEDROUTE']._serialized_end=4461
  _globals['_MPREACHNLRIATTRIBUTE']._serialized_start=4463
  _globals['_MPREACHNLRIATTRIBUTE']._serialized_end=4572
  _globals['_MPUNREACHNLRIATTRIBUTE']._serialized_start=4574
  _globals['_MPUNREACHNLRIATTRIBUTE']._serialized_end=4666
  _globals['_TWOOCTETASSPECIFICEXTENDED']._serialized_start=4668
  _globals['_TWOOCTETASSPECIFICEXTENDED']._serialized_end=4771
  _globals['_IPV4ADDRESSSPECIFICEXTENDED']._serialized_start=4773
  _globals['_IPV4ADDRESSSPECIFICEXTENDED']._serialized_end=4881
  _globals['_FOUROCTETASSPECIFICEXTENDED']._serialized_start=4883
  _globals['_FOUROCTETASSPECIFICEXTENDED']._serialized_end=4987
  _globals['_LINKBANDWIDTHEXTENDED']._serialized_start=4989
  _globals['_LINKBANDWIDTHEXTENDED']._serialized_end=5044
  _globals['_VALIDATIONEXTENDED']._serialized_start=5046
  _globals['_VALIDATIONEXTENDED']._serialized_end=5081
  _globals['_COLOREXTENDED']._serialized_start=5083
  _globals['_COLOREXTENDED']._serialized_end=5113
  _globals['_ENCAPEXTENDED']._serialized_start=5115
  _globals['_ENCAPEXTENDED']._serialized_end=5151
  _globals['_DEFAULTGATEWAYEXTENDED']._serialized_start=5153
  _globals['_DEFAULTGATEWAYEXTENDED']._serialized_end=5177
  _globals['_OPAQUEEXTENDED']._serialized_start=5179
  _globals['_OPAQUEEXTENDED']._serialized_end=5233
  _globals['_ESILABELEXTENDED']._serialized_start=5235
  _globals['_ESILABELEXTENDED']._serialized_end=5294
  _globals['_ESIMPORTROUTETARGET']._serialized_start=5296
  _globals['_ESIMPORTROUTETARGET']._serialized_end=5336
  _globals['_MACMOBILITYEXTENDED']._serialized_start=5338
  _globals['_MACMOBILITYEXTENDED']._serialized_end=5400
  _globals['_ROUTERMACEXTENDED']._serialized_start=5402
  _globals['_ROUTERMACEXTENDED']._serialized_end=5434
  _globals['_TRAFFICRATEEXTENDED']._serialized_start=5436
  _globals['_TRAFFICRATEEXTENDED']._serialized_end=5484
  _globals['_TRAFFICACTIONEXTENDED']._serialized_start=5486
  _globals['_TRAFFICACTIONEXTENDED']._serialized_end=5543
  _globals['_REDIRECTTWOOCTETASSPECIFICEXTENDED']._serialized_start=5545
  _globals['_REDIRECTTWOOCTETASSPECIFICEXTENDED']._serialized_end=5615
  _globals['_REDIRECTIPV4ADDRESSSPECIFICEXTENDED']._serialized_start=5617
  _globals['_REDIRECTIPV4ADDRESSSPECIFICEXTENDED']._serialized_end=5692
  _globals['_REDIRECTFOUROCTETASSPECIFICEXTENDED']._serialized_start=5694
  _globals['_REDIRECTFOUROCTETASSPECIFICEXTENDED']._serialized_end=5765
  _globals['_TRAFFICREMARKEXTENDED']._serialized_start=5767
  _globals['_TRAFFICREMARKEXTENDED']._serialized_end=5804
  _globals['_MUPEXTENDED']._serialized_start=5806
  _globals['_MUPEXTENDED']._serialized_end=5879
  _globals['_VPLSEXTENDED']._serialized_start=5881
  _globals['_VPLSEXTENDED']._serialized_end=5931
  _globals['_UNKNOWNEXTENDED']._serialized_start=5933
  _globals['_UNKNOWNEXTENDED']._serialized_end=5979
  _globals['_EXTENDEDCOMMUNITIESATTRIBUTE']._serialized_start=5981
  _globals['_EXTENDEDCOMMUNITIESATTRIBUTE']._serialized_end=6054
  _globals['_AS4PATHATTRIBUTE']._serialized_start=6056
  _globals['_AS4PATHATTRIBUTE']._serialized_end=6110
  _globals['_AS4AGGREGATORATTRIBUTE']._serialized_start=6112
  _globals['_AS4AGGREGATORATTRIBUTE']._serialized_end=6166
  _globals['_PMSITUNNELATTRIBUTE']._serialized_start=6168
  _globals['_PMSITUNNELATTRIBUTE']._serialized_end=6245
  _globals['_TUNNELENCAPSUBTLVENCAPSULATION']._serialized_start=6247
  _globals['_TUNNELENCAPSUBTLVENCAPSULATION']._serialized_end=6308
  _globals['_TUNNELENCAPSUBTLVPROTOCOL']._serialized_start=6310
  _globals['_TUNNELENCAPSUBTLVPROTOCOL']._serialized_end=6355
  _globals['_TUNNELENCAPSUBTLVCOLOR']._serialized_start=6357
  _globals['_TUNNELENCAPSUBTLVCOLOR']._serialized_end=6396
  _globals['_TUNNELENCAPSUBTLVSRPREFERENCE']._serialized_start=6398
  _globals['_TUNNELENCAPSUBTLVSRPREFERENCE']._serialized_end=6464
  _globals['_TUNNELENCAPSUBTLVSRCANDIDATEPATHNAME']._serialized_start=6466
  _globals['_TUNNELENCAPSUBTLVSRCANDIDATEPATHNAME']._serialized_end=6533
  _globals['_TUNNELENCAPSUBTLVSRPRIORITY']._serialized_start=6535
  _globals['_TUNNELENCAPSUBTLVSRPRIORITY']._serialized_end=6582
  _globals['_TUNNELENCAPSUBTLVSRBINDINGSID']._serialized_start=6584
  _globals['_TUNNELENCAPSUBTLVSRBINDINGSID']._serialized_end=6651
  _globals['_SRBINDINGSID']._serialized_start=6653
  _globals['_SRBINDINGSID']._serialized_end=6712
  _globals['_SRV6ENDPOINTBEHAVIOR']._serialized_start=6715
  _globals['_SRV6ENDPOINTBEHAVIOR']._serialized_end=6848
  _globals['_SRV6BINDINGSID']._serialized_start=6851
  _globals['_SRV6BINDINGSID']._serialized_end=6994
  _globals['_TUNNELENCAPSUBTLVSRENLP']._serialized_start=6996
  _globals['_TUNNELENCAPSUBTLVSRENLP']._serialized_end=7067
  _globals['_SRWEIGHT']._serialized_start=7069
  _globals['_SRWEIGHT']._serialized_end=7110
  _globals['_SEGMENTFLAGS']._serialized_start=7112
  _globals['_SEGMENTFLAGS']._serialized_end=7190
  _globals['_SEGMENTTYPEA']._serialized_start=7192
  _globals['_SEGMENTTYPEA']._serialized_end=7257
  _globals['_SEGMENTTYPEB']._serialized_start=7260
  _globals['_SEGMENTTYPEB']._serialized_end=7389
  _globals['_TUNNELENCAPSUBTLVSRSEGMENTLIST']._serialized_start=7391
  _globals['_TUNNELENCAPSUBTLVSRSEGMENTLIST']._serialized_end=7496
  _globals['_TUNNELENCAPSUBTLVEGRESSENDPOINT']._serialized_start=7498
  _globals['_TUNNELENCAPSUBTLVEGRESSENDPOINT']._serialized_end=7548
  _globals['_TUNNELENCAPSUBTLVUDPDESTPORT']._serialized_start=7550
  _globals['_TUNNELENCAPSUBTLVUDPDESTPORT']._serialized_end=7594
  _globals['_TUNNELENCAPSUBTLVUNKNOWN']._serialized_start=7596
  _globals['_TUNNELENCAPSUBTLVUNKNOWN']._serialized_end=7651
  _globals['_TUNNELENCAPTLV']._serialized_start=7653
  _globals['_TUNNELENCAPTLV']._serialized_end=7719
  _globals['_TUNNELENCAPATTRIBUTE']._serialized_start=7721
  _globals['_TUNNELENCAPATTRIBUTE']._serialized_end=7780
  _globals['_IPV6ADDRESSSPECIFICEXTENDED']._serialized_start=7782
  _globals['_IPV6ADDRESSSPECIFICEXTENDED']._serialized_end=7890
  _globals['_REDIRECTIPV6ADDRESSSPECIFICEXTENDED']._serialized_start=7892
  _globals['_REDIRECTIPV6ADDRESSSPECIFICEXTENDED']._serialized_end=7967
  _globals['_IP6EXTENDEDCOMMUNITIESATTRIBUTE']._serialized_start=7969
  _globals['_IP6EXTENDEDCOMMUNITIESATTRIBUTE']._serialized_end=8045
  _globals['_AIGPTLVIGPMETRIC']._serialized_start=8047
  _globals['_AIGPTLVIGPMETRIC']._serialized_end=8081
  _globals['_AIGPTLVUNKNOWN']._serialized_start=8083
  _globals['_AIGPTLVUNKNOWN']._serialized_end=8128
  _globals['_AIGPATTRIBUTE']._serialized_start=8130
  _globals['_AIGPATTRIBUTE']._serialized_end=8181
  _globals['_LARGECOMMUNITY']._serialized_start=8183
  _globals['_LARGECOMMUNITY']._serialized_end=8263
  _globals['_LARGECOMMUNITIESATTRIBUTE']._serialized_start=8265
  _globals['_LARGECOMMUNITIESATTRIBUTE']._serialized_end=8336
  _globals['_LSNODEFLAGS']._serialized_start=8338
  _globals['_LSNODEFLAGS']._serialized_end=8446
  _globals['_LSIGPFLAGS']._serialized_start=8448
  _globals['_LSIGPFLAGS']._serialized_end=8541
  _globals['_LSSRRANGE']._serialized_start=8543
  _globals['_LSSRRANGE']._serialized_end=8582
  _globals['_LSSRCAPABILITIES']._serialized_start=8584
  _globals['_LSSRCAPABILITIES']._serialized_end=8684
  _globals['_LSSRLOCALBLOCK']._serialized_start=8686
  _globals['_LSSRLOCALBLOCK']._serialized_end=8736
  _globals['_LSATTRIBUTENODE']._serialized_start=8739
  _globals['_LSATTRIBUTENODE']._serialized_end=9013
  _globals['_LSATTRIBUTELINK']._serialized_start=9016
  _globals['_LSATTRIBUTELINK']._serialized_end=9359
  _globals['_LSATTRIBUTEPREFIX']._serialized_start=9361
  _globals['_LSATTRIBUTEPREFIX']._serialized_end=9457
  _globals['_LSBGPPEERSEGMENTSIDFLAGS']._serialized_start=9459
  _globals['_LSBGPPEERSEGMENTSIDFLAGS']._serialized_end=9551
  _globals['_LSBGPPEERSEGMENTSID']._serialized_start=9553
  _globals['_LSBGPPEERSEGMENTSID']._serialized_end=9651
  _globals['_LSATTRIBUTEBGPPEERSEGMENT']._serialized_start=9654
  _globals['_LSATTRIBUTEBGPPEERSEGMENT']._serialized_end=9850
  _globals['_LSATTRIBUTE']._serialized_start=9853
  _globals['_LSATTRIBUTE']._serialized_end=10044
  _globals['_UNKNOWNATTRIBUTE']._serialized_start=10046
  _globals['_UNKNOWNATTRIBUTE']._serialized_end=10108
  _globals['_SRV6STRUCTURESUBSUBTLV']._serialized_start=10111
  _globals['_SRV6STRUCTURESUBSUBTLV']._serialized_end=10304
  _globals['_SRV6SIDFLAGS']._serialized_start=10306
  _globals['_SRV6SIDFLAGS']._serialized_end=10336
  _globals['_SRV6TLV']._serialized_start=10338
  _globals['_SRV6TLV']._serialized_end=10382
  _globals['_SRV6INFORMATIONSUBTLV']._serialized_start=10385
  _globals['_SRV6INFORMATIONSUBTLV']._serialized_end=10619
  _globals['_SRV6INFORMATIONSUBTLV_SUBSUBTLVSENTRY']._serialized_start=10554
  _globals['_SRV6INFORMATIONSUBTLV_SUBSUBTLVSENTRY']._serialized_end=10619
  _globals['_SRV6L3SERVICETLV']._serialized_start=10622
  _globals['_SRV6L3SERVICETLV']._serialized_end=10760
  _globals['_SRV6L3SERVICETLV_SUBTLVSENTRY']._serialized_start=10698
  _globals['_SRV6L3SERVICETLV_SUBTLVSENTRY']._serialized_end=10760
  _globals['_SRV6L2SERVICETLV']._serialized_start=10763
  _globals['_SRV6L2SERVICETLV']._serialized_end=10901
  _globals['_SRV6L2SERVICETLV_SUBTLVSENTRY']._serialized_start=10698
  _globals['_SRV6L2SERVICETLV_SUBTLVSENTRY']._serialized_end=10760
  _globals['_PREFIXSID']._serialized_start=10903
  _globals['_PREFIXSID']._serialized_end=10950
# @@protoc_insertion_point(module_scope)
