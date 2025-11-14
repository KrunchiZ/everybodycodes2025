def count_matches(data, i):
    total = 1
    for j in range(1, 4):
        count = 0
        if (j != i):
            for a in range(len(data[i])):
                if (data[i][a] == data[j][a]):
                    count += 1
            total *= count
    return (total)

def main():
    data = {
    1: "CGGCAGTCTCGAAGGGTACTGTGTGCACGCGTCATTTTGATGGGACCTCCTAAAAACCGCGTGATCCACCCTTTCATTCTATGCGCCGGACGCACCCCGGGTTAAGTGGCATCCGCGGTAACTGATAA",
    2: "AATGCTAGTCTATAAGGGCCTTGGTCTTTCGGAAATGGCCCTTATAGATGAGGTACGCTTGGGCCAGCTGTTCGGGTAGAACTTCGGACGGTTCGGCTGATGTGTAGAAACGCTGAAGACTACTGGGG",
    3: "AATGAGTCTCGAAAGGTGCTGTGGGCTCGCGGCATTTGCCTTTATACTCGTAATAACCTTGTGATCGACGTTTTGATTGTATGCGGCGGGGTTAGCCTGAGGTAAGGAACCTCCGAGGTAAACGAGGG"
    }
    index = {}
    for i in range(1, 4):
        index[i] = count_matches(data, i)
    print(index[max(index)])
    return

if __name__ == "__main__":
    main()
