import math

def Djirksta_Alg(dict_of_nodes, shortest_distance_from_A):


    node_links = dict_of_nodes

    previous_vertex = {}

    unvisted = []

    for keys in shortest_distance_from_A.keys():
        unvisted.append(keys)


    visited = []

    # print(find_smallest_dist(shortest_distance_from_A, visited))

    while unvisted:

        # visit the vertex with the smallest known distance from A
        target_node = find_smallest_dist(shortest_distance_from_A, visited)

        # for current vertex examine the distance to unvisted neighbor vertexes
        paths_from_node = select_paths(target_node, visited, node_links)
        # calculate the distance from each neighbor vertex from start vertex
        # if calculated distance is less than known distance update shortest distance list

        check_routes(paths_from_node, shortest_distance_from_A, target_node, visited, previous_vertex)
        # update the previous vertex for each of the updated distances

        # add current vertex to visted listed
        visited.append(target_node)
        unvisted.pop(unvisted.index(target_node))

        #print("Dict ", shortest_distance_from_A)
        #print(previous_vertex)

        #print out the shortest route

    return shortest_route(shortest_distance_from_A, previous_vertex)

def find_smallest_dist(shortest_distance_dict, visted_nodes):

    ## cycle through shortest_distance_dictionary to find the node with the current shortest distance and unvisted

    largest_distance = math.inf
    largest_node = ""
    shortest_distance_dict_copy = shortest_distance_dict.copy()

    ## remove all visted nodes from consideration
    for node in visted_nodes:
        if node in shortest_distance_dict_copy.keys():
            shortest_distance_dict_copy.pop(node)

    ## cycle through remaining nodes to find shortest distance, this will have problem with ties

    for node in shortest_distance_dict_copy:

        if shortest_distance_dict_copy[node] < largest_distance:
            largest_distance = shortest_distance_dict_copy[node]
            largest_node = node

    return largest_node

def select_paths(node, visited, node_links):

    paths_from_node = {}

    for link in node_links:
        if node in link and node not in visited:
            paths_from_node.update({link : node_links.get(link)})

    return paths_from_node

def check_routes(paths_from_node, shortest_distance_from_A, target_node, visited, previous_vert):

    # calculate the distance from each neighbor vertex from start vertex
    # if calculated distance is less than known distance update shortest distance list

    distance_from_start = 0


    # strip previously visited nodes from paths

    for node in paths_from_node:

        node_letter = node.strip(target_node)

        # update previous node dictionary

        if node_letter not in visited:
            distance_from_start = paths_from_node.get(node) + shortest_distance_from_A.get(target_node)


            if distance_from_start <= shortest_distance_from_A.get(node_letter):
                shortest_distance_from_A.update({node_letter: distance_from_start})
                previous_vert.update({node_letter:node.strip(node_letter)})

def shortest_route(dict_of_data, path_dict):

    # return a list ordered with the best part
    copy = dict_of_data.copy()
    copy = dict(sorted(copy.items(), key=lambda item: item[1]))

    list_of_best_path = []

    start_letter = ""

    #Two methods exist here, one to print out to console, one to return a list

    for letter in copy:
        if dict_of_data.get(letter) == 0:
            #print( letter, "is the start!")
            start_letter = letter
        else:
            #print("shortest path from", letter, "is: ")
            #recursive?
            if letter == "Z":
                shortest_route_2_list(letter,start_letter,path_dict, list_of_best_path)
            #shortest_route_2(letter, start_letter, path_dict)
    return list_of_best_path

def shortest_route_2_list(letter,start_letter, previous_vertex,list_of_best_path):

    if letter == start_letter:
        return
    else:
        list_of_best_path.append(previous_vertex.get(letter) + letter)
        shortest_route_2_list(previous_vertex.get(letter), start_letter, previous_vertex, list_of_best_path)



def shortest_route_2(letter, start_letter, previous_vertex):

    if letter == start_letter:
        print("finished!")
    else:
        print(letter, "->", previous_vertex.get(letter))
        shortest_route_2(previous_vertex.get(letter), start_letter, previous_vertex)
