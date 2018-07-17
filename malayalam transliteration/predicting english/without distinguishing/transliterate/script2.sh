#!/bin/sh
cd /home/jeswin/Downloads/CRF++-0.57
#echo hi >hi.txt
crf_test -m model test.txt >output.txt
cp output.txt /media/jeswin/Lectures and Files/icfoss/malayalam_transliteration/predicting_english/without_distinguishing/transliterate
