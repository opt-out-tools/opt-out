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
  // eslint-disable-next-line no-unused-vars
  const reqBody = { texts: [text] };

  /**
   * @description gets prediction array from response object and returns predictions values array by
   * converting them to number from boolean, string or number
   * @param body
   * @returns {number[]}
   */
  // eslint-disable-next-line no-unused-vars
  function getPredictions (body) {
    if (body.predictions.isArray) {
      return body.predictions.map(x => Number(x));
    }

    // eslint-disable-next-line no-unused-vars
    function styleTweetsToPrediction (predictions) {
      predictions.map(predictionInt => {
        tweetTextNode.setAttribute('data-prediction', predictionInt.toString());
        styleTweet(tweetTextNode, popupPrefs);
        return 'processed-true';
      }

      );
    }
  }

  // eslint-disable-next-line no-unused-vars
  function applyResults (processingResults) {
    // TODO; Go over array and apply results
    node.classList.remove('processing');
    node.classList.add('processed-true');
  }
};

// eslint-disable-next-line no-undef
postData(OPT_OUT_API_URL, reqBody)
  // eslint-disable-next-line no-undef
  .then(getPredictions)
  // eslint-disable-next-line no-undef
  .then(styleTweetsToPrediction)
  // eslint-disable-next-line no-undef
  .then(applyResults);

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
    .then(handleErrors)
    .then(handleResponse)
    .catch(err => {
      console.error(err);
    });
  return response.json();
}
