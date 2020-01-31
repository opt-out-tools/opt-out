import styleTweet from './styleTweet';

/**
 * @description function which calls server for given node, and depending on the response,
 * applies pre-defined action
 * @param node
 * @param selector
 * @param popupPrefs
 */
export default (node, selector, popupPrefs) => {
  node.classList.add('processing');
  console.log('Sending Request');
  const link = 'https://api.optoutools.com/predict';
  const xhr = new XMLHttpRequest();
  const tweetTextNode = node.querySelector(
    `${selector} > div ~ div > div ~ div`
  );
  xhr.open('POST', link, true);
  xhr.setRequestHeader('Content-type', 'application/json;charset=UTF-8');
  xhr.withCredentials = true;
  xhr.onreadystatechange = (e) => {
    if (xhr.readyState !== 4) {
      return;
    }
    if (xhr.status === 200) {
      const prediction = Number(JSON.parse(xhr.response).predictions[0]);
      console.log(
        'Response received as ', prediction);
      // eslint-disable-next-line no-constant-condition
      if (prediction) {
        node.classList.add('processed-true');
        tweetTextNode.setAttribute('data-prediction', prediction.toString());
        styleTweet(tweetTextNode, popupPrefs);
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
      texts: [tweetTextNode.innerText]
    })
  );
};
