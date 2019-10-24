const restoreOptions = require('./reset');

describe('test popup code', () => {
  let fakeGet;
  let fakeBrowser;
  beforeEach(async () => {
    // fake the browser
    fakeGet = jest.fn((text) => text);
    fakeBrowser = { storage: { sync: { get: fakeGet } } };
    global.browser = fakeBrowser;

    // add elements to select
    document.body.innerHTML = '<div id="text_crossed"></div>';

    // wait a tick to give the production code the chance to execute
    return new Promise((resolve) => process.nextTick(resolve));
  });

  it(' restoreOption should call browser.storage.sync.get once', () => {
    restoreOptions();
    expect(fakeGet.mock.calls.length).toBe(1);
  });

  it('should call browser API', () => {
    restoreOptions();
    expect(browser.storage.sync.get).toHaveBeenCalled();
  });
});
