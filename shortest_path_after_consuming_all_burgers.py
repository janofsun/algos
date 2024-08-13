'''
Given a NxN grid. Given a character 'S' (start point), character 'E' (end point), a character 'B' (Burger), and a character 'O' (Empty road). There is a person who wants to start from the starting point and wants to reach the ending point by consuming all the burgers. You need to return the minimum distance the person has to cover from start to end point by eating all the burgers. The person can travel either top, down, right, or left. Diagonal movement is not allowed. Also, the person can only reach the end point after consuming all the burgers.

The test case is as follows:

BOOB
OSOO
OOOE
BOOO

Expected Answer: 11

The explanation of this test case is as follows:-
Person initially starts at 'S' (1,1) (Initial 0 units).
Then goes to (3,0) to eat the first burger. (now 0+3=3units).
Then goes to (0,0) to eat the second burger (now 0+3+3=6units).
Then goes to (0,3) to eat third burger (so now 0+3+3+3=9units).
Then finally after eating all the burgers goes to (2,3) 'E' endpoint (so now 0+3+3+3+2=11units).
So final answer is 11units. This is the shortest path.
'''