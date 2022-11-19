import random 
############################################################################################################################################################################################################################################################
class Vertex:
    def __init__(self, atom, cost):
        self.atom = atom 
        self.cost = cost
        self.edges = []

Text_File = open('data.txt', 'r')

First_Line = Text_File.readline().strip().split(' ')
Total_Budget = int(First_Line[0])
V_or_C = First_Line[1]
Restarts = int(First_Line[2])


Input_Vertex_Edge = Text_File.read().split('\n\n')

Vertices = Input_Vertex_Edge[0].split('\n')
Edges = Input_Vertex_Edge[1].split('\n')

Total_Edges = []

for edge in Edges:
    input = edge.split(' ')
    Total_Edges.append(input)

Vertex_Dict = {}
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

def Random_Restart():
    Vertex_Set = []
    for vertex in Vertex_Dict.keys():
        if random.choices(range(2)) == [1]:
            Vertex_Set.append(vertex)
    print("Randomly chosen start state: ", Vertex_Set)
    return Vertex_Set
################################################################################################

def Choose_Neighbors(Vertex_Set):
    Min_Cost, Min_Error = Error_Function(Vertex_Set)
    Sucessor_State = []

    if V_or_C == 'V':
        print("Neighbors")

    for vertex in Vertex_Dict.keys():
        OGVertex_Set = Vertex_Set.copy()

        if vertex in Vertex_Set:
            OGVertex_Set.remove(vertex)
            Cost, Error = Error_Function(OGVertex_Set)

            if Min_Error >= Error:
                if Error == Min_Error and Min_Cost > Cost:
                    Min_Cost = Cost
                    Sucessor_State = OGVertex_Set.copy()
                elif Min_Error > Error:
                    Min_Cost = Cost 
                    Min_Error = Error
                    Sucessor_State = OGVertex_Set.copy()
            if V_or_C == 'V':
                print(OGVertex_Set, " Cost = ", Cost, ".Error = ", Error)

        elif vertex not in Vertex_Set:
            OGVertex_Set.append(vertex)
            OGVertex_Set.sort()

            Cost, Error = Error_Function(OGVertex_Set)

            if Min_Error >= Error:
                if Error == Min_Error and Min_Cost > Cost:
                    Min_Cost = Cost
                    Sucessor_State = OGVertex_Set.copy()
                elif Min_Error > Error:
                    Min_Cost = Cost
                    Min_Error = Error
                    Sucessor_State = OGVertex_Set.copy()
            if V_or_C == 'V':
                 print(OGVertex_Set, " Cost = ", Cost, ".Error = ", Error)

    if Sucessor_State == [] and OGVertex_Set != []:
        return 0, Vertex_Set
    else:
        return 1, Sucessor_State
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

def Error_Function(Vertex_Set):
    Total_Cost = 0
    Unvisited_Edges_Cost = 0

    for vertex in Vertex_Set:
        Total_Cost = Total_Cost + Vertex_Dict[vertex].cost

    Unvisited_Edges = Unused_Edges_Count(Vertex_Set)
    for edge in Unvisited_Edges:
        Unvisited_Edges_Cost = Unvisited_Edges_Cost + min(Vertex_Dict[edge[0]].cost, Vertex_Dict[edge[1]].cost)

    Func_Output = max(0, Total_Cost - Total_Budget) + Unvisited_Edges_Cost

    return Total_Cost, Func_Output
################################################################################################

def Valid_Solution(Vertex_Set):
    Cost, Error = Error_Function(Vertex_Set)
    Unvisited_Edges = Unused_Edges_Count(Vertex_Set)

    if Cost < Total_Budget and Unvisited_Edges == []:
        return True
    else:
        return False
################################################################################################

def Hill_Climbing_Algorithm():
    Solution = []

    for restarts in range(Restarts):
        Finish = False
        Solution = Random_Restart()

        Cost, Error = Error_Function(Solution)

        if V_or_C == 'V':
            print("Cost = ", Cost, ". Error = ", Error)

        Done, Solution = Choose_Neighbors(Solution)
        if Done == 0:
            if Valid_Solution(Solution):
                print("\n Solution is ", Solution, "\n")
            else:
                print("\n Search Faild. \n")
            Finish = True

        while not Finish:
            if V_or_C == 'V':
                print("\n Move to ", Solution)

            Done, Solution = Choose_Neighbors(Solution)

            if Done == 0:
                if Valid_Solution(Solution):
                    print("\n Solution is ", Solution, "\n")
                else:
                    print("\n Search Faaild. \n")
                Finish = True
################################################################################################

Hill_Climbing_Algorithm()