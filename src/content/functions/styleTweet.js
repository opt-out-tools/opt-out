import { TWEET_CLASSES } from '../constants';

/**
 * @description Sets display classes to tweet nodes when the text has been predicted
 * to be misogynist and when the options are set to block misogynist content.
 */
export default function (element, popupPrefs) {
  element.classList.remove(...Object.values(TWEET_CLASSES));
  const tweetPredictionValue = parseFloat(element.dataset.prediction);
  const modifyTweetThreshold = parseFloat(popupPrefs.sliderVal);
  if (
    // Tweet is predicted to be misogynist
    tweetPredictionValue !== 0 &&
    // Option to modify tweet is turned on
    modifyTweetThreshold !== 0 &&
    // Tweets prediction value is enough to modify
    tweetPredictionValue >= modifyTweetThreshold &&
    // unill jest setup for null coalescing opeartor is added
    TWEET_CLASSES[popupPrefs.optionVal] !== undefined
  ) {
    element.classList.add(TWEET_CLASSES[popupPrefs.optionVal] ?? '');
    // TODO: replace with element.classList.add(TWEET_CLASSES[popupPrefs.optionVal] ?? '');
  }
}
