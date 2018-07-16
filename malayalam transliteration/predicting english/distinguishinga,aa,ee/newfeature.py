import codecs

filem = codecs.open("mala.txt","r",encoding="utf-8")
out = codecs.open ("swara.txt","a",encoding="utf-8")
malword=filem.readline()
while malword != "" :
    swaraksharam = "0"
    expr = malword[0] == "അ" or malword[0] =="ആ" or malword[0] =="ഇ" or malword[0] =="ഈ" or malword[0] =="ഉ"or malword[0] =="ഊ" or malword[0] =="ഋ" or malword[0] =="എ"
    expr2 = malword[0] =="ഏ" or malword[0] =="ഐ" or malword[0] =="ഒ" or malword[0] =="ഓ" or malword[0] =="ഔ"
    if(expr or expr2):
      swaraksharam = "1"
    out.write(swaraksharam+"\n")
    malword=filem.readline()
