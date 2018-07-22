import subprocess
import codecs
from shutil import copy2

engword =  input("Enter your word ")
filetempe = codecs.open("tempe.txt","w",encoding="utf-8")
filetempe.write(engword)
filetempe.close()
subprocess.call(['./script1.sh'])
filee = codecs.open("english.txt","r",encoding="utf-8")
out = codecs.open ("splitted.txt","w",encoding="utf-8")
vowels =["a","e","i","o","u"]
engword=filee.readline()
while engword != "" :
    i=0
    c=0
    while engword[i] !="$":
        out.write(engword[i])
        prev = engword[i]
        if engword[i] in vowels :
            out.write(" 1")
            c=c+1
            out.write("\n")
            new = True

        if engword[i+1] =="r" and engword[i+2] == "i" and prev != "s" :
            i =i+1
            c=c+1
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
            c=c+1
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
            if c == 0:
                out.write(" 1")
                c=c+1
            elif engword[i+1] == "$":
                out.write(" 3")
            else:
                out.write(" 2")
            out.write("\n")
        i=i+1
        new = False

    engword=filee.readline()
out.close()
fileeng = codecs.open("splitted.txt","r",encoding="utf-8")
#filem = codecs.open("test2.txt","r",encoding="utf-8")
out = codecs.open ("/home/jeswin/Downloads/CRF++-0.57/finaleng.txt","w",encoding="utf-8")
engword=fileeng.readline()
#malword=filem.readline()
while engword != "" :
    out.write(str(len(engword)-3)+" ")
    out.write(engword)
    engword=fileeng.readline()
subprocess.Popen(["bash", "./script2.sh"])
