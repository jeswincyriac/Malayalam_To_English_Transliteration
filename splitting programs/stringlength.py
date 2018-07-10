import codecs
fileeng = codecs.open("english.txt","r",encoding="utf-8")
#filem = codecs.open("test2.txt","r",encoding="utf-8")
out = codecs.open ("finaleng.txt","w",encoding="utf-8")
engword=fileeng.readline()
#malword=filem.readline()
while engword != "" :
    out.write(str(len(engword)-1)+":")
    out.write(engword)
    engword=fileeng.readline()
