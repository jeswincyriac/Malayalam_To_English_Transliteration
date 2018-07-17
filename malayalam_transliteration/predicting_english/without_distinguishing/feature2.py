#extracts chillaksharam

#awk '{print($4)}' out1.txt>preeng.txt
import codecs

filem = codecs.open("preeng.txt","r",encoding="utf-8")
out = codecs.open ("preeng2.txt","w",encoding="utf-8")
malword=filem.readline()
while malword != "" :
    i=0
    out.write(malword[i])
    exp = malword[i+1] == "ി"or malword[i+1] =="ാ"or malword[i+1] == "ീ"or malword[i+1] == "ു"or malword[i+1] == "ൂ"or malword[i+1] == "ൃ"or malword[i+1] == "ൗ"
    exp2= malword[i+1] ==  "േ" or malword[i+1] =="ൈ"or malword[i+1] =="ോ"or malword[i+1] =="ൌ"or malword[i+1] =="െ" or malword[i+1] =="്"or malword[i+1] == "ം"
    if (( exp or exp2 or malword[i+1] =="ൊ") and malword[i+2] =="ം" ):
        out.write(malword[i+1])
        out.write(malword[i+2])
        out.write(": ")
        out.write(malword[i+1])
        out.write(malword[i+2])
        i=i+2
        out.write("\n")
    elif ( exp or exp2 or malword[i+1] =="ൊ"):
        out.write(malword[i+1])
        out.write(": ")
        out.write(malword[i+1])
        i=i+1
        out.write("\n")
    else:
        out.write(": 0")
        out.write("\n")
    malword=filem.readline()
#column -t -s $':' preeng2.txt >preeng3.txt
