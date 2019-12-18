import updateSliderKnob from '../functions/updateSliderKnob';

describe('Testing updateSliderKnob adding and removing of `slider-angry` class', () => {
  const slider = document.createElement('input');
  slider.setAttribute('type', 'range');
  slider.setAttribute('min', '0');
  slider.setAttribute('max', '1');
  beforeEach(() => {
    slider.classList.remove(...slider.classList);
    slider.value = '1';
  });
  test('check if slider adds `slider-angry` class', () => {
    slider.value = '0';
    updateSliderKnob(slider);
    expect(slider.classList.contains('slider-angry'))
      .toBe(true);
  });
  test('check if slider removes `slider-angry` class', () => {
    slider.classList.add('slider-angry');
    slider.value = '1';
    updateSliderKnob(slider);
    expect(slider.classList.contains('slider-angry'))
      .toBe(false);
  });
});
