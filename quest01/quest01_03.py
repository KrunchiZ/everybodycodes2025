list = ["Yndacris","Urcalyx","Durnral","Harnjorath","Thazagrath","Tirluth","Cyndnarel","Urakther","Balthgnaris","Naldralis","Kronadir","Vyrlyr","Fenxaril","Sorsin","Braerilor","Sarfeth","Vaelnixis","Nylmir","Vanfeth","Galasis","Hazaris","Uraksarix","Naronar","Zyrlyr","Wynzral","Zorkynar","Bryncarth","Tharncarth","Brythaxar","Lazxel"]

length = len(list)

index = (-16, 15, -13, 41, -13, 32, -19, 16, -35, 14, -19, 36, -44, 32, -45, 41, -49, 5, -34, 19, -5, 46, -5, 27, -5, 18, -5, 9, -5, 34, -5, 40, -5, 25, -5, 6, -5, 29, -5, 36, -5, 47, -34, 27, -31, 33, -29, 28, -30, 35, -34, 23, -31, 29, -17, 21, -32, 16, -34)

for i in range(len(index)):
    list[0], list[index[i] % length] = list[index[i] % length], list[0]

print(list[0])
