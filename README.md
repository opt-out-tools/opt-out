
## Let's Stop It - Sexual Cyber Harassment and Sexist Hate Speech

A tool to help people avoid online sexual harassment by filtering out unwanted comments from Facebook or Twitter.

### Installation requires:
tensorflow 1.12.2,
keras 2.2.4, 
numpy,
pandas,
flask,
matplotlib,
scikit-learn

To create an environment in conda run: `conda create --name stop-it tensorflow keras numpy pandas flask matplotlib scikit-learn`

### Usage:
python model.py

or using flask

python deploy.py and in the browser

127.0.0.1:5000/test?sentence="your sentence to analyse" (without quotation marks)

For further details about the project and topic as a whole, please see the wiki

- The Problem : Outlines the issue
- The Solution : Describes the browser extension that we are aiming to build and it's target functionality 
- Flow in TensorFlow : The current workings of the model
