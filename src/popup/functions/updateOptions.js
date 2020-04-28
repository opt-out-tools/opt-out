import updateSliderKnob from './updateSliderKnob.js';

/**
 * @description Updates slider and option states, from values provided by result, and sets them in popup
 * @param result {object}
 */
export default function (result) {
  const slider = document.querySelector('#slider');
  if (
    // There are saved settings
    result &&
    result.optOut &&
    result.optOut.slider &&
    result.optOut.selector
  ) {
    document.querySelector(`#${result.optOut.selector}`).checked = true;
    // Set the settings on the slider
    slider.value = result.optOut.slider;
    updateSliderKnob(slider);
  } else {
    // No saved settings
    updateSliderKnob(slider);
  }
}
