# Applied Machine Learning Tutorials

## Background

This repo contains a series of notebooks on various aspects applied machine learning. The focus for much of the beginning is on classical learning, both supervised and unsupervised. Deep learning will be visited later on after foundations are established. The use of visualizations as a tool for understanding ML algorithms is highly emphasized throughout.

These tutorials originated from a series of talks I gave in 2018 for the IT division at Virginia Tech. Since these were applied talks, I didn't go into details on how to actually implement the algorithms. Regarding theory, I assume no background other than being able to read algebraic equations and some basic linear algebra. Any explicit use of probability theory is generally avoided since some may lack background in that material. I do assume that readers are familiar with python 3 and programming in general.

## Contents

The tutorials are intended to be worked through in the order the talks were given, which are
1. [Background](https://github.com/rkingery/ml_tutorials/blob/master/background.pdf) (read as needed)
2. [Classification](https://github.com/rkingery/ml_tutorials/blob/master/classification.ipynb)
3. [Regression](https://github.com/rkingery/ml_tutorials/blob/master/regression.ipynb)
4. [Dimensionality Reduction](https://github.com/rkingery/ml_tutorials/blob/master/dimension_reduction.ipynb)
5. [Clustering](https://github.com/rkingery/ml_tutorials/blob/master/clustering.ipynb)
6. [Supervised Anomaly Detection and Unbalanced Data](https://github.com/rkingery/ml_tutorials/blob/master/supervised_anomalies.ipynb)
7. [Unsupervised Anomaly Detection](https://github.com/rkingery/ml_tutorials/blob/master/unsupervised_anomalies.ipynb)
8. [Text Classification](https://github.com/rkingery/ml_tutorials/blob/master/ml_with_text.ipynb)
9. [Time Series Basics](https://github.com/rkingery/ml_tutorials/blob/master/time_series_basics.ipynb)
10. [Machine Learning with Time Series](https://github.com/rkingery/ml_tutorials/blob/master/ml_time_series.ipynb)
11. [Weakly Supervised Learning](https://github.com/rkingery/ml_tutorials/blob/master/weak_supervision.ipynb)

More tutorials will be added periodically. Check back.

## Viewing and Running Notebooks

If you want to view the notebooks without downloading them, you can use the [Jupyter nbviewer](https://nbviewer.jupyter.org/). Just paste the link to the notebook in their form. 

To execute the code, clone the repo and run `pip install -r requirements.txt` inside the repo root, ideally in an isolated virtual/conda environment. Notebooks can then be launched and run by running `jupyter notebook` in your shell and pasting the URL into your browser.

## Notes
- For those who'd prefer a docker container, docker support hasn't yet been built in, but I'm planning too soon.
- For those who prefer Google Collab, I hate Collab. Until it functions more like Jupyter I've no plans to use it. Sorry.
