# Applied Machine Learning Tutorials

## Background

This repo contains a series of notebooks on various aspects applied machine learning. The focus for much of the beginning is on classical learning, both supervised and unsupervised. Deep learning will be visited later on after foundations are established. The use of visualizations as a tool for understanding ML algorithms is highly emphasized throughout.

These tutorials originated from a series of talks I gave in 2018 for the IT division at Virginia Tech. Since these were applied talks, I didn't go into details on how to actually implement the algorithms. Regarding theory, I assume no background other than being able to read algebraic equations and some basic linear algebra. Any explicit use of probability theory is generally avoided since some may lack background in that material. I do assume that readers are familiar with python 3 and programming in general.

## Contents

### Fundamentals
- [Background](https://github.com/rkingery/ml_tutorials/blob/master/resources/background.pdf) (read as needed)
- [Binary Classification](https://github.com/rkingery/ml_tutorials/blob/master/notebooks/classification.ipynb)
- [Multiclass Classification](https://github.com/rkingery/ml_tutorials/blob/master/notebooks/multiclass.ipynb) (TBA)
- [Regression](https://github.com/rkingery/ml_tutorials/blob/master/notebooks/regression.ipynb)
- [Dimensionality Reduction](https://github.com/rkingery/ml_tutorials/blob/master/notebooks/dimension_reduction.ipynb)
- [Clustering](https://github.com/rkingery/ml_tutorials/blob/master/notebooks/clustering.ipynb)

### Applications
- [Supervised Anomaly Detection and Unbalanced Data](https://github.com/rkingery/ml_tutorials/blob/master/notebooks/supervised_anomalies.ipynb)
- [Unsupervised Anomaly Detection](https://github.com/rkingery/ml_tutorials/blob/master/notebooks/unsupervised_anomalies.ipynb)
7. [Text Classification](https://github.com/rkingery/ml_tutorials/blob/master/notebooks/ml_with_text.ipynb)
8. [Time Series Basics](https://github.com/rkingery/ml_tutorials/blob/master/notebooks/time_series_basics.ipynb)
9. [Machine Learning with Time Series](https://github.com/rkingery/ml_tutorials/blob/master/notebooks/ml_time_series.ipynb)

### Dealing with Inadequate Data
- [Labeling Data](https://github.com/rkingery/ml_tutorials/blob/master/notebooks/labeling_data.ipynb) (TBA)
- [Active Learning](https://github.com/rkingery/ml_tutorials/blob/master/notebooks/active_learning.ipynb) (TBA)

Tutorials are added periodically. Check back.

## Viewing and Running Notebooks

If you want to view the notebooks without downloading them, you can use the [Jupyter nbviewer](https://nbviewer.jupyter.org/). Just paste the URL to the notebook there and it will render correctly. 

To execute the code, clone the repo and run `pip install -r requirements.txt` inside the repo root, ideally in an isolated virtual/conda environment. Notebooks can then be launched and run by running `jupyter notebook` in your shell and pasting the URL into your browser.

## Notes
- For those who'd prefer a docker container, docker support hasn't yet been built in, but I'm planning to soon.
- For those who prefer Google Colab, I hate Colab. Until it functions more like Jupyter I've no plans to use it. Sorry.
