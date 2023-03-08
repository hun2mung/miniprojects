def solution(my_str, n):
    answer = []
    a = str
    cnt=1
    for i in my_str:
        a = a+i
        cnt+=1
        if cnt % n == 0:
            answer.append(a)
            a=str

    return answer
if __name__ == '__main__':
    solution([7, 77, 17])
