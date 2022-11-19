# Best_Vertex_Cover
The two Python programs use the Iterative Deepening and Simple Hill Climbing (with "random" restarts) algorithms to find solutions for the Best Vertex Cover Problem.  
These programs utilize the concept of state spaces as models on which the algorithms work.  
The Best Vertex Cover problem is as follows:
- Input: An undirected graph G, in which each vertex is marked by a positive cost, and a total budget T.
- Goal: A set of vertices S such that (a) every edge in G has at least one end in S and (b) the total cost of the vertices in S is at most T.

#### How to run programs:
- Make sure Python3 is installed.
- Run the program on the terminal using "python3 <program_name>.py".
- Make sure the text file where the program is getting its input from is within the same directory the program is running in.

### Below is the format in which the input file must be in, in order for the program to run correctly:
- Line 1: The budget (a positive integer) and flags: "V" for verbose output or "C" for compact output. For the hill-climbing program, the number of random restarts to run.
- Each vertex. Name (you may assume that this is a single alphabetic character) and cost (a positive integer), 1 per line.
Blank line
- Each edge: the names of the two ends. 1 per line.

_You can oepn the "test.txt" file to see how the input format should look like._  
_Note: Make sure there is no endline (\n) after the last line of the input file to avoid program error._
