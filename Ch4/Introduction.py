# The Algorithm of finding the shortest path between any vertex and all the other vertex.
# Let's say I wanna get the shortest path from vertex 0 to all other vertices. I have 8 vertices (0:7)
# I make two vertex-indexed arrays: edgeTo() -> the last edge to the vertex.
#                                   distTo() -> the distance from 0 to the vertex.
#                 edgeTo()       distTo()
#           0       null            0
#           1      5 -> 1          1.05     these are random distances.
#           2      0 -> 2          0.26
#           3      7 -> 3          0.97
#           4      0 -> 4          0.38
#           5      4 -> 5          0.73
#           6      3 -> 6          1.49
#           7      2 -> 7          0.60
#
#  Let's say I wanna know the shortest path from 0 to 6.
#  - The last edge is 3 -> 6, the last edge to 3 is 7 -> 3, the last edge
#    to 7 is 2 -> 7, and the last edge to 2 is 0 -> 2, so the path is 0 -> 2 -> 7 -> 3 -> 6.
#  - I use stack to store these last edges, then print them.
