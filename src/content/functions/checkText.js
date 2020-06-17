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

function handleResponse (response) {
  return response;
}

// eslint-disable-next-line no-undef
const handleRepsponseOrError = compose(handleErrors, handleResponse);

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
  postData(OPT_OUT_API_URL, reqBody).then(body => {
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
      styleTweet(tweetTextNode, popupPrefs);
    } else {
      // If no prediction
      node.classList.add('processed-false');
    }
    node.classList.remove('processing');
  });
};

async function postData (url = '', data = {}) {
  const response = await fetch(url, {
    method: 'POST',
    mode: 'cors',
    credentials: 'include',
    headers: {
      'Content-Type': 'application/json;charset=UTF-8',
      'Access-Control-Allow-Origin': '*'
    },
    body: JSON.stringify(data)
  })
    .then(handleRepsponseOrError)
    .catch(err => {
      return {
        error: err
      };
    });
  return response.json();
}
