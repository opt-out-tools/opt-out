import styleTweet from './functions/styleTweet';
import processTweets from './functions/processTweets';
import onError from './functions/onError';
import updateOption from './functions/updateOption';
import {
  SELECTOR_ONLINE_ROOT,
  SELECTOR_OFFLINE_ROOT,
  SELECTOR_ONLINE_TWEET,
  SELECTOR_OFFLINE_TWEET
} from './constants';

/**
 * @description Setting up constants for further use
 * @type {string}
 */
const bodyColor = window.getComputedStyle(document.body, null).getPropertyValue('background-color');
const root = document.getElementById(SELECTOR_OFFLINE_ROOT) || document.getElementById(SELECTOR_ONLINE_ROOT);
const tweetSelector = (document.querySelector('body').classList.contains('logged-out')) ? SELECTOR_OFFLINE_TWEET : SELECTOR_ONLINE_TWEET;

/**
 * @description Defining default values for user preferences
 * @type {popupPrefs}
 */
let popupPrefs = {
  optionVal: 'text_crossed',
  sliderVal: '0'
};

/**
 * @description for every node added to the DOM, run processTweets
 * @type {MutationObserver}
 */
const checkTweetList = (mutationsList) => {
  mutationsList.forEach((mutation) => {
    if (mutation.type === 'childList') {
      if (mutation.addedNodes.length > 0) {
        processTweets(tweetSelector, popupPrefs);
      }
    }
  });
};


/**
 * Setting preferences color to match twitter body color
 */
document.documentElement.style.setProperty('--color', bodyColor);

/**
 * Syncing contentScript preferences if already predefined in storage
 */
browser.storage.sync.get('optOut').then(result => { popupPrefs = updateOption(result, popupPrefs); }, onError);

/**
 * Adds listener which upon receiving new preferences from popup goes over processed tweets and changes applied class
 * TODO: optimization: instead of replacing class, modify style in css using variables or browser.tabs.insertCSS API
 */
browser.runtime.onMessage.addListener((popupSettings) => {
  if (popupPrefs !== popupSettings) {
    popupPrefs = updateOption(popupSettings, popupPrefs);
    const posts = document.querySelectorAll('.processed-true');
    posts.forEach((post) => {
      const tweetText = post.querySelector(
        `${tweetSelector} > div ~ div > div ~ div`
      );
      styleTweet(tweetText, popupPrefs);
    });
  }
});

/**
 * Starts observer which will trigger styling observers for addition of tweets to TweetList
 */
const checkTweetListObserver = new MutationObserver(checkTweetList);
checkTweetListObserver.observe(root, { childList: true, subtree: true });
