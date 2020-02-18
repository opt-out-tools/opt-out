import styleTweet from './styleTweet';
import { OPT_OUT_API_URL } from '../constants';

/**
 * @description throws new error if response is not in 200-299 range
 * @param response
 * @returns {{ok}|*}
 */
function handleErrors (response) {
  if (!response.ok) {
    let errorText;
    response.json().then(body => {
      errorText = body.texts[0];
      console.error(response.statusText + ' -> ' + errorText);
    });
    throw Error(response.statusText);
  }
  return response;
}

/**
 * @description function which calls server for given node, and depending on the response,
 * applies pre-defined action
 * @param node
 * @param selector
 * @param popupPrefs
 */
export default (node, selector, popupPrefs) => {
  node.classList.add('processing');
  // Get text for req
  const tweetTextNode = node.querySelector(
    `${selector} > div ~ div > div ~ div`
  );
  const text = tweetTextNode.innerText;
  const reqBody = { texts: [text] };
  fetch(OPT_OUT_API_URL, {
    method: 'POST',
    mode: 'cors',
    credentials: 'include',
    headers: {
      'Content-Type': 'application/json;charset=UTF-8',
      'Access-Control-Allow-Origin': '*'
    },
    body: JSON.stringify(reqBody)
  })
    .then(handleErrors)
    .then(response => {
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
          if (body.texts[0]) {
            console.error('error ->' + body.texts[0]);
            console.log('text given -> ', tweetTextNode);
          }
          styleTweet(tweetTextNode, popupPrefs);
        } else {
          // If no prediction
          node.classList.add('processed-false');
        }
      });
      // Remove processing state from tweet
      node.classList.remove('processing');
    })
    .catch(err => {
      // Remove processing state from tweet
      node.classList.add('processed-false');
      node.classList.remove('processing');
      console.error(err, node);
    });
};
