import onError from '../functions/onError';

describe('Test: onError', () => {
  test('testing if onError gives console.error', () => {
    const spy = jest.spyOn(global.console, 'error').mockImplementation();
    onError('I am error for test.'); // Won't be displayed (mocked)
    console.error('random error'); // Won't be displayed (mocked)
    expect(spy).toHaveBeenCalledTimes(2);
    expect(spy).toHaveBeenLastCalledWith('random error');
    expect(spy.mock.calls).toEqual([['Error: I am error for test.'], ['random error']]);
    spy.mockRestore();
  });
});
