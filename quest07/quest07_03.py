def name_fit_rules(name, rules):
    if (7 > len(name) > 11):
        return False
    for i in range(len(name) - 1):
        if (name[i] in rules) and (name[i + 1] not in rules[name[i]]):
            return False
    return True

def generate_list(name, rules, list):
    if (len(name) > 11):
        return
    tail = name[len(name) - 1]
    if (tail in rules):
        for i in range(len(rules[tail])):
            tmp = name + rules[tail][i]
            print(tmp)
            if (7 <= len(tmp) <= 11):
                list.append(tmp)
            generate_list(tmp, rules, list)


def main():
    data = "Khara,Xaryt,Noxer,Kharax"
    names = data.split(',')
    rules = {
        'r': "veagy",
        'a': "evxrg",
        'e': "rxvt",
        'h': "aev",
        'g': "ry",
        'y': "pt",
        'i': "vr",
        'K': "h",
        'v': "e",
        'B': "r",
        't': "h",
        'N': "e",
        'p': "h",
        'H': "e",
        'l': "t",
        'z': "e",
        'X': "a",
        'n': "v",
        'x': "z",
        'T': "i"
    }
    total = 0
    for name in names:
        if (name_fit_rules(name, rules) == False):
            names.remove(name)
    print(names)
    list = []
    for name in range(len(names)):
        generate_list(name, rules, list)
    print(len(list))

if __name__ == "__main__":
    main()
