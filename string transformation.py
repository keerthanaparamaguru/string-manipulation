def transform_cost(s1, s2):
    # count letters in s1
    count1 = {}
    for ch in s1:
        count1[ch] = count1.get(ch, 0) + 1

    # count letters in s2
    count2 = {}
    for ch in s2:
        count2[ch] = count2.get(ch, 0) + 1

    cost = 0
    for ch in count2:
        have = count1.get(ch, 0)    # how many we already have
        need = count2[ch]           # how many we need

        if need > have:
            cost = cost + (need - have)

    return cost


print(transform_cost("ABD", "AABCCAD"))    # 4
print(transform_cost("ABC", "XYZ"))        # 3