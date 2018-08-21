 awk '{print($1" "$2)}' malsplit.txt >test.txt
 paste test.txt splitted.txt>train.txt
cd ../CRF++-0.57
crf_learn template ../training/train.txt model
