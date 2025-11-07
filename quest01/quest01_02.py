list = ["Kharris","Ilmarsar","Falox","Azcoryx","Shaelgnar","Raeljor","Rahelor","Nythvash","Draiththys","Qalnor","Shaeleon","Thazfyr","Felnzor","Nexdra","Skarpyr","Drakox","Cyndthar","Tharthyn","Elvarryn","Myrsyron"]

index = 0

index = (index - 7 + 6 - 9 + 12 - 7 + 14 - 5 + 9 - 5 + 11 - 5 + 10 - 5 + 17 - 10 + 11 - 10 + 11 - 14) % len(list)


print(list[index])
