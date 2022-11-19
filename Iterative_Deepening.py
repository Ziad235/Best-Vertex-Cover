import random
from locale import currency
############################################################################################################################################################################################################################################################
Text_File = open('data.txt', 'r')

First_Line = Text_File.readline().strip().split(' ')
Total_Budget = int(First_Line[0])
V_or_C = First_Line[1]

Input_Vertex_Edge = Text_File.read().split('\n\n')

Vertices = Input_Vertex_Edge[0].split('\n')
Edges = Input_Vertex_Edge[1].split('\n')

Total_Edges = []

for edge in Edges:
    u_input = edge.split(' ')
    Total_Edges.append(u_input)

Vertex_Dict = {}
############################################################################################################################################################################################################################################################
class Vertex:
    def __init__(self, atom, cost):
        self.atom = atom 
        self.cost = cost
        self.edges = []

############################################################################################################################################################################################################################################################
for vertex in Vertices:
    vertex_cost = vertex.split(' ')
    new_vertex = Vertex(vertex_cost[0], int(vertex_cost[1]))
    Vertex_Dict[vertex_cost[0]] = new_vertex

for edge in Edges:
    tmp_edges = edge.split(' ')
    Vertex_Dict[tmp_edges[0]].edges.append(Vertex_Dict[tmp_edges[1]])
    Vertex_Dict[tmp_edges[1]].edges.append(Vertex_Dict[tmp_edges[0]])
############################################################################################################################################################################################################################################################
def Cost_Function(Vertex_Set):
    Cost = 0

    for vertex in Vertex_Set:
        Cost = Cost + Vertex_Dict[vertex].cost

    return Cost
################################################################################################
def Unused_Edges_Count(input_set):
    unvisited_edges = Total_Edges.copy()
    visited_edges = []

    for edge in input_set:
        for v_edge in unvisited_edges:
            if edge in v_edge:
                visited_edges.append(v_edge)
    
    for edge in visited_edges:
        if edge in unvisited_edges:
            unvisited_edges.remove(edge)
    
    return unvisited_edges
################################################################################################
def Valid_Solution(Vertex_Set):
    Cost = Cost_Function(Vertex_Set)
    Unvisited_Edges = Unused_Edges_Count(Vertex_Set)

    if Cost < Total_Budget and Unvisited_Edges == []:
        return True
    else:
        return False
################################################################################################
def DFS(State, Depth):
    if Valid_Solution(State):
        print("Found a solution at ", State)
        return "stop"
    if Depth == 0:
        return "temp"
    for vertex in Vertex_Dict.keys():
        if State == [] or (ord(vertex) > ord(State[-1]) and Total_Budget >= Cost_Function(State)+Vertex_Dict[vertex].cost and Unused_Edges_Count(State+[vertex]) != Unused_Edges_Count(State)):
            State.append(vertex)

            if V_or_C == 'V':
                print(State, " Cost = ", Cost_Function(State))
            Halt = DFS(State, Depth-1)
            if Halt == "stop":
                return "stop"
            State.pop()
################################################################################################
def IDS():
    State = []
    Depth = 0
    Incomplete = True

    while(Incomplete):
        Depth = Depth + 1
        if V_or_C == "V":
            print("\n Depth = ", Depth)
        Halt = DFS(State, Depth)
        if Halt == "stop":
            break
        if Depth == 5:
            Incomplete = False

IDS()