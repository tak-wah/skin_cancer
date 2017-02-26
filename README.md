# Melanoma Prediction

A web service that takes an images and returns the positive or negative possibility of  melanoma problem.

This project was inspired by a researcher group at Stanford university to predict skin cancer. However the result is not as good as theirs, due to the fact of a smaller dataset.

## Machine Learning Background

Under the hood we use [TensorFlow](https://www.tensorflow.org/), but we added [Keras](https://keras.io) as an extra layer on top which makes it easy to create a new model.

## Installation

Install [virtualenv](https://virtualenv.pypa.io/en/stable/)
```python
pip3 install virtualenv
```
Use virtualenv
```python
virtualenv tmp
source tmp/bin/activate
```

Install requirements by using PIP:
```python
pip3 install -r requirements.txt
```

## Starting
```python
python3 app.py
```
