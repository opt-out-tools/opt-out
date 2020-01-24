import updateSliderKnob from './updateSliderKnob.js';

/**
 * @description Updates slider and option states, from values provided by result, and sets them in popup
 * @param result {object}
 */
export default function (result) {
  document.querySelector(`#${result.optOut.selector}`).checked = true;
  const slider = document.querySelector('#slider');
  slider.value = result.optOut.slider;
  updateSliderKnob(slider);
}
