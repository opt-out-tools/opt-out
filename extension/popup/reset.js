const selectorLookup = {
  tw: '#text_white',
  tc: '#text_crossed',
  tr: '#text_removed',
};

const defaultStyle = 'tc';

async function restoreOptions() {
  try {
    const { style } = await browser.storage.sync.get('style');
    const selector = selectorLookup[style] || selectorLookup[defaultStyle];
    document.querySelector(selector).click();
  } catch (error) {
    console.log(`Error: ${error}`);
  }
}

module.exports = restoreOptions;
