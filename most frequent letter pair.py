def most_frequent_pair(sentence):
    words = sentence.split()

    count = {}
    order = []          # pairs in order of first appearance

    for w in words:
        pair = w[0] + w[-1]     # first letter + last letter

        if pair not in count:
            count[pair] = 0
            order.append(pair)

        count[pair] = count[pair] + 1

    # find the highest count
    max_count = 0
    for pair in order:
        if count[pair] > max_count:
            max_count = count[pair]

    # collect all pairs with that count
    result = []
    for pair in order:
        if count[pair] == max_count:
            result.append(pair)

    return " ".join(result)


print(most_frequent_pair("she is good grid god and ground player plotter"))   # gd