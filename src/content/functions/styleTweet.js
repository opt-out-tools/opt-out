/**
 * @description Sets display classes to tweet nodes when the text has been predicted
 * to be misogynist and when the options are set to block misogynist content.
 */
export default function (element, popupPrefs) {
  element.classList.remove('opt-out-tw', 'opt-out-tc', 'opt-out-trem');
  const tweetPredictionValue = parseFloat(element.dataset.prediction);
  const modifyTweetThreshold = parseFloat(popupPrefs.sliderVal);
  if (
    // Tweet is predicted to be misogynist
    tweetPredictionValue !== 0 &&
    // Tweets prediction value is enough to modify
    tweetPredictionValue >= modifyTweetThreshold
  ) {    
    switch (popupPrefs.optionVal) {
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
}
