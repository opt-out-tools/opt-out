/**
 * @description Depending on `option` sets classes to tweet nodes
 */
export default function (element, popupPrefs) {
  console.log('styling tweet', element, popupPrefs);
  element.classList.remove('opt-out-tw', 'opt-out-tc', 'opt-out-trem');
  if (parseFloat(element.dataset.prediction) <= parseFloat(popupPrefs.sliderVal)) {
    switch (popupPrefs.optionVal) {
      case 'text_white':
        element.classList.add('opt-out-tw');
        break;
      case 'text_crossed':
        element.classList.add('opt-out-tc');
        break;
      case 'text_removed':
        element.classList.add('opt-out-trem');
        break;
    }
  }
}
