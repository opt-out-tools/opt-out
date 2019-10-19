let selector;
let option = 'tw';

const root = document.getElementById('doc') || document.getElementById('react-root');

if (document.querySelector('body').classList.contains('logged-out')) {
  console.log('offline');
  selector = '.tweet';
} else {
  console.log('online');
  selector = '[data-testid="tweet"]';
}

/*
Depending on `option` sets classes to tweet nodes
 */
const styleTweet = function (element, selectedOption) {
  if (selectedOption.includes('tw')) element.classList.add('opt-out-tw');
  else element.classList.remove('opt-out-tw');
  if (selectedOption.includes('tc')) element.classList.add('opt-out-tc');
  else element.classList.remove('opt-out-tc');
  if (selectedOption.includes('tr')) element.classList.add('opt-out-trem');
  else element.classList.remove('opt-out-trem');
};

/*
function which calls server for given node, and depending on the response,
applies pre-defined action
 */
const checkText = function (node) {
  console.log('Sending Request');
  const link = 'https://api.optoutools.com/predict';
  const xhr = new XMLHttpRequest();
  xhr.open('POST', link, true);
  xhr.setRequestHeader('Content-type', 'application/json;charset=UTF-8');
  xhr.withCredentials = true;
  xhr.onreadystatechange = function (e) {
    if (xhr.readyState !== 4) {
      return;
    }
    if (xhr.status === 200) {
      console.log(
        'Response received as ',
        JSON.parse(xhr.response).predictions[0],
      );
      if (JSON.parse(xhr.response).predictions[0]) {
        node.classList.add('processed-true');
        const tweetText = node.querySelector(
          `${selector} > div ~ div > div ~ div`,
        );
        styleTweet(tweetText, option);
      } else {
        node.classList.add('processed-false');
      }
    } else {
      console.error(e);
      console.log('Failed response', xhr);
    }
  };
  xhr.send(
    JSON.stringify({
      texts: [node.innerText],
    }),
  );
};

/*
 * Predefines action and changes it depending on user action
 */
// disable eslint error for browser
// eslint-disable-next-line no-undef
browser.runtime.onMessage.addListener((message) => {
  if (option !== message.command) {
    option = message.command;
    const posts = document.querySelectorAll('.processed-true');
    posts.forEach((post) => {
      const tweetText = post.querySelector(
        `${selector} > div ~ div > div ~ div`,
      ); // selecting text inside tweet
      styleTweet(tweetText, option);
    });
  }
});

const processTweets = function () {
  const posts = document.querySelectorAll(selector); // selecting tweet object
  posts.forEach((post) => {
    if (post.classList.contains('processed-true')) return;
    if (post.classList.contains('processed-false')) return;
    checkText(post);
  });
};

const checkTweetList = function (mutationsList) {
  mutationsList.forEach((mutation) => {
    if (mutation.type === 'childList') {
      processTweets();
    }
  });
};
const checkTweetListObserver = new MutationObserver(checkTweetList);
checkTweetListObserver.observe(root, { childList: true, subtree: true });
