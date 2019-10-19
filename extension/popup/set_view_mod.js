document.console.log('ss');
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
    function onError(error) {
      alert(`Error: ${error}`);
    }
    browser.storage.sync.set({ style: msg });
    browser.tabs.sendMessage(tabs[0].id, {
      command: msg,
    });
  }

  browser.tabs.query({ active: true, currentWindow: true })
    .then(setChecks)
    .catch(reportError);

  function reportError(error) {
    console.error(`Could not opt-out: ${error}`);
    // reportExecuteScriptError(error)
  }
}

/**
 * There was an error executing the script.
 * Display the popup's error message, and hide the normal UI.
 */
function reportExecuteScriptError(error) {
  document.querySelector('#popup-content').classList.add('hidden');
  document.querySelector('#error-content').classList.remove('hidden');
  console.error(`Failed to execute opt-out content script: ${error.message}`);
}

function restoreOptions() {
  function setCurrentChoice(result) {
    document.querySelector('#text_white').checked = result.split(',').includes('tw');
    document.querySelector('#text_crossed').checked = result.split(',').includes('tc');
    document.querySelector('#text_removed').checked = result.split(',').includes('tr');
  }

  function onError(error) {
    console.log(`Error: ${error}`);
  }

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