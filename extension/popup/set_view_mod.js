import restoreOptions from './reset';

const slider = document.getElementById('slider');

/**
 * There was an error executing the script.
 * Display the popup's error message, and hide the normal UI.
 */
function reportExecuteScriptError(error) {
  document.querySelector('#popup-content').classList.add('hidden');
  document.querySelector('#error-content').classList.remove('hidden');
  console.error(`Failed to execute opt-out content script: ${error.message}`);
}

function listenForClicks() {
  function setChecks(tabs) {
    let msg = 'tc';
    if (document.getElementById('text_white').checked) msg = 'tw';
    if (document.getElementById('text_crossed').checked) msg = 'tc';
    if (document.getElementById('text_removed').checked) msg = 'tr';

    browser.storage.sync.set({ style: msg });

    browser.tabs.sendMessage(tabs[0].id, {
      command: slider.value < 0.5 ? [] : [msg],
    });
  }

  function reportError(error) {
    console.error(`Could not opt-out: ${error}`);
    reportExecuteScriptError(error);
  }

  browser.tabs
    .query({ active: true, currentWindow: true })
    .then(setChecks)
    .catch(reportError);
}

/**
 * When the popup loads, inject a content script into the active tab,
 * and add a click handler.
 * If we couldn't inject the script, handle the error.
 */
document.addEventListener('DOMContentLoaded', restoreOptions);
document.addEventListener('click', listenForClicks);

slider.addEventListener('input', (evt) => {
  if (evt.target.value < 1) {
    slider.classList.add('slider-angry');
  } else {
    slider.classList.remove('slider-angry');
  }
});
