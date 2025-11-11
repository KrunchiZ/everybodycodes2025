note = "ABCAaBBBABACbCbCACaAabbbCaAbCbAaAccCcBBBBABBCBaBCaBACcaCcABBcAbbaCCccbAcAaaAAbcbcCCcabAbbbacBBBbBCaB"
count = 0
for i in range(len(note) - 1):
    if (note[i] == 'A'):
        j = i + 1
        while (j < len(note)):
            if (note[j] == str.lower(note[i])):
                count += 1
            j += 1
print(count)
