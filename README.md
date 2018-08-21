# Malayalam_To_English_Transliteration

This tool uses a Conditional Random Fields (CRF) model created by mapping the
correspondingly sounding English and Malayalam syllables. The model was trained on 3000 syllable pairs.We used a two judge accuracy evaluation and 73 of the 100 names predicted had a Levenshtein ratio higher than 0.9 according to the first judge ,while  69 of the 100 names were true according to the second judge.

### Prerequisites
* This project uses python3 and Bash.
* A copy of the [CRF++ tool](https://taku910.github.io/crfpp/) is provided along this repository. For installation and other details refer [here](https://taku910.github.io/crfpp/#install)  
### Running the tool
* run testing/program.py and input a word in Malayalam script to get its English transliteration as output.
* If you want to  

This transliteration project was done as part of the one month Natural Language Processing internship at ICFOSS(International Center for Free and Open Source Software) 
