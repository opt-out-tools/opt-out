const jsdom = require('jsdom');

describe('opt-out-ext.js', () => {
  let newWindow;
  beforeAll(() => {
    // Mock out MutationObserver
    global.MutationObserver = class {
      constructor (callback) { return true; }
      disconnect () {}
      observe (element, initObject) {}
    };

    // Create page
    newWindow = new jsdom.JSDOM(`
      <!DOCTYPE html>
      <html>
        <body>
          <div data-testid="tweet">
            <h1>Oh ya!</h1>
          </div>
          <div data-testid="tweet" class="processed-true">
            <h1>Oh ya!</h1>
          </div>
        </body>
      </html>
    `, {
      resources: 'usable',
      runScripts: 'dangerously'
    }).window;
    newWindow.eval(require('../opt-out-ext.js'));
  });
  describe('browser.runtime.onMessage.addListener event listener', () => {
    describe('message created from popup', () => {
      it('when new text format option configured, applies the correct class to tweets', () => {
        // Send message
        browser.runtime.sendMessage({
          selector: 'text_removed',
          slider: '1'
        });
        // Check that document.body HTML has changed some tweets
        expect(newWindow.document.body).toMatchSnapshot();
      });
    });
  });
});
