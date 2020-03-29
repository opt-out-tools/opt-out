import styleTweet from '../functions/styleTweet';

describe('styleTweet.js', () => {
  describe('styleTweet', () => {
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
        <div id="testElement">
          I'm gay.
        </div>
      `;
      element = document.getElementById('testElement');
      // Is 100% misogynist
      element.setAttribute('data-prediction', '1');
    });

    it('applies class to element when tweet prediction value above display threshold', () => {
      styleTweet(element, popupPrefs);
      expect(element.classList.contains('opt-out-trem')).toBe(true);
    });

    it('does not apply class to element when tweet prediction value below display threshold', () => {
      document.body.innerHTML = `
        <div id="testElement"></div>
      `;
      element = document.getElementById('testElement');
      // Is 50% misogynist
      element.setAttribute('data-prediction', '0.5');

      styleTweet(element, {
        // Show all tweets predicted misogynist
        sliderVal: 1,
        optionVal: 'text_removed',
      });
      expect(element.classList.contains('opt-out-trem')).toBe(false);
    });

    it('removes existing class from element when tweet prediction value below display threshold', () => {
      // Create dom element
      document.body.innerHTML = `
        <div id="testElement" class='opt-out-trem'></div>
      `;
      element = document.getElementById('testElement');
      // Is 50% misogynist
      element.setAttribute('data-prediction', '0.5');

      styleTweet(element, {
        // Show all tweets predicted misogynist
        sliderVal: 1,
        optionVal: 'text_removed',
      });
      expect(element.classList.contains('opt-out-trem')).toBe(false);
    });
  });
});
