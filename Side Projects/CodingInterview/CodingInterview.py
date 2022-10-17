def Convert(suite):
    if(len(suite) == 0):
        return " "
    else:
        lst_char = []
        occurence = []
        return_string = ""

        for lettre in suite:
            if(lettre not in lst_char):
                lst_char.append(lettre)

        for element in lst_char:
            occ = suite.count(element)
            occurence.append(occ)

        for i in range(len(lst_char)):
            return_string+=str(occurence[i])+ "" + lst_char[i]
        
        return return_string

suite = "aaaabbccc"
res = Convert(suite)
print(res)

