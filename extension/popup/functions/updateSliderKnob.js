/**
 * @description Updates slider's knob css image depending on the current value
 *
 * @param slider
 */
export default function (slider) {
  (parseFloat(slider.value) >= 0.5) ? slider.classList.remove('slider-angry') : slider.classList.add('slider-angry');
}
