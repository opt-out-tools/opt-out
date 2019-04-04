## Anti-Harassment Browser Extension

A tool to help people avoid online sexual harassment by filtering out unwanted comments from Facebook, Twitter or Youtube.

Installation:

Usage:

Contributing: 

Credits:

To do:
- Think about synonyms in corpus dictionary -> dictionary.py
- Add more tests with different unicode characters and when unicodes are near numbers -> normalize.py
- Read more around re module and refactor escape\_ and replace\_ methods into one -> normalize.py
- Why are own imports not working properly -> model.py
- Optimize ranking method -> dictionary.py
- Plot WVS for model -> model.py
### Bugs
- Not all stopwords being removed -> normalize.py -> due to when remove punctuation and whitespaces not being trimmed
- Word embeddings are incredibly flat
