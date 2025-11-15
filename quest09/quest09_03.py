def are_parents(p1, p2, child):
    for i in range(len(child)):
        if (child[i] != p1[i]) and (child[i] != p2[i]):
            return (False)
    return (True)

def find_parents(data, i):
    x = 1
    while (x < len(data)):
        y = 1
        while (x != i) and (y < len(data) + 1):
            if (y != i) and (y != x):
                if (are_parents(data[x], data[y], data[i]) == True):
                    return [x, y]
            y += 1
        x += 1
    return [0, 0]

def find_ancestors(parents, i):
    list = parents[i]
    if list == [0, 0]:
        return []
    list.extend(find_ancestors(parents, parents[i][0]))
    list.extend(find_ancestors(parents, parents[i][1]))
    return list

def find_descendants(parents, x):
    list = []
    a = 1
    while a <= len(parents):
        if x == parents[a][0] or x == parents[a][1]:
            list.append(a)
            list.extend(find_descendants(parents, a))
        a += 1
    return list

def find_siblings(parents, i):
    list = []
    if parents[i] == [0, 0]:
        return list
    for a in range(1, len(parents) + 1):
        if a!= i and parents[a] == parents[i]:
            list.append(a)
    return list

def main():
    data = {
        1: "GCAGGCGAGTATGATACCCGGCTAGCCACCCC",
        2: "TCTCGCGAGGATATTACTGGGCCAGACCCCCC",
        3: "GGTGGAACATTCGAAAGTTGCATAGGGTGGTG",
        4: "GCTCGCGAGTATATTACCGAACCAGCCCCTCA",
        5: "GCAGCTTAGTATGACCGCCAAATCGCGACTCA",
        6: "AGTGGAACCTTGGATAGTCTCATATAGCGGCA",
        7: "GGCGTAATAATCGGATGCTGCAGAGGCTGCTG",
        8: "GGCGTAAAGTATGGATGCTGGCTAGGCACCCG",
    }
    parents = {}
    scales = {}
    for i in range(1, len(data) + 1):
        parents[i] = find_parents(data, i)
    for i in range(1, len(parents) + 1):
        scales[i] = find_ancestors(parents, i)
    for i in range(1, len(parents) + 1):
        scales[i].extend(find_descendants(parents, i))
    print(parents)
    for i in range(1, len(parents) + 1):
        scales[i].extend(find_siblings(parents, i))
    print(scales)
    return

if __name__ == "__main__":
    main()
