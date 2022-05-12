from node import Node
from edge import Edge

class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges

    def graph_info(self, node_style="None", edge_style="None", output_style="None"):
        if node_style == "None":
            all_node = [each_node.value for each_node in self.nodes]
        elif node_style == "Full":
            all_node = [(each_node.value, each_node.rho, each_node.activity, each_node.active) for each_node in self.nodes]
        
        if edge_style == "None":
            all_edge = [(each_edge.node1, each_edge.node2) for each_edge in self.edges]
        if edge_style == "Full":
            all_edge = [(each_edge.node1, each_edge.node2, each_edge.weight, each_edge.capacity) for each_edge in self.edges]

        return (all_node, all_edge)
        
