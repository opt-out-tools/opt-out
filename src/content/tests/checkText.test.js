import fetchMock from 'fetch-mock';

import checkText from '../functions/checkText';
import { SELECTOR_ONLINE_TWEET, OPT_OUT_API_URL } from '../constants';

fetchMock.config.overwriteRoutes = true;

describe('checkText.js', () => {
  let popupPrefs;
  let element;
  let tweetText;
  let error;

  beforeEach(() => {
    // Since errors in logs
    error = jest.spyOn(console, 'error').mockImplementation(() => {});

    // Clear fetch history
    fetchMock.resetHistory();

    popupPrefs = {
      sliderVal: 1,
      optionVal: 'text_removed',
    };

    // Create dom element
    document.body.innerHTML = `
      <div id='testElement'>
        <div class="tweet" data-testid="tweet">
            <div>
              <div></div> 
              <div></div>
            </div>
            <div>
              <div></div>
              <div id="tweetText">I'm here and I'm queer</div>
            </div>
        </div>
      </div>
    `;

    // Set tweet text to innerText in dom
    element = document.getElementById('testElement');
    tweetText = document.getElementById('tweetText');
    tweetText.innerText = tweetText.innerHTML;
  });

  test('check that the fetch API fired with correct body', async () => {
    fetchMock.postOnce(OPT_OUT_API_URL, {
      status: 200,
      body: {},
    });

    checkText(element, SELECTOR_ONLINE_TWEET, popupPrefs);

    // Calls API
    expect(fetchMock.called(OPT_OUT_API_URL)).toBe(true);
    expect(fetchMock.calls().length).toBe(1);
    // Includes correct request body
    expect(JSON.parse(fetchMock.lastOptions(OPT_OUT_API_URL).body)).toEqual({
      texts: ["I'm here and I'm queer"],
    });
  });

  test('check proccessing state applied during api resolution and removed after', async () => {
    fetchMock.postOnce(OPT_OUT_API_URL, {
      status: 200,
      body: { texts: ['Error!'] },
    });

    // Check text function
    checkText(element, SELECTOR_ONLINE_TWEET, popupPrefs);

    // Expect processing state to be applied
    expect(element.classList.contains('processing')).toEqual(true);

    // Resolve the response
    await fetchMock.flush();

    // Expect processing state to be removed
    expect(element.classList.contains('processing')).toEqual(false);
  });

  test('on error response, log error and apply correct state to tweet', async () => {
    fetchMock.postOnce(OPT_OUT_API_URL, {
      status: 400,
      body: { texts: ['This is bad, man'] },
    });

    // Check text function
    checkText(element, SELECTOR_ONLINE_TWEET, popupPrefs);
    // Resolve the response
    await fetchMock.flush();

    expect(error).toHaveBeenCalled();
  });

  test('on success response with no prediction, apply correct state to tweet', async () => {
    fetchMock.postOnce(OPT_OUT_API_URL, {
      status: 200,
      body: { predictions: [] },
    });

    // Check text function
    checkText(element, SELECTOR_ONLINE_TWEET, popupPrefs);
    // Resolve the response
    await fetchMock.flush();

    // Expect processed state to be false
    expect(element.classList.contains('processed-false')).toEqual(true);
  });

  test('on success response with true prediction, apply correct state to tweet', async () => {
    fetchMock.postOnce(OPT_OUT_API_URL, {
      status: 200,
      body: { predictions: [true] },
    });

    // Check text function
    checkText(element, SELECTOR_ONLINE_TWEET, popupPrefs);
    // Resolve the response
    await fetchMock.flush();

    // Expect processed state to be false
    expect(element.classList.contains('processed-true')).toEqual(true);
  });
});
