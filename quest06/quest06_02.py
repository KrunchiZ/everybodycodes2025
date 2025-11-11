note = "ABCCAbbCBbABAccbAbBbbCAAbbAaaacaacCCACAcAAACBcABCaCcCaBbBcCBaACBCaaBBbBcaAbCBcACccBBaabABbcaabCBBcCCAaAAaACbcbAcaBbACCACBcbCAccCBbCaAacBbbaBcbAAccbCabbcABCaCCAcCCBBaaBBBACbcbCABccCCAbBAaACACccBabcABcaCcAbAAcaAcABBcaCcbAaaBAAACcbcAcACCaBBCbcaCcaBCbAaCBCaBCBcabABCAaBABaCaCCababaAbaACAcCcCCAcbaAbACBbAC"
count = 0
for i in range(len(note) - 1):
    if ('A' <= note[i] <= 'Z'):
        uppercase = note[i]
        j = i + 1
        while (j < len(note)):
            if (note[j] == str.lower(uppercase)):
                count += 1
            j += 1
print(count)
