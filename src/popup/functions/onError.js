/**
 * @description Display the popup's error message, and hide the normal UI.
 *
 * @param error - contains error message
 */
export default function (error) {
  document.querySelector('#popup-content').classList.add('hidden');
  document.querySelector('#error-content').classList.remove('hidden');
  console.error(`Failed to execute opt-out content script: ${error.message}`);
}
