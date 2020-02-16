import { OPT_OUT_API_URL } from './constants';

let selector;
let option = 'text_crossed';
let slider = '1';
const bodyColor = window.getComputedStyle(document.body, null).getPropertyValue('background-color');
document.documentElement.style
  .setProperty('--color', bodyColor);

const root = document.getElementById('doc') || document.getElementById('react-root');

if (document.querySelector('body').classList.contains('logged-out')) {
  console.log('offline');
  selector = '.tweet';
} else {
  console.log('online');
  selector = '[data-testid="tweet"]';
}
/**
 * @description Updates `option` and `slider` depending on the given result
 * @param result
 */
const updateOption = (result) => {
  option = result.optOut.selector;
  slider = result.optOut.slider;
};

/**
 * @description Function handles errors.
 * @param error
 */
const onError = (error) => {
  console.error(`Error: ${error}`);
};

/**
 * @description Depending on `option` sets classes to tweet nodes
 */
const styleTweet = (element, selectedOption, sliderValue) => {
  const tweetPredictionValue = parseFloat(element.dataset.prediction);
  const hideThreshold = parseFloat(sliderValue);
  element.classList.remove('opt-out-tw', 'opt-out-tc', 'opt-out-trem');
  if (
    tweetPredictionValue !== 0 &&
    tweetPredictionValue <= hideThreshold
  ) {
    switch (selectedOption) {
      case 'text_white':
        element.classList.add('opt-out-tw');
        break;
      case 'text_crossed':
        element.classList.add('opt-out-tc');
        break;
      case 'text_removed':
        element.classList.add('opt-out-trem');
        break;
    }
  }
};

/**
 * @description function which calls server for given node, and depending on the response,
 * applies pre-defined action
 * @param node
 */
const checkText = (node) => {
  node.classList.add('processing');

  // Get text for req
  const tweetTextNode = node.querySelector(
    `${selector} > div ~ div > div ~ div`
  );
  const text = tweetTextNode.innerText;
  const reqBody = { texts: [text] };

  const reqHeaders = new Headers();
  reqHeaders.set('Content-type', 'application/json;charset=UTF-8');

  fetch(OPT_OUT_API_URL, {
    method: 'POST',
    headers: reqHeaders,
    body: JSON.stringify(reqBody),
    mode: 'cors'
  })
    .then(response => {
      // If successful response
      if (response.ok) {
        // Parse body json
        response.json().then(body => {
          const predictions = body.predictions;
          // If response contains prediction
          if (predictions && predictions.length > 0) {
            // Convert prediction state to int
            const predictionInt = Number(predictions[0]);
            // Add processing status and prediction to tweet node
            node.classList.add('processed-true');
            tweetTextNode.setAttribute(
              'data-prediction',
              predictionInt.toString()
            );
            styleTweet(tweetTextNode, option, slider);
          } else {
            // If no prediction
            node.classList.add('processed-false');
          }
        });
      } else {
        console.log('Failed response: ', response);
      }
      // Remove processing state from tweet
      node.classList.remove('processing');
    })
    .catch(err => {
      // Remove processing state from tweet
      node.classList.remove('processing');
      console.log(err);
    });
};

/**
 * @description get every tweet and process unprocessed ones.
 */
const processTweets = () => {
  const posts = document.querySelectorAll(selector); // selecting tweet object
  posts.forEach((post) => {
    if (post.classList.contains('processed-true')) return;
    if (post.classList.contains('processed-false')) return;
    if (post.classList.contains('processing')) return;
    checkText(post);
  });
};

/**
 * @description for every change in DOM run processTweets
 * @param mutationsList
 */
const checkTweetList = (mutationsList) => {
  mutationsList.forEach((mutation) => {
    if (mutation.type === 'childList') {
      processTweets();
    }
  });
};

const checkTweetListObserver = new MutationObserver(checkTweetList);

// MAIN FUNCTION

browser.storage.sync.get('optOut').then(updateOption, onError);
/**
 * Adds listener which on new message received from popup goes over tweets and applies new style
 */
browser.runtime.onMessage.addListener((message) => {
  if ((option !== message.selector) || (slider !== message.slider)) {
    option = message.selector;
    slider = message.slider;
    const posts = document.querySelectorAll('.processed-true');
    posts.forEach((post) => {
      const tweetText = post.querySelector(
        `${selector} > div ~ div > div ~ div`
      );
      styleTweet(tweetText, option, slider);
    });
  }
});

checkTweetListObserver.observe(root, { childList: true, subtree: true });
