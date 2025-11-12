def name_fit_rules(name, rules):
    for i in range(len(name) - 1):
        if (name[i] in rules) and (name[i + 1] not in rules[name[i]]):
            return False
    return True

def main():
    data = "Xendthys,Harnnar,Wyrnar,Xendcion,Tharoris,Tharvoran,Zraalmir,Xendnar,Taloris,Talmir,Harnvoran,Talnar,Talcion,Talthys,Talvoran,Talaris,Xendmir,Harncion,Xendvoran,Wyrcion,Tharnar,Xendsar,Harnaris,Wyrtaril,Harnthys,Harnoris,Tharsar,Zraaloris,Harnmir,Zraaloris,Wyrcion,Tharcion,Wyrvoran,Zraalthys,Harnsar,Wyrsar,Tyrtaril,Taltaril,Brylmir,Brylcion,Talsar,Harntaril,Tyrsar,Tyraris,Tyrvoran,Urmir,Harncion,Xendoris,Zraaltaril,Talcion,Wyroris,Zraalsar,Urtaril,Thararis,Tharthys,Urthys,Tharmir,Bryltaril,Urnar,Xendcion,Zraalsar,Zraalmir,Xendaris,Zraalcion,Bryloris,Zraalcion,Xendtaril,Tharcion,Wyrmir,Brylnar,Wyrthys,Zraaltaril,Brylaris,Zraalthys,Brylvoran,Wyraris,Uroris,Urcion,Brylthys,Urvoran,Tyrthys,Tyroris,Zraalaris,Tyrnar,Zraalvoran,Zraalvoran,Zraalnar,Uraris,Tyrcion,Zraalcion,Tyrmir,Brylcion,Thartaril,Zraalcion,Brylsar,Ursar,Zraalnar,Tyrcion,Urcion,Zraalaris"
    names = data.split(',')
    rules = {
        'y': "svl",
        'r': "ainsoctvm",
        'e': "v",
        'i': "rsol",
        'm': "i",
        'd': "soactnvm",
        'v': "o",
        'o': "rn",
        'l': "msoactnv",
        'H': "a",
        'n': "asoctnvmd",
        'h': "yv",
        'a': "alvrn",
        'B': "r",
        'W': "y",
        's': "a",
        'c': "i",
        'T': "ahy",
        'Z': "r",
        't': "ha",
        'X': "e",
        'U': "r"
    }
    checksum = 0
    for i in range(len(names)):
        if (name_fit_rules(names[i], rules) == True):
            checksum += (i + 1)
    print(checksum)

if __name__ == "__main__":
    main()
