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
  });
  describe('browser.runtime.onMessage.addListener event listener', () => {
    it('styles a tweet that has the class .processed-true', () => {
      document.body.innerHtml = `
        <div data-testid="tweet">
          <h1>Oh ya!</h1>
        </div>
      `;
    });
  });
});
