# Melanoma Prediction

A web service that takes an images and returns the positive or negative possibility of  melanoma problem.

This project was inspired by a researcher group at Stanford university to predict skin cancer. However the result is not as good as theirs, due to the fact of a smaller dataset.

## Machine Learning Background

Under the hood we use [TensorFlow](https://www.tensorflow.org/), but we added [Keras](https://keras.io) as an extra layer on top which makes it easy to create a new model.

## Installation
### Everything else

Install requirements by using PIP:
```python
pip3 install -r requirements.txt
```
### Windows
#### Forget it!

~~It is recommended to use [Anaconda](https://www.continuum.io/downloads). The version 4.3.0 comes with python 3.6. You should change to version 3.5.0 after installing when using TensorFlow 1.0.0:~~
```python
conda install python=3.5.0
```
~~Go ahead with downloading TensorFlow:~~
```python
conda create -n tensorflow python=3.5
activate tensorflow
conda install -c conda-forge tensorflow
```
