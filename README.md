# Applied Machine Learning Tutorials

## Background

This repo contains a series of notebooks on various aspects applied machine learning. The focus for much of the beginning is on classical learning, both supervised and unsupervised. Deep learning will be visited later on after foundations are established. The use of visualizations as a tool for understanding ML algorithms is highly emphasized throughout.

These tutorials originated from a series of talks I gave in 2018 for the IT division at Virginia Tech. Since these were applied talks, I didn't initially plan to go into details on how to actually implement the algorithms. I am starting to put together notebooks to address the fundamentals more, mainly to help with those preparing data science interviews.

## Knowledge Assumed

Regarding theory, I assume no background other than being able to read algebraic equations and some basic linear algebra (e.g. matrix multiplication, vectors). Knowledge of probability theory shouldn't be essential for going through most of the tutorials, but may be helpful in some areas. Similarly, if calculus shows up somewhere, you can probably ignore it and be fine. On the practical side of things, I assume that readers are familiar with python and basic programming concepts in general.

## Contents

### Core Knowledge
- [Arrays, Dataframes, Plotting](https://nbviewer.jupyter.org/github/rkingery/ml_tutorials/blob/master/notebooks/arrays.ipynb)
- [Binary Classification](https://nbviewer.jupyter.org/github/rkingery/ml_tutorials/blob/master/notebooks/classification.ipynb)
- [Regression](https://nbviewer.jupyter.org/github/rkingery/ml_tutorials/blob/master/notebooks/regression.ipynb)
- [Dimensionality Reduction](https://nbviewer.jupyter.org/github/rkingery/ml_tutorials/blob/master/notebooks/dimension_reduction.ipynb)
- [Clustering](https://nbviewer.jupyter.org/github/rkingery/ml_tutorials/blob/master/notebooks/clustering.ipynb)
- [ Unbalanced Data and Supervised Anomaly Detection](https://nbviewer.jupyter.org/github/rkingery/ml_tutorials/blob/master/notebooks/supervised_anomalies.ipynb)
- [Data Wrangling Part 1: EDA](https://nbviewer.jupyter.org/github/rkingery/ml_tutorials/blob/master/notebooks/eda.ipynb)
- [Data Wrangling Part 2: Cleaning](https://nbviewer.jupyter.org/github/rkingery/ml_tutorials/blob/master/notebooks/data_cleaning.ipynb) (WIP)
<!-- - [Multiclass Classification and Categorical Data](https://nbviewer.jupyter.org/github/rkingery/ml_tutorials/blob/master/notebooks/multiclass.ipynb) (TBA) -->

### Deep Learning
- [PyTorch: Tensors, Autodiff, Cuda](https://nbviewer.jupyter.org/github/rkingery/ml_tutorials/blob/master/notebooks/pytorch.ipynb)
- [Neural Networks (Part 1): Basics](https://nbviewer.jupyter.org/github/rkingery/ml_tutorials/blob/master/notebooks/neural_nets_1.ipynb)
- [Neural Networks (Part 2): Going Deeper](https://nbviewer.jupyter.org/github/rkingery/ml_tutorials/blob/master/notebooks/neural_nets_2.ipynb)
- [Neural Networks (Part 3): Optimizers](https://nbviewer.jupyter.org/github/rkingery/ml_tutorials/blob/master/notebooks/neural_nets_3.ipynb)
- [Convolutional Neural Networks (Part 1): Basics](https://nbviewer.jupyter.org/github/rkingery/ml_tutorials/blob/master/notebooks/cnns_1.ipynb)

### Natural Language Processing
- [Text Classification](https://nbviewer.jupyter.org/github/rkingery/ml_tutorials/blob/master/notebooks/ml_with_text.ipynb)

### Computer Vision

### Other
- [Unsupervised Anomaly Detection](https://nbviewer.jupyter.org/github/rkingery/ml_tutorials/blob/master/notebooks/unsupervised_anomalies.ipynb)
- [Time Series Basics](https://nbviewer.jupyter.org/github/rkingery/ml_tutorials/blob/master/notebooks/time_series_basics.ipynb)
- [Machine Learning with Time Series](https://nbviewer.jupyter.org/github/rkingery/ml_tutorials/blob/master/notebooks/ml_time_series.ipynb)
- [ML Deep Dive: Probability and Naive Bayes](https://nbviewer.jupyter.org/github/rkingery/ml_tutorials/blob/master/notebooks/naive_bayes.ipynb)
- [Generating Random Numbers](https://nbviewer.jupyter.org/github/rkingery/ml_tutorials/blob/master/notebooks/random.ipynb)
<!-- - [ML Deep Dive: Nearest Neighbors](https://nbviewer.jupyter.org/github/rkingery/ml_tutorials/blob/master/notebooks/nearest_neighbors.ipynb) (TBA) -->
<!-- - [Labeling Data](https://nbviewer.jupyter.org/github/rkingery/ml_tutorials/blob/master/notebooks/labeling_data.ipynb) (TBA) -->
<!-- - [Active Learning](https://nbviewer.jupyter.org/github/rkingery/ml_tutorials/blob/master/notebooks/active_learning.ipynb) (TBA) -->

Tutorials are added periodically. Check back.

## Viewing the Notebooks

If you want to view the notebooks without downloading them, you can just click the links here in the README, or use the [Jupyter nbviewer](https://nbviewer.jupyter.org/) website, where you can just paste the URL to the notebook and it should render correctly. 

## Running the Notebooks

### Install using local conda environment
To setup an environment to run the notebooks on your own machine, you should first have [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [anaconda](https://docs.anaconda.com/anaconda/install/) installed and working on your computer. Once you've done this, do the following in sequence to setup your environment. Note: If running on Windows (sorry bro) you may need to modify these commands slightly.

```
conda create --name ml_tutorials python=3.6 pip
conda activate ml_tutorials
# recommend making sure your shell is using the python and pip packages inside your anaconda path (e.g. ~/anaconda3/.../python)
which python && which pip
# if python or pip path is something different (e.g. /usr/local/bin/python), restart your shell and try again
cd <directory where you want repo to go>
git clone https://github.com/rkingery/ml_tutorials.git
cd ml_tutorials
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

Once your environment is setup, each time you want to use it I recommend following a workflow something like this.

```
conda activate ml_tutorials
cd <path to ml_tutorials>
git pull
pip install -r requirements.txt  # occasionally new packages may be added
jupyter notebook  # should launch a jupyter session in your browser
conda deactivate  # when finished with session
```

### Install with Docker
TBD.

