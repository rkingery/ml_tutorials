# Applied Machine Learning Tutorials

## Background

This repo contains a series of notebooks on various aspects applied machine learning. The focus for much of the beginning is on classical learning, both supervised and unsupervised. Deep learning will be visited later on after foundations are established. The use of visualizations as a tool for understanding ML algorithms is highly emphasized throughout.

These tutorials originated from a series of talks I gave in 2018 for the IT division at Virginia Tech. Since these were applied talks, I didn't initially plan to go into details on how to actually implement the algorithms. I am starting to put together notebooks to address the fundamentals more, mainly to help with those preparing data science interviews.

## Knowledge Assumed

Regarding theory, I assume no background other than being able to read algebraic equations and some basic linear algebra. Knowledge of probability theory shouldn't be essential for going through the tutorials, but may be helpful in some areas. On the practical side of things, I assume that readers are familiar with python 3 and basic programming concepts in general.

## Contents

- [Mathematical Background](https://github.com/rkingery/ml_tutorials/blob/master/resources/background.pdf) (read as needed)
- [Binary Classification](https://github.com/rkingery/ml_tutorials/blob/master/notebooks/classification.ipynb)
- [Regression](https://github.com/rkingery/ml_tutorials/blob/master/notebooks/regression.ipynb)
- [Dimensionality Reduction](https://github.com/rkingery/ml_tutorials/blob/master/notebooks/dimension_reduction.ipynb)
- [Clustering](https://github.com/rkingery/ml_tutorials/blob/master/notebooks/clustering.ipynb)
- [Supervised Anomaly Detection and Unbalanced Data](https://github.com/rkingery/ml_tutorials/blob/master/notebooks/supervised_anomalies.ipynb)
- [Unsupervised Anomaly Detection](https://github.com/rkingery/ml_tutorials/blob/master/notebooks/unsupervised_anomalies.ipynb)
- [Text Classification](https://github.com/rkingery/ml_tutorials/blob/master/notebooks/ml_with_text.ipynb)
- [Time Series Basics](https://github.com/rkingery/ml_tutorials/blob/master/notebooks/time_series_basics.ipynb)
- [Machine Learning with Time Series](https://github.com/rkingery/ml_tutorials/blob/master/notebooks/ml_time_series.ipynb)
- [Generating Random Numbers](https://github.com/rkingery/ml_tutorials/blob/master/notebooks/random.ipynb)
- [Multiclass Classification](https://github.com/rkingery/ml_tutorials/blob/master/notebooks/multiclass.ipynb) (TBA)
- [Labeling Data](https://github.com/rkingery/ml_tutorials/blob/master/notebooks/labeling_data.ipynb) (TBA)
- [Active Learning](https://github.com/rkingery/ml_tutorials/blob/master/notebooks/active_learning.ipynb) (TBA)

Tutorials are added periodically. Check back.

## Viewing the Notebooks

If you want to view the notebooks without downloading them, you can use the [Jupyter nbviewer](https://nbviewer.jupyter.org/). Just paste the URL to the notebook there and it will render correctly. 

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
One day soon man. One day soon.

## Notes
- For those who prefer Google Colab, I hate Colab. Until it functions more like Jupyter I've no plans to use it. Sorry.
