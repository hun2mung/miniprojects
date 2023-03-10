def solution(numbers):
    answer = 0
    sum1 = []
    sum2 = []
    for i in numbers:
        if  i >= 0:
            sum1.append(i)
    sum1 = sorted(sum1)
    
    for i in numbers:
        if  i < 0:
            sum2.append(i)
    sum2 = sorted(sum2)

    mul1 =0
    mul2=0
    if len(sum1) >= 2:
        mul1 = sum1[-1]*sum1[-2]
    if len(sum2) >= 2:
        mul2 = sum2[-1]*sum2[-2]
    
    answer = max(mul1,mul2)
    
    return print(answer)
if __name__ == '__main__':
    solution([0, -31, 24, 10, 1, 9])
