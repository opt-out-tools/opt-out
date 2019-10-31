let selector;
let option = 'text_crossed';
let slider = '1';

function updateOption(result) {
  option = result.optOut.selector;
  slider = result.optOut.slider;
}

function onError(error) {
  console.log(`Error: ${error}`);
}
browser.storage.sync.get('optOut').then(updateOption, onError);


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
const styleTweet = function (element, selectedOption, sliderValue) {
  if ((selectedOption === 'text_white') && (sliderValue === '1')) element.classList.add('opt-out-tw');
  else element.classList.remove('opt-out-tw');
  if ((selectedOption === 'text_crossed') && (sliderValue === '1')) element.classList.add('opt-out-tc');
  else element.classList.remove('opt-out-tc');
  if ((selectedOption === 'text_removed') && (sliderValue === '1')) element.classList.add('opt-out-trem');
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
        styleTweet(tweetText, option, slider);
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
browser.runtime.onMessage.addListener((message) => {
  if ((option !== message.selector) || (slider !== message.slider)) {
    option = message.selector;
    slider = message.slider;
    const posts = document.querySelectorAll('.processed-true');
    posts.forEach((post) => {
      const tweetText = post.querySelector(
        `${selector} > div ~ div > div ~ div`,
      ); // selecting text inside tweet
      styleTweet(tweetText, option, slider);
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
