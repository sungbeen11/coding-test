def solution(cap, n, deliveries, pickups):
    answer = 0

    while deliveries or pickups:
        while deliveries and deliveries[-1] == 0:
            deliveries.pop()

        while pickups and pickups[-1] == 0:
            pickups.pop()

        if not deliveries and not pickups:
            break

        answer += max(len(deliveries), len(pickups)) * 2

        del_cap = cap
        while deliveries and del_cap > 0:
            if deliveries[-1] <= del_cap:
                del_cap -= deliveries.pop()
            else:
                deliveries[-1] -= del_cap
                del_cap = 0

        pic_cap = cap
        while pickups and pic_cap > 0:
            if pickups[-1] <= pic_cap:
                pic_cap -= pickups.pop()
            else:
                pickups[-1] -= pic_cap
                pic_cap = 0

    return answer