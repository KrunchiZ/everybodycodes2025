def name_fit_rules(name, rules):
    if (7 > len(name) > 11):
        return False
    for i in range(len(name) - 1):
        if (name[i] in rules) and (name[i + 1] not in rules[name[i]]):
            return False
    return True

def generate_list(name, rules, list):
    if (len(name) == 11):
        return
    tail = name[len(name) - 1]
    if (tail in rules):
        for i in rules[tail]:
            tmp = name + i
            if (7 <= len(tmp)):
                list.append(tmp)
            generate_list(tmp, rules, list)

def main():
    data = "Ny,Nyl,Nyth,Nyss,Nyrix,Pald,Cael,Fen,Gorath,Ryth,Zyrix,Gar,Grim,Xaral,Elar,Skar,Tharn,Rylar,Bryl,Nex"
    rules = {
        's': "asjfcxrzt",
        'E': "l",
        'X': "a",
        'N': "ey",
        'r': "aiejfcxrzstvn",
        'F': "e",
        'i': "soxm",
        'l': "yojfcxrzstdva",
        'a': "rlvt",
        'e': "xtlv",
        'Z': "y",
        'G': "oar",
        't': "hy",
        'k': "v",
        'j': "o",
        'C': "a",
        'T': "h",
        'o': "rnv",
        'R': "y",
        'y': "vxrl",
        'n': "jfcxrzst",
        'x': "sejfcxrzt",
        'B': "r",
        'd': "jfcxrzst",
        'S': "k",
        'f': "ae",
        'c': "a",
        'h': "jfcxrzstv",
        'z': "ei",
        'P': "a",
        'm': "jfcxrzst"
    }
    names = data.split(',')
    total = 0
    names_len = len(names)
    i = 0
    while i < names_len:
        if (name_fit_rules(names[i], rules) == False):
            names.remove(names[i])
            i = -1
            names_len -= 1
        i += 1
    list = []
    for name in names:
        generate_list(name, rules, list)
    list = set(list)
    list = sorted(list)
    print(len(list))

if __name__ == "__main__":
    main()
