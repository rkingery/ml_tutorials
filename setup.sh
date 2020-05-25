#! usr/bin/bash

conda install python pip -y
pip install -r requirements.txt
python -m spacy download en_core_web_sm
