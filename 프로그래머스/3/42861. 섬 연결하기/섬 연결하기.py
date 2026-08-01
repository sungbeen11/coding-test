def solution(n, costs):
    p_list = [i for i in range(n)]
    answer = 0
    costs = sorted(costs,key = lambda x : x[2] )
    
    def root(i):
        if p_list[i] != i:
            p_list[i] = root(p_list[i])
        return p_list[i]
    
    for x,y,cost in costs:
        if root(x) == root(y):
            continue
        p_list[root(y)] = p_list[x]
        answer += cost
    return answer

