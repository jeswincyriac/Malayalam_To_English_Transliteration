import subprocess
import codecs
from shutil import copy2



#cmd = r"sed  's/ /\n/g' input.txt > temp.txt "
#subprocess.call(cmd, shell=True,universal_newlines=True)
subprocess.call(['./script1.sh'])
filem = codecs.open("malayalam.txt","r",encoding="utf-8")
out = codecs.open ("/home/jeswin/Downloads/CRF++-0.57/test.txt","w",encoding="utf-8")
malword=filem.readline()
while malword != "" :
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

    out.write("$ 9 9")
    out.write("\n")
    malword=filem.readline()
#subprocess.call(['./script2.sh'])
subprocess.Popen(["bash", "./script2.sh"])
filem.close()
out.close()
#tempin = codecs.open("output.txt","r",encoding="utf-8")
#tempout = codecs.open ("finaloutput.txt","w",encoding="utf-8")
#letter = tempin.readline()
#while malword != "" :
#    tempout.write(letter)
#    print(letter)
#    letter = tempin.readline()
