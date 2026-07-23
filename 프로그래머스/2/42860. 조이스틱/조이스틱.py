def solution(name):
    n = len(name)
    front = 0
    back = 0
    answer = 0
    for x in name:
        a = ord(x) - ord('A')
        if a > 13:
            a = 26 - a
        answer += a
    move = n - 1

    for i in range(n):
        next_index = i + 1
        while next_index < n and name[next_index] == 'A':
            next_index += 1
        turn_back = 2 * i + (n - next_index)
        reverse_first = i + 2 * (n - next_index)
        move = min(move, turn_back, reverse_first)
    answer += move
    return answer