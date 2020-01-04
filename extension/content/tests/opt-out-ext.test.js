// Mock out MutationObserver
global.MutationObserver = class {
  constructor (callback) { return true; }
  disconnect () {}
  observe (element, initObject) {}
};

describe('opt-out-ext.js', () => {
  beforeAll(() => {
    // Import file, loading listeners in to browser
    require('../opt-out-ext');

    // Create page
    document.body.innerHtml = `
      <div data-testid="tweet">
        <h1>Oh ya!</h1>
      </div>
    `;
  });
  describe('browser.runtime.onMessage.addListener event listener', () => {
    describe('when message created from popup', () => {
      it('when new text format option configured, applies the correct class to tweets', () => {
        // Send message
        browser.runtime.sendMessage({
          selector: 'text_removed',
          slider: '1'
        });
      });
    });
  });
});
