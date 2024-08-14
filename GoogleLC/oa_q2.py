def solution(A):
    # 从全0数组开始，所以初始变化必须从0增加到A[0]
    moves = A[0]
    
    # 遍历数组，计算从一个元素到下一个元素所需的增加操作数
    for i in range(1, len(A)):
        if A[i] > A[i - 1]:
            # 只有当当前元素大于前一个元素时，我们才需要进行操作
            moves += A[i] - A[i - 1]
    
    return moves

# 测试案例
print(solution([2, 3]))        # 应返回 3
print(solution([2, 2, 0, 0, 1]))  # 应返回 2
print(solution([5, 4, 2, 4, 1]))  # 应返回 5