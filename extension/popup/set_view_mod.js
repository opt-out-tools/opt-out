function restoreOptions() {
  function setCurrentChoice(result) {
    document.querySelector(`#${result.optOut.selector}`).checked = true;
    document.querySelector('#slider').value = result.optOut.slider;
  }

  function onError(error) {
    console.log(`Error: ${error}`);
  }

  browser.storage.sync.get('optOut').then(setCurrentChoice, onError);
}

// const slider = document.getElementById('slider');
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
  function setSliderKnobCSS(slider, sliderStatus) {
    // Todo: fix with CSS value only style
    // eslint-disable-next-line no-unused-expressions
    (sliderStatus === '1') ? slider.classList.remove('slider-angry') : slider.classList.add('slider-angry');
  }

  function setChecks(tabs) {
    const slider = document.getElementById('slider');
    const sliderStatus = slider.value;
    setSliderKnobCSS(slider, sliderStatus);
    const optionValue = document.querySelector('input[name="text_options"]:checked').value || 'tc';
    const popupSettings = {
      slider: sliderStatus,
      selector: optionValue,
    };
    browser.storage.sync.set({ optOut: popupSettings });
    browser.tabs.sendMessage(tabs[0].id, popupSettings);
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
document.addEventListener('input', listenForClicks);
