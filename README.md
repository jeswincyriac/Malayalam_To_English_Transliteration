# Malayalam_To_English_Transliteration

This tool uses a Conditional Random Fields (CRF) model created by mapping the
correspondingly sounding English and Malayalam syllables. The model was trained on 3000 syllable pairs.We used a two judge accuracy evaluation and 73 of the 100 names predicted had a Levenshtein ratio higher than 0.9 according to the first judge ,while  69 of the 100 names were true according to the second judge.

## Prerequisites
* This project uses python3 and Bash.
* A copy of the [CRF++ tool](https://taku910.github.io/crfpp/) is provided along this repository. For installation and other details refer [here](https://taku910.github.io/crfpp/#install)  
## Running the tool
* run testing/program.py and input a word in Malayalam script to get its English transliteration as output.
* If you want to  train the model yourself
  * run training/splitmalayalm.py with the name of the file containing Malayalam words as argument.
  * similarly run training/splitenglish.py and give the filename of the English words as argument. 
  * use bash train.sh to train new model
  
## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
This transliteration project was done along with my team mate [Govind GS](https://github.com/govind4873) during the one month Natural Language Processing internship at ICFOSS(International Center for Free and Open Source Software,Trivandrum).Project mentors Deepu Shaji and Anju RC gave immense support under the guidence of project head Dr. Rajeev R R.
