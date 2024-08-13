'''
You are given an array A consisting of N numbers. In one move you can delete either the
first two, the last two, or the first and last elements of A. No move can be performed if the
length of A is smaller than 2. The result of each move is the sum of the deleted elements.

Write a function:
class Solution { public int solution(int[] A); }

that, given an array A of N integers, returns the maximum number of moves that can be
performed on A, such that all performed moves have the same result.
Examples:

Given A = [3, 1, 5, 3, 3, 4, 2], the function should return 3. The first move should delete
two last elements (4 and 2 with sum = 6), then A = [3, 1, 5, 3, 3]. The second move may
delete first and last elements (3 and 3 with sum = 6), then A = [1, 5, 3). The third move
should delete first two elements (1 and 5 with sum = 6), then A = [3).
Given A = [4, 1, 4, 3, 3, 2, 5, 2], the function should return 4. It is possible to delete the first
and last elements four times, as each such pair of elements sums up to 6.
Given A = [1, 9, 1, 1, 1, 1,1,1, 8, 1], the function should return 1. There is no way to
perform move that results with the same sum more than once.
Given A = [1, 9, 8, 9, 5, 1, 2], the function should return 3. The first move should delete the
first two elements, then the second and third moves should delete first and last elements
twice.
Given A = [1, 1, 2, 3, 1, 2, 2, 1, 1, 2], the function should return 4.
'''
'''
Python3 || O(n^2) TC and O(n^2) SC || Top down recursion with memoization

Depending on the constraints this may/may not work.
seems like it can be solved with DP. Could potentially have a better greedy algorithm, but cant think of anything.
'''
def solution(A):

    def dfs(l,r,target,cache):
        if r-l+1 < 2:
            return 0
        key = (l,r)
        if key in cache:
            return cache[key]
        
        maximum = 0
        if A[l] + A[l+1] == target:
            maximum = max(maximum,1+dfs(l+2,r,target,cache))
        if A[l] + A[r] == target:
            maximum = max(maximum,1+dfs(l+1,r-1,target,cache))
        if A[r] + A[r-1] == target:
            maximum = max(maximum,1+dfs(l,r-2,target,cache))

        cache[key] = maximum
        return maximum
        
    
    if len(A) < 2:
        return 0
    
    l = 0
    r = len(A)-1
    op1 = dfs(l+2,r,A[l]+A[l+1],{})
    op2 = dfs(l+1,r-1,A[l]+A[r],{})
    op3 = dfs(l,r-2,A[r]+A[r-1],{})

    return max(op1,op2,op3)+1

A = [3, 1, 5, 3, 3, 4, 2]
print(solution(A)) #3

A1 = [4, 1, 4, 3, 3, 2, 5, 2]
print(solution(A1)) #4

A2 = [1, 9, 1, 1, 1, 1,1,1, 8, 1]
print(solution(A2)) #1

A3 = [1, 9, 8, 9, 5, 1, 2]
print(solution(A3)) #3

A4 = [1, 1, 2, 3, 1, 2, 2, 1, 1, 2]
print(solution(A4))  # 4 

A5 = [1]