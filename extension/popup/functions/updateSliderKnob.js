/**
 * @description Updates slider's knob css image depending on the current value
 *
 * @param slider
 */
export default function (slider) {
  (slider.value === '1') ? slider.classList.remove('slider-angry') : slider.classList.add('slider-angry');
}
