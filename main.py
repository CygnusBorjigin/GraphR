from node import Node
from edge import Edge
from graph import Graph

import numpy as np

test_node = [Node(i, np.random.rand()) for i in range(10)]
test_edge = [Edge(np.random.randint(1, 11), np.random.randint(1, 11), np.random.random(), np.random.random()) for i in range(100) if np.random.rand() > 0.3]
test_graph = Graph(test_node, test_edge)

print(test_graph.graph_info(node_style="Full"))

test_graph.new_activity([(1, 2), (2, 2), (3, 4)])

print(test_graph.graph_info(node_style="Full"))