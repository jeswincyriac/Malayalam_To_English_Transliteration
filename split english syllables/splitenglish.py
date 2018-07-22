import codecs

filein = codecs.open("secondroundenglishwords.txt","r",encoding="utf-8")
out = codecs.open ("splitted.txt","w",encoding="utf-8")
vowels =["a","e","i","o","u"]
engword=filein.readline()
while engword != "" :
    i=0
    while engword[i] !="$":
        out.write(engword[i])
        prev = engword[i]
        if engword[i] in vowels :
            out.write("\n")
            new = True

        if engword[i+1] =="r" and engword[i+2] == "i" and prev != "s" :
            i =i+1
            out.write(engword[i])
            prev = engword[i]
            new = False
        if engword[i+1] in vowels:
            exp =True
        else:
            exp =False
        exp2 = engword[i+1] == "y" and (prev != "y" and prev not in vowels and engword[i+2] not in vowels)
        exp3 = engword[i+1] == "h" and (prev != "y" and prev not in vowels)
        exp4 = exp2 or exp or exp3
        while exp4  :
            out.write(engword[i+1])
            prev = engword[i+1]
            new = False
            i=i+1
            if engword[i+1] in vowels:
                exp =True
            else:
                exp =False
            exp2 = engword[i+1] == "y" and (prev != "y" and prev not in vowels and engword[i+2] not in vowels )
            exp3 = engword[i+1] == "h" and (prev != "y" and prev not in vowels)
            exp4 = exp2 or exp or exp3
        if new == False:
            out.write("\n")
        i=i+1
        new = False

    engword=filein.readline()
