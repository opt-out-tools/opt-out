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
    let msg = [];
    if (document.getElementById('text_white').checked) {
      msg.push('tw');
    }
    if (document.getElementById('text_crossed').checked) {
      msg.push('tc');
    }
    if (document.getElementById('text_removed').checked) {
      msg.push('tr');
    }
    msg = msg.join();
    // disable eslint error for browser
    // eslint-disable-next-line no-undef
    browser.storage.sync.set({ style: msg });
    // eslint-disable-next-line no-undef
    browser.tabs.sendMessage(tabs[0].id, {
      command: msg,
    });
  }

  function reportError(error) {
    console.error(`Could not opt-out: ${error}`);
    reportExecuteScriptError(error);
  }

  // eslint-disable-next-line no-undef
  browser.tabs
    .query({ active: true, currentWindow: true })
    .then(setChecks)
    .catch(reportError);
}

function restoreOptions() {
  function setCurrentChoice(result) {
    document.querySelector('#text_white').checked = result.style
      .split(',')
      .includes('tw');
    document.querySelector('#text_crossed').checked = result.style
      .split(',')
      .includes('tc');
    document.querySelector('#text_removed').checked = result.style
      .split(',')
      .includes('tr');
  }

  function onError(error) {
    console.log(`Error: ${error}`);
  }

  // disable eslint error for browser
  // eslint-disable-next-line no-undef
  const getting = browser.storage.sync.get('style');
  getting.then(setCurrentChoice, onError);
}

/**
 * When the popup loads, inject a content script into the active tab,
 * and add a click handler.
 * If we couldn't inject the script, handle the error.
 */
document.addEventListener('DOMContentLoaded', restoreOptions);
document.addEventListener('click', listenForClicks);

var slider = document.getElementById("slider");
slider.addEventListener("input", function (evt) {   
    if (evt.target.value < 1) {
      slider.classList.add("slider-angry");
    } else {
      slider.classList.remove("slider-angry");

    }
   
})