
# Stop It <img src='logo_stopit.png' align="right" height="165" />

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/made-with-javascript.svg)](https://forthebadge.com)  

[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v1.4%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md)

Stop It is a browser extension that helps people protect themselves against sexual harassment and sexist hate speech on Facebook and Twitter. The browser extension will have three functionalities:
- Block certain accounts on these platforms from writing comments.
- Automatically replace comments of a sexually aggressive nature.
- Give an overview of the sentiment of the comments on a page before it renders via a sentiment dashboard. The user can then chose what they do and don't want to see.

The project is still in its infancy. Please see 'Project Development' below for the current status.

## Overview

Sexual harassment and sexist hate speech are described by [international law](https://tbinternet.ohchr.org/Treaties/CEDAW/Shared%20Documents/1_Global/CEDAW_C_GC_35_8267_E.pdf) as acts of *gender based violence* happening *online* and *in technology-mediated spaces* that inflict *physical, mental or sexual harm or suffering, threats of such acts, coercion* and *other deprivations of liberty*. This is a global tragedy affecting the well-being, economical potential and representation of women. Let's __Stop It.__

To learn more about this problem and explore the steps Stop It is taking to combat it, see the [Stop It Wiki](https://github.com/malteserteresa/stop-it/wiki/The-Problem).

## Project Development

Stop It is an open source project under active development. Currently, machine learning models are being evaluated for their ability to classify sexual harrassment text. If you would like to test the current model (trained on troll data), please see the 'Installation Instructions' below. If you would like to contribute to the project, please see [Contributing](https://github.com/malteserteresa/stop-it/blob/master/contributing.md).

## Installation Instructions

To install the current model:
1. Clone this repository by running the command `git clone https://github.com/malteserteresa/stop-it.git` in the relevant directory.
2. [Download Anaconda](https://www.anaconda.com/distribution/#download-section)
3. Install Anaconda using the [guide for your operating system](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html#regular-installation)
4. Create a conda environment with the required depenencies by running the following bash command: 
`conda create --name stop-it tensorflow keras numpy pandas flask matplotlib scikit-learn pytest`
5. Run `source activate stop-it` to ensure the stop-it conda environment is selected.

## Usage
The two important files are **model.py** and **deploy.py** 

- model.py builds the model and saves it to a .h5 file 

- deploy.py predicts the sentiment of a sentence when the /predict API is hit.
It runs a flask server and loads a model from saved_model_data/models folder. 

If you just want to **play with the model**, open a terminal and: 
1. `cd into the top-level directory`
2. `python -m src/stopit build --path_to_data path/to/dataset --text_column_name eg. content --label_column_name eg. label`
*This will build the model only.*


Predict can be used similarly: `
1. `cd into the top-level directory`
2. `python -m src/stopit predict --path_to_model path/to/model --path_to_data path/to/dataset --text_column_name eg. content`
*Plot and evaluate are still under construction*


Or **deploy the project locally**: 
1. Check that you are loading in the model you wish within the deploy.py file.
2. In a terminal run: `python -m deploy.py`
3. And in the browser go to `127.0.0.1:5000/predict?sentence=your sentence to analyse`. Be sure to include spaces in the sentences. Spaces can be explicity set using the UTF-8 encoded `%20`. For example, to test the sentence 'Just Stop It', you could run:
- `127.0.0.1:5000/predict?sentence=Just Stop It` **or**
- `127.0.0.1:5000/predict?sentence=Just%20Stop%20It`

__NB__: the flask app needs to be re-initiated for each new sentence (you can exit the flask app pressing `Ctrl + c` and re-initiate it with `python deploy.py`). This is due to how TensorFlow works (more info can be found in the Issues tab).



To work on the browser extension run:
```
cd extension
npm install
```

And to run the test:
```
npm test
```

### Testing
To run the tests:
1.  `cd into the top-level directory`
2. `python -m pytest`

## Funding
If you would like to fund the project or make a donation, please email [Teresa Ingram](mailto:opt-out-tool@gmail.com)

***

> Please note that this project is released with a [Contributor Code of Conduct](https://github.com/malteserteresa/stop-it/blob/master/CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.


