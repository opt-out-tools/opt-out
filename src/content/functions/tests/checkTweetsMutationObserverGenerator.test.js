import checkTweetsMutationObserverGenerator from '../checkTweetsMutationObserverGenerator';
import processTweets from '../processTweets';
jest.mock('../processTweets');

describe('checkTweetsMutationObserverGenerator', () => {
  beforeEach(() => {
    document.body.innerHTML = `
    <div id="root">
    </div>
    `;
  });
  test('Returns instance of mutation observer', () => {
    expect(checkTweetsMutationObserverGenerator('', '')).toBeInstanceOf(
      MutationObserver
    );
  });

  test('Check that observer observes correct event', () => {
    const observer = checkTweetsMutationObserverGenerator('', '');
    observer.observe(document.getElementById('root'), {
      childList: true,
      subtree: true
    });
    const root = document.getElementById('root');
    // Update the root tree by adding a childNode
    root.innerHTML = `<p>I'm gay</p>`
    setTimeout(() => {expect(processTweets).toBeCalled()}, 1500)
    
  });
});
