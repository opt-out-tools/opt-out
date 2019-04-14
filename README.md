## Anti-Harassment Browser Extension

A tool to help people avoid online sexual harassment by filtering out unwanted comments from Facebook, Twitter or Youtube.

Installation:

Usage:

python model.py

or using flask

python deploy.py and in the browser http://127.0.0.1:5000/test?sentence=<your sentence to analyse>

Contributing: 

Credits:

### To do (Priority order):
- Optimize ranking method -> dictionary.py
- Plot WVS for model -> model.py
- Refactor tests and add more accurate test cases like stop words or escape characeters within sentences -> normalize.py
- Think about synonyms in corpus dictionary -> dictionary.py
- Read more around re module and refactor escape\_ and replace\_ methods into one -> normalize.py
- Why are own imports not working properly -> model.py

### Bugs
- Word embeddings are incredibly flat

### Resolved
- Not all stopwords being removed -> normalize.py -> due to when remove punctuation and whitespaces not being trimmed ---> resolved by changing the ordering of processes within normalize
