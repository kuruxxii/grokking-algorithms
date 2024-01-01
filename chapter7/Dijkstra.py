# float('inf') is used for setting a variable with an infinitely large value
infinity = float("inf")

graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

"""
costs
"""
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

"""
parents
"""
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

"""
processed
"""
processed = []


def find_lowest_cost_node(costs):
    lowest_cost = infinity
    lowest_cost_node = None
    for node in costs:
        if costs[node] < lowest_cost and node not in processed:
            lowest_cost = costs[node]
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for neighbor in neighbors:
        neighbor_new_cost = cost + neighbors[neighbor]
        if neighbor_new_cost < costs[neighbor]:
            costs[neighbor] = neighbor_new_cost
            parents[neighbor] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
print(f'The path is {parents}')
