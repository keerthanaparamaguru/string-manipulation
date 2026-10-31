def expand(s):
    first = {}      # character -> its first position (1-based)
    parts = []      # the repeated groups

    for i in range(len(s)):
        ch = s[i]

        if ch not in first:
            first[ch] = i + 1      # i starts at 0, so add 1

        parts.append(ch * first[ch])

    return "-".join(parts)


print(expand("abcaba"))    # a-bb-ccc-a-bb-a