def solution(digits):
    max1 = max2 = max3 = -1  # 初始化最大一位数、两位数和三位数为无效值
    
    for digit in digits:
        # 更新最大三位数：尝试将当前数字追加到最大两位数后面形成的新三位数
        if max2 != -1:  # 确保有有效的两位数
            new_max3 = int(f"{max2}{digit}")
            max3 = max(max3, new_max3)
        
        # 更新最大两位数：尝试将当前数字追加到最大一位数后面形成的新两位数
        if max1 != -1:  # 确保有有效的一位数
            new_max2 = int(f"{max1}{digit}")
            max2 = max(max2, new_max2)
        
        # 更新最大一位数
        max1 = max(max1, digit)
    
    return max(max1, max2, max3)

# 测试案例
print(solution([7, 2, 3, 3, 4, 9])) 
print(solution([0, 0, 5, 7]))