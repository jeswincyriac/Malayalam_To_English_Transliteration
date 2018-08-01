#!/bin/sh
cd /home/jeswin/Downloads/CRF++-0.57
#echo hi >hi.txt
#after
awk '{print($1" "$2)}' test.txt >test1.txt
crf_test -m model test1.txt >tempoutput.txt
cp tempoutput.txt /media/jeswin/Lectures\ and\ Files/icfoss/malayalam_transliteration/predicting_english/without_distinguishing/transliterate
#rm tempoutput.txt
cd /media/jeswin/Lectures\ and\ Files/icfoss/malayalam_transliteration/predicting_english/without_distinguishing/transliterate
awk '{print($3)}' tempoutput.txt >output1.txt
tr -d '\n' < output1.txt > output2.txt
tr "$" "\n" < output2.txt>output.txt
cat output.txt
#rm output2.txt
#rm tempoutput.txt
#rm output1.txt
