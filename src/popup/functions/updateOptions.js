import updateSliderKnob from './updateSliderKnob.js';

/**
 * @description Updates slider and option states, from values provided by result, and sets them in popup
 * @param result {object}
 */
export default function (result) {
  const slider = document.querySelector('#slider');
  // If no saved settings in local storage
  if (
    Object.keys(result).length === 0 ||
    result.optOut == null ||
    (result.optOut.slider == null && result.optOut.selector == null)
  ) {
    // Set slider class for display
    updateSliderKnob(slider);
  } else {
    // If there are saved settings
    document.querySelector(`#${result.optOut.selector}`).checked = true;
    // Set the settings on the slider
    slider.value = result.optOut.slider;
    updateSliderKnob(slider);
  }
}
