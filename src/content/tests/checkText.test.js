import checkText from '../functions/checkText';
import {
  SELECTOR_ONLINE_TWEET,
  OPT_OUT_API_URL
} from '../constants';

const fetchMock = require("fetch-mock");
fetchMock.mock(OPT_OUT_API_URL, 200);

describe('checkText.js', () => {
  let popupPrefs;
  let element;

  beforeEach(() => {

    popupPrefs = {
      // Show no tweets predicted misogynist
      sliderVal: 0.1,
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
    element = document.getElementById('testElement');
    tweetText = document.getElementById('tweetText');
    tweetText.innerText = tweetText.innerHTML;

  });

  test('check that the fetch API fired', () => {
    checkText(element, SELECTOR_ONLINE_TWEET, popupPrefs);
    expect(fetchMock.called(OPT_OUT_API_URL)).toBe(true);
    expect(fetchMock.calls().length).toBe(1);
    expect(JSON.parse(fetchMock.lastOptions(OPT_OUT_API_URL)['body'])).toEqual({texts: ["I'm here and I'm queer"]});
  });
});


