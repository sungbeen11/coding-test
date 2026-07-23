def solution(n, info):
    result = [0,0,0,0,0,0,0,0,0,0,0]
    result_mi = 0
    def recur(i,x,answer):
        nonlocal result_mi,result
        if i == 10:
            answer[10] = x
            a = 0
            b = 0
            for i in range(10):
                if answer[i] > info[i]:
                    a += 10 - i
                if info[i] >= answer[i] and info[i] != 0:
                    b += 10 - i
            diff = a - b
            if diff > 0 and (
                diff > result_mi or
                (diff == result_mi and answer[::-1] > result[::-1])):
                result_mi = diff
                result = answer[:]
            return 0
        if x > info[i]:
            answer[i] = info[i] + 1
            x -= answer[i]
            recur(i+1,x,answer)
            x += answer[i]
            answer[i] = 0
        recur(i+1,x,answer)  
    recur(0,n,result)
    if result_mi == 0:
        return [-1]
    return result