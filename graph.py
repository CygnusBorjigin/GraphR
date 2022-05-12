from node import Node
from edge import Edge

class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges

    def graph_info(self, node_style="None", edge_style="None", output_style="None"):
        # form the representation
        if node_style == "None":
            all_node = [each_node.value for each_node in self.nodes]
        elif node_style == "Full":
            all_node = [(each_node.value, each_node.rho, each_node.activity, each_node.active) for each_node in self.nodes]
        
        if edge_style == "None":
            all_edge = [(each_edge.node1, each_edge.node2) for each_edge in self.edges]
        if edge_style == "Full":
            all_edge = [(each_edge.node1, each_edge.node2, each_edge.weight, each_edge.capacity) for each_edge in self.edges]

        # format the output
        if output_style == "None":
            return (all_node, all_edge)
        elif output_style == "dict":
            output = {
                "nodes" : all_node,
                "edges" : {}
            }

            for each_edge_index in range(len(self.edges)):
                if edge_style == "None":
                    output["edges"][str(each_edge_index)] = {
                        "node1" : self.edges[each_edge_index].node1,
                        "node2" : self.edges[each_edge_index].node2
                    }
                elif edge_style == "Full":
                    output["edges"][str(each_edge_index)] = {
                        "node1" : self.edges[each_edge_index].node1,
                        "node2" : self.edges[each_edge_index].node2,
                        "weight" : self.edges[each_edge_index].weight,
                        "capacity" : self.edges[each_edge_index].capacity
                    }

        return output
        
