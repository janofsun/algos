'''
In order to curb the spread of the novel COVID-19 virus, the citizens of Hackerland need to be vaccinated on priority.
There are center_nodes vaccination centers in Hackerland, where each center has a status denoted by statusfil:
• Centers with a shortage of vaccines have status 1.
• Those with sufficient vaccines have status 2.
• Those with a surplus have status 3.

Vaccines can be transferred from centers with a surplus to centers with a deficit. There is a network of bidirectional roads between centers where the ith road is between cities center_ from[il and center_to/ll. Each road takes 1 unit of time to traverse. Find the minimum time in which all deficient centers can receive a supply of vaccines from some surplus center.
Note:
• Surplus centers have an inexhaustible supply of vaccines.
• Multiple surplus centers can ship their surplus simultaneously.
• Multiple deliveries from a single surplus center can leave simultaneously.
• Vaccines are only shipped from centers with status 3 to centers with status 1. Status 2 centers do nothing.

Example
There are center_nodes = 6 centers, and center_edges = 6 roads.
The network of roads is described by center_from = [1, 2, 3, 4, 5, 6] and center_to = [2, 3, 4, 5, 6, 1].
The statuses of centers are status = [3, 2, 1, 2, 1, 2].
'''

# like lc rotten oranges
def findMinimumTime(centre_nodes, centre_from, centre_to, status):