def min_cost(N, P, Q):
    best = -1
    max_buses = (N + 79) // 80      # buses needed if only buses were used

    for b in range(max_buses + 1):
        left = N - b * 80           # people still waiting
        if left < 0:
            left = 0

        shuttles = (left + 7) // 8  # round up: shuttles for leftover people
        litres = b * P + shuttles * Q

        if best == -1 or litres < best:
            best = litres

    return best * 75


print(min_cost(240, 50, 8))    # 11250
print(min_cost(95, 60, 10))    # 6000