from node import Node
from edge import Edge

class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
        self.first_neighborhood = {}
        self.__build_first_neighbor()

    def __build_first_neighbor(self):
        # initialize the hash
        for each_node in self.nodes:
            self.first_neighborhood[str(each_node.value)] = []
        
        # populate the hash
        for each_edge in self.edges:
            if each_edge.node2 not in self.first_neighborhood[str(each_edge.node1)]:
                self.first_neighborhood[str(each_edge.node1)].append(each_edge.node2)

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
                "nodes" : {},
                "edges" : {}
            }
            # node info 
            if node_style == "Full":
                for each_node in all_node:               
                    output["nodes"][str(each_node[0])] = {
                        "threshold" : each_node[1],
                        "activity" : each_node[2],
                        "active" : each_node[3]
                    }
            elif node_style == "None":
                output["nodes"] = all_node

            # formate edge info
            if edge_style == "None":
                for each_edge_index in range(len(self.edges)):
                    output["edges"][str(each_edge_index)] = {
                        "node1" : self.edges[each_edge_index].node1,
                        "node2" : self.edges[each_edge_index].node2
                    }
            elif edge_style == "Full":
                for each_edge_index in range(len(all_edge)):
                    output["edges"][str(each_edge_index)] = {
                        "node1" : all_edge[each_edge_index][0],
                        "node2" : all_edge[each_edge_index][1],
                        "weight" : all_edge[each_edge_index][2],
                        "capacity" : all_edge[each_edge_index][3]
                    }


        return output
        
    def new_activity(self, targets):
        for each_target in targets:
            for each_node in self.nodes:
                if each_node.value == each_target[0]:
                    each_node.receive(each_target[1])

    def static(self):
        for each_node in self.nodes:
            if each_node.active:
                return False
        return True
