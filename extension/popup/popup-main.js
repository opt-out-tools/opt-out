import updateOptions from './functions/updateOptions.js';
import onError from './functions/onError.js';
import updateSliderKnob from './functions/updateSliderKnob.js';

/**
 * @description get input values, send them to storage and send message for update to background
 * script
 * @param tabs
 */
function setChecks(tabs) {
  const slider = document.getElementById('slider');
  const optionValue = document.querySelector('input[name="text_options"]:checked').value || 'tc';
  const popupSettings = {
    slider: slider.value,
    selector: optionValue,
  };

  updateSliderKnob(slider);
  browser.storage.sync.set({ optOut: popupSettings });
  browser.tabs.sendMessage(tabs[0].id, popupSettings);
}

/**
 * When the popup loads, inject a content script into the active tab,
 * and add a click handler.
 * If we couldn't inject the script, handle the error.
 */
document.addEventListener('DOMContentLoaded', browser.storage.sync.get('optOut').then(updateOptions, onError));
document.addEventListener('input', () => {
  browser.tabs
    .query({
      active: true,
      url: 'https://twitter.com/*',
      currentWindow: true,
    })
    .then(setChecks, onError);
});
