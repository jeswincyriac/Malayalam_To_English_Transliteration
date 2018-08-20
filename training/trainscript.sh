 awk '{print($1" "$2)}' test.txt >test1.txt
 cd ../CRF++-0.57
 crf_learn template ../training/test1.txt model
