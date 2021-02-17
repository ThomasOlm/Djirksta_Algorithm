# Djirksta_Algorithm
This is a project to make a graphical display of Djirksta's Algorithm. Implemented with Pygame. 

Djirstka 

My implementation of the famous shortest open first path algortihm. Each link is examined for its distance from A and if this link is found to be smaller the list is updated. Process continues untill every node has been visted. Returns the shortest path from Z to A.

Pygame

The pygame section of the program has three pieces: one: store a dictionary of lines and circles, two: draw these dictionaries, three: pass two dictionaries to the Algorithm file.

Each time the mouse is clicked, the position is used to create a circle. The circle is an class and stores the location and identity of each circle.
Then when two or more circles are created, a line is drawn between them. This line is also stored as an object in a dictionary. This repeats until the user clicks on the end point.
This whole process can occur twice. 
When the user is finished, they click the calculate route button and the dictionaries are passed to the algorithm.
Algorthim returns best route, and that route is changed to green.
