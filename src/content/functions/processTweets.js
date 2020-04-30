import checkText from './checkText';
// TODO: Check opt-out-ext.js for changes needed here
export default (selector, popupPrefs) => {
  console.log("SICK!")
  const posts = document.querySelectorAll(selector); // selecting tweet object
  posts.forEach((post) => {
    if (post.classList.contains('processed-true')) return;
    if (post.classList.contains('processed-false')) return;
    if (post.classList.contains('processing')) return;
    checkText(post, selector, popupPrefs);
  });
};
