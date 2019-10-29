const restoreOptions = require('./reset');

describe('test reset options function of popup code', () => {
  const defaultId = 'text_crossed';
  const selector = `#${defaultId}`;

  beforeEach(async () => {
    // add input to select
    document.body.innerHTML = `<input type="radio" id="${defaultId}" >`;
  });

  // test using WebExtension mock
  it('reset should call browser storage API', () => {
    restoreOptions();
    expect(browser.storage.sync.get).toHaveBeenCalled();
  });

  it('reset should select the default option', async () => {
    const input = document.querySelector(selector);
    // mock storage should be empty, so reset should select the default option
    expect(input.checked).toBe(false);
    await restoreOptions();
    expect(input.checked).toBe(true);
  });

  // TODO: Add test for selecting a different case than the default
});
