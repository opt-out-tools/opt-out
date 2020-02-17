import styleTweet from './functions/styleTweet';
import processTweets from './functions/processTweets';
import onError from './functions/onError';
import updateOption from './functions/updateOption';

const bodyColor = window.getComputedStyle(document.body, null).getPropertyValue('background-color');
const root = document.getElementById('doc') || document.getElementById('react-root');
const selector = (document.querySelector('body').classList.contains('logged-out')) ? '.tweet' : '[data-testid="tweet"]';
const checkTweetListObserver = new MutationObserver(
  (mutationsList) => {
    mutationsList.forEach((mutation) => {
      if (mutation.type === 'childList') {
        processTweets(selector, popupPrefs); // TODO: add Mutation Record to be used instead of document.querySelectorAll(selector)
      }
    });
  }
);

let popupPrefs = {
  optionVal: 'text_crossed',
  sliderVal: '1'
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
    popupPrefs = popupSettings;
    const posts = document.querySelectorAll('.processed-true');
    posts.forEach((post) => {
      const tweetText = post.querySelector(
        `${selector} > div ~ div > div ~ div`
      );
      styleTweet(tweetText, popupPrefs);
    });
  }
});

/**
 * Starts observer which will process every new Tweet added to the DOM
 */
checkTweetListObserver.observe(root, { childList: true, subtree: true });
