def name_fit_rules(name, rules):
    for i in range(len(name) - 1):
        if (name[i] in rules) and (name[i + 1] not in rules[name[i]]):
            return False
    return True

def main():
    data = "Harndax,Azthyris,Harnthyris,Azwyris,Nydax,Harnwyris,Nythyris,Azdax,Nywyris"
    names = data.split(',')
    rules = {
        'N': "y",
        'n': "tdw",
        'y': "trb",
        'd': "a",
        'i': "s",
        'z': "b",
        'H': "a",
        'a': "xb",
        'A': "z",
        'w': "y",
        'r': "in",
        't': "h",
        'h': "y"
    }
    for name in names:
        if (name_fit_rules(name, rules) == True):
            print(name)
            return

if __name__ == "__main__":
    main()
