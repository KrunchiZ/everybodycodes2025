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
    for i in range(len(data)):
        parents[i + 1] = find_parents(data, i + 1)
    print(parents)
    return

if __name__ == "__main__":
    main()
