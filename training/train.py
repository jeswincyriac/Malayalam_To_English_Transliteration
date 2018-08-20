import codecs
import sys
import subprocess
filem = codecs.open(sys.argv[1],"r",encoding="utf-8")
#fileeng = open ("english.txt","r")
out = codecs.open ("test.txt","a",encoding="utf-8")
malword=filem.readline()

while malword != "" :

    #engword=fileeng.readline().lower()
    i=0
    while malword[i] !="$":
        out.write(malword[i])
        exp = malword[i+1] == "ി"or malword[i+1] =="ാ"or malword[i+1] == "ീ"or malword[i+1] == "ു"or malword[i+1] == "ൂ"or malword[i+1] == "ൃ"or malword[i+1] == "ൗ"
        exp2= malword[i+1] ==  "േ" or malword[i+1] =="ൈ"or malword[i+1] =="ോ"or malword[i+1] =="ൌ"or malword[i+1] =="െ" or malword[i+1] =="്"or malword[i+1] == "ം"
        if ( (exp or exp2 or malword[i+1] =="ൊ") and malword[i+2] =="ം"):
            out.write(malword[i+1])
            out.write(malword[i+2])
            out.write(" ")
            out.write(malword[i+1])
            out.write(malword[i+2])
            if i==0:
                out.write(" 1 ")
            elif malword[i+2] == "$" or malword[i+3] == "$" :
                out.write(" 3 ")
            else:
                out.write(" 2 ")

            i=i+3
        elif ( exp or exp2 or malword[i+1] =="ൊ"):
            out.write(malword[i+1])
            out.write(" ")
            out.write(malword[i+1])
            if i==0:
                out.write(" 1 ")
            elif malword[i+2] == "$"  :
                out.write(" 3 ")
            else:
                out.write(" 2 ")
            i=i+2

        else:
            out.write(" 0 ")
            if i==0:
                out.write(" 1 ")
            elif malword[i+1] == "$" :
                out.write(" 3 ")
            else:
                out.write(" 2 ")

            i=i+1
        out.write("\n")


    malword=filem.readline()
subprocess.call(['./trainscript.sh'])
