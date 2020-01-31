/**
 * @description Updates `option` and `slider` depending on the given result
 * @param result
 * @param popupPrefs
 * @return popupPrefs
 */
export default function (result, popupPrefs) {
  popupPrefs.optionVal = result.optOut.selector;
  popupPrefs.sliderVal = result.optOut.slider;
  return popupPrefs;
}
