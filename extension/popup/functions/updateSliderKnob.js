/**
 * @description Updates slider's knob css image depending on the current value
 *
 * @param slider
 */
export default function (slider) {
  slider.classList.remove(...slider.classList);
  switch (true) {
    case (parseFloat(slider.value) >= 1) :
      slider.classList.add('slider-happy');
      break;
    case (parseFloat(slider.value) >= 0.9) :
      slider.classList.add('slider-09');
      break;
    case (parseFloat(slider.value) >= 0.8) :
      slider.classList.add('slider-08');
      break;
    case (parseFloat(slider.value) >= 0.7) :
      slider.classList.add('slider-07');
      break;
    case (parseFloat(slider.value) >= 0.6) :
      slider.classList.add('slider-06');
      break;
    case (parseFloat(slider.value) >= 0.5) :
      slider.classList.add('slider-05');
      break;
  }
}
