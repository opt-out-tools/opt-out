
# Stop It <img src='logo.png' align="right" height="139" />

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/made-with-javascript.svg)](https://forthebadge.com)[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v1.4%20adopted-ff69b4.svg)](code-of-conduct.md)

Stop It is a tool to help people avoid cyber sexual harassment and sexist hate speech by filtering out unwanted comments on platforms such as Facebook and Twitter. Stop It will be released as a browser extension, that automatically scans and blocks unwanted comments.

## Overview

Sexual harassment and sexist hate speech are described by [international law](https://tbinternet.ohchr.org/Treaties/CEDAW/Shared%20Documents/1_Global/CEDAW_C_GC_35_8267_E.pdf) as acts of *gender based violence* happening *online* and *in technology-mediated spaces* that inflict *physical, mental or sexual harm or suffering, threats of such acts, coercion* and *other deprivations of liberty*. This is a global tragedy affecting the well-being, economical potential and representation of women. Let's __Stop It.__

To learn more about this problem and explore the steps Stop It is taking to combat it, see the [Stop It Wiki](https://github.com/malteserteresa/stop-it/wiki/The-Problem).

## Open Source Project

Stop It is an open source project under active development. Currently, machine learning models are being evaluated for their ability to classify sexual harrassment text. If you would like to test the current model (trained on troll data), please see the 'Installation Instructions' below. If you would like to contribute to the project, please see [Contributing](https://github.com/malteserteresa/stop-it/blob/master/contributing.md).

## Installation Instructions

To install the current model:
1. [Download Anaconda](https://www.anaconda.com/distribution/#download-section)
2. Install Anaconda using the [guide for your operating system](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html#regular-installation)
3. Create a conda environment with the required depenencies by running the following bash command: `conda create --name stop-it tensorflow keras numpy pandas flask matplotlib scikit-learn pytest`

## Usage
In a Terminal, run the command: `python model.py`

Or using flask, run: `python deploy.py`
And in the browser go to 127.0.0.1:5000/predict?sentence=your sentence to analyse. 
Be sure to include spaces in the sentences. Spaces can be explicity set using the UTF-8 encoded `%20`.

To work on the browser extension run:
```
cd extension
npm install
```

And to run the test:
```
npm test
```

## Funding
If you would like to fund the project or make a donation, please email [Tess Ingram](mailto:tee.in.grams@gmail.com)


