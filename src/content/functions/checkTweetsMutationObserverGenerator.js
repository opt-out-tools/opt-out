import processTweets from './processTweets';

const checkTweetsMutationObserverGenerator = (tweetSelector, popupPrefs) => {
  const checkTweetList = mutationsList => {
    mutationsList.forEach(mutation => {
      if (mutation.type === 'childList') {
        if (mutation.addedNodes.length > 0) {
          console.log(tweetSelector);

          processTweets(tweetSelector, popupPrefs);
          console.log(processTweets);
        }
      }
    });
  };
  const observer = new MutationObserver(checkTweetList);
  return observer;
};

export default checkTweetsMutationObserverGenerator;
