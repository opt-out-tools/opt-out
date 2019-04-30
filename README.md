
![Stop](https://github.com/malteserteresa/stop-it/blob/master/images/icon.png)

## Sexual Harassment and Sexist Hate Speech Online

### What is it?

We're glad you asked. Sexual harassment and sexist hate speech online are mentioned in international law documents such as the Committee on the Elimination of Discriminationagainst Women declaration, a committee within the UN. They describe these behaviours as acts of **gender based violence happening online and in technology-mediated spaces.**

### What's this project doing about this?

Here is a tool to help people defend themselves on Facebook or Twitter.


                                                             
### Installation requires:
`tensorflow 1.12.2,
keras 2.2.4, 
numpy,
pandas,
flask,
matplotlib,
scikit-learn`

We recommend you install anaconda to handle these package and run the command below to create an 
To create an environment in conda run: 
`conda create --name stop-it tensorflow keras numpy pandas flask matplotlib scikit-learn pytest`

### Usage:
`python model.py`

or via the browser

`python deploy.py`

127.0.0.1:5000/predict?sentence="your sentence to analyse" (without quotation marks). 

Be sure to include spaces in the senteces. Spaces can be explicity set using the UTF-8 encoded "%20".

To work on the browser extension run:
`cd extension 
npm install`

And to run the test:
`npm test`

For further details about the project and topic as a whole, please see the wiki

- The Problem : Outlines the issue
- The Solution : Describes the browser extension that we are aiming to build and it's target functionality 
- Flow in TensorFlow : The current workings of the model
- The Language of Misogyny and Sexual Aggression : A discussion of the language of cyber sexual harassment/sexist hate speech and the surrounding literature

Icons from : http://www.aha-soft.com/iconsets.htm
