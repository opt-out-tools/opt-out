
![Stop](https://github.com/malteserteresa/stop-it/blob/master/images/icon.png)

## Sexual Harassment and Sexist Hate Speech Online

### What is it?

We're glad you asked. In international law these behaviours are described as acts of **gender based violence** happening **online** and **in technology-mediated spaces** that inflict **physical, mental or sexual harm or suffering, threats of such acts, coercion** and **other deprivations of liberty.**[1](https://tbinternet.ohchr.org/Treaties/CEDAW/Shared%20Documents/1_Global/CEDAW_C_GC_35_8267_E.pdf) This is a global tragedy affecting the well-being, economical potential and representation of women.

We advise you check out these two things next. 
- [Random Rape Threat Generator](https://www.rapeglish.com/)
- [The Problem](https://github.com/malteserteresa/stop-it/wiki/The-Problem)

The first link is a random rape threat generator. This will give you a sense of the content we are trying to protect against. This was built by Emma Jane and Nicole A Vincent and gives examples of the internet language called Rapeglish. Warning, it's extreme language.

The second link is our own research into this subject.

### What's this project doing about this?

We hope to develop a tool to help people protect themselves on Facebook or Twitter.
- [The Solution](https://github.com/malteserteresa/stop-it/wiki/The-Solution)
- [Current Design](https://github.com/malteserteresa/stop-it/wiki/Current-Design)

The first link is an in-depth description of the browser extension we are hoping to build. The second link is the current implementaiton details.
                                                             
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

Icons from : http://www.aha-soft.com/iconsets.htm
