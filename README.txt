Parallel Breadth First Search on Large Graphs
Prateek Kumar Singh

The folder contains 6 files:

 Code Development
- mapper.py: For each node in the graph, mapper.py emits nodeID, distance from source, 
including distance from itself.- reducer.py: Takes input from mapper.py, then select shortest Path for each node.
- stop.py: Contains the Stopping Condition of the algorithm.
- run.sh: Shell file to execute the program.Performance AnalysisReport.pdfalong with README making a total of 6 files.

Note that the program takes input a as .txt file named graph.txt and is initialised 
using another .txt file named distance.txt. Their description is given below:

- graph.txt: Each line contains the Node ID of the node in a graph along with it's
Adjacency list which gives the outlinks from the current node. Each line in the file
should end with a New line(\n) character and NOT a Return carriage(\r).
- distance.txt: Each line contains the Node ID of the node in a graph along with it's
Distance from the source node. The distance 9999 represents infinity. Each line in the
File should end with a New line(\n) character and NOT a Return carriage(\r).

To run the code, scp all the files for task 1 to jumphost and then hadoop.
Upload the input file i.e. graph.txt to HDFS using the command 
"hadoop fs -copyFromLocal graph.txt /" on the EMR Master Node. Now, change mode for 
the run.sh using "chmod +x run.sh". Then execute ./run.sh

After the stopping condition is met and all the iterations are done, the output is 
Saved in the distance.txt file.