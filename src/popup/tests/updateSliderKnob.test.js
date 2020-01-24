import updateSliderKnob from '../functions/updateSliderKnob';

describe('Testing updateSliderKnob adding and removing of `slider-angry` class', () => {
  const slider = document.createElement('input');
  slider.setAttribute('type', 'range');
  slider.setAttribute('min', '0');
  slider.setAttribute('max', '1');
  beforeEach(() => {
    slider.classList.remove(...slider.classList);
    slider.value = '0';
  });

  const caseClassName = [
    ['1', 'slider-happy'],
    ['0.9', 'slider-09'],
    ['0.8', 'slider-08'],
    ['0.7', 'slider-07'],
    ['0.6', 'slider-06'],
    ['0.5', 'slider-05']
  ];

  test.each(caseClassName)(
    'given value %p adds %p class',
    (value, className) => {
      slider.value = value;
      updateSliderKnob(slider);
      expect(slider.classList.contains(className))
        .toBe(true);
    }
  );

  const caseClassNum = [
    ['1', 1],
    ['0.9', 1],
    ['0.8', 1],
    ['0.7', 1],
    ['0.6', 1],
    ['0.5', 1],
    ['0.4', 0],
    ['0', 0]
  ];

  test.each(caseClassNum)(
    'given value %p have only %p class',
    (value, numOfClasses) => {
      slider.value = value;
      updateSliderKnob(slider);
      expect(slider.classList.length)
        .toBe(numOfClasses);
    }
  );
});
