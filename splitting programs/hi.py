import codecs
fileeng = codecs.open("final.txt","r",encoding="utf-8")
out = codecs.open("english.txt","w",encoding="utf-8")
engword=fileeng.readline()
while engword != "" :
      out.write(engword)
      engword=fileeng.readline()
      engword=fileeng.readline()
