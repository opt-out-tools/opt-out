
## Let's Stop It - Sexual Cyber Harassment and Sexist Hate Speech

![Stop](https://github.com/malteserteresa/stop-it/blob/master/images/test.png)

A tool to help people avoid online sexual harassment by filtering out unwanted comments from Facebook or Twitter.

                                                             
## Setup requirements

1. [Download Anaconda](https://www.anaconda.com/distribution/#download-section)
2. Install Anaconda using the [guide for your operating system](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html#regular-installation)
3. To create an environment in conda run: `conda create --name stop-it tensorflow keras numpy pandas flask matplotlib scikit-learn pytest`

## Usage
In a Terminal, run the command: `python model.py`

Or using flask, run: `python deploy.py`
And in the browser go to [127.0.0.1:5000/predict?sentence=your sentence to analyse](http://127.0.0.1:5000/predict?sentence=your sentence to analyse). Be sure to include spaces in the sentences. Spaces can be explicity set using the UTF-8 encoded `%20`.

To work on the browser extension run:
```
cd extension 
npm install
```

And to run the test:
```
npm test
```

## Further info

For further details about the project and topic as a whole, please see the wiki

- The Problem : Outlines the issue
- The Solution : Describes the browser extension that we are aiming to build and it's target functionality 
- Flow in TensorFlow : The current workings of the model
- The Language of Misogyny and Sexual Aggression : A discussion of the language of cyber sexual harassment/sexist hate speech and the surrounding literature

Icons from : http://www.aha-soft.com/iconsets.htm
