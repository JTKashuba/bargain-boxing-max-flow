# Bargain Boxing Max Flow

A software application developed in Python to determine the maximum flow in a flow network using the Ford-Fulkerson algorithm 

## Problem Statement

Suppose we are given a set of boxes, each specified by their height, width, and depth in inches. All three side lengths of every box lie strictly between 1 inch and 36 inches. As you should expect, one box can be placed inside another if the first box can be rotated so that its height, width, and depth are respectively at least one inch smaller smaller than the height, width, and depth of the second box. Boxes can be nested recursively. Call a box visible if it is not inside another box. Write code that will determine the smallest number of visible boxes. (More info and diagrams available in asst6.pdf and bargainBoxing.pdf)


## User Instructions
* Save the ```bargain-boxing-max-flow``` repo locally
* From the command line, navigate to the ```bargain-boxing-max-flow``` directory
* The program uses standard input/output; hence, it receives variable information from a ```.txt``` file provided by the user
* Run the program with a command of the following form ```python3 nestingBoxes_maxFlow.py < file.txt```, where ```file.txt``` is a file with the variables for which you're attempting to determine the max flow
* There are 3 sample files provided: namely ```inSample1.txt```, ```inSample2.txt```, and ```judge3.txt```. The max flow for the samples are ```1```, ```3```, and ```6``` respectively
* If you would like to utilize this program with different variables, follow the format listed in the third paragraph of asst6.pdf when creating your ```.txt``` file
* The program constructs and evaluates a bipartite graph from data received from the input file, determining the smallest number of visible boxes when optimally nesting them inside one another (i.e., max flow)
* There are even more visual aids and comments in the source code in ```nestingBoxes_maxFlow.py``` for future developers ease of use to modify it to their specific needs


## Contact Info
[LinkedIn](https://www.linkedin.com/in/jtkashuba)

kashuba.jt@gmail.com