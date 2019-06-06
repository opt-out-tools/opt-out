
# Opt Out <img src='logo.png' align="right" height="165" />

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/made-with-javascript.svg)](https://forthebadge.com)  

[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v1.4%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md)

Opt Out is a browser extension that filters sexual harassment and sexist hate speech from an individual’s twitter feed. 

The General Data Protection Regulation (GDPR) has changed our lives online on social media platforms. We have the right to be forgotten, to see what is being collected about us and to opt-out if we wish. The current abuse that those who identify as women suffer is not avoidable. We see Opt Out as an extension of the GDPR that also protects the human rights of women and those with intersecting identities online. While steps have been made to protect these people online, not enough has been done. This is a global tragedy affecting the well-being, economical potential and political representation of these people. Let's __Opt Out.__

To learn more about this problem and explore the steps Opt Out is taking to combat it, see the [Opt Out Wiki](https://github.com/malteserteresa/opt-out/wiki/The-Problem).

The project is still in its infancy. Please see 'Project Development' below for the current status.

## To Install

 ```
    git clone https://github.com/opt-out-tool/opt-out
    cd opt-out
    pip install -r requirements.txt
```
## To Deploy Locally
 ```
    export FLASK_APP=deploy.py
    export FLASK_DEBUG=1
    flask run
 ```



## To Use
1. Deploy locally (follow the steps above)
2. And in the browser go to `127.0.0.1:5000/predict?sentence=your sentence to analyse`. Be sure to include spaces in the sentences. Spaces can be explicity set using the UTF-8 encoded `%20`. For example, to test the sentence 'Just Opt Out', you could run:
- `127.0.0.1:5000/predict?sentence=Just Opt Out` **or**
- `127.0.0.1:5000/predict?sentence=Just%20Opt%20Out`

## To Test
To run the tests:
```
  cd opt-out
  python -m pytest
```

## To Deploy (Docker)
TBC

## Project Development

Opt Out is an open source project under active development. Currently, machine learning models are being evaluated for their ability to classify sexual harassment text. If you would like to test the current model (trained on troll data), please see the 'Installation Instructions' below. If you would like to contribute to the project, please see [Contributing](https://github.com/malteserteresa/opt-out/blob/master/contributing.md) first, and then check out the find-out and try-out repos.


## Funding
If you would like to fund the project or make a donation, please email [Teresa Ingram](mailto:opt-out-tool@gmail.com)

***

> Please note that this project is released with a [Contributor Code of Conduct](https://github.com/malteserteresa/opt-out/blob/master/CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.


