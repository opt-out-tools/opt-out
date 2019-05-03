var jsdom = require('mocha-jsdom')
const {expect} = require('chai');
const {
  getTweet,
  getSentimentScore,
  modifyHatefulTweet

} = require('../src/replace');

describe('replace', () => {

    jsdom()

    describe('Find elements containing tweets and replace them with something else.', () => {
      it('returns a tweet', () => {
        var div = document.createElement('div')
        expect(div.nodeName).to.equal('DIV')
        expect(getTweet()).to.equal();
        expect(getTweet()).to.equal();
      });
      it('returns a score', () => {
        expect(getSentimentScore()).to.equal();
        expect(getSentimentScore()).to.equal();
      });
      it('returns a the modified text', () => {
        expect(modifyHatefulTweet()).to.equal();
        expect(modifyHatefulTweet()).to.equal();
      });
    } ) } )