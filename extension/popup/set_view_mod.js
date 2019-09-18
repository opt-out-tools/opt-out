
function listenForClicks() {
    document.addEventListener("click", (e) => {

        if (document.getElementById('text_white').checked){

        }

        function getChecks(tabs) {
            let msg =[];
            if (document.getElementById('text_white').checked){
                msg.push("tw");
            }
            if (document.getElementById('text_crossed').checked){
                msg.push("tc");
            }
            if (document.getElementById('text_removed').checked){
                msg.push("tr");
            }
            msg = msg.join();

            browser.tabs.sendMessage(tabs[0].id, {
                command: msg,
            });
        }


        browser.tabs.query({active: true, currentWindow: true})
            .then(getChecks)
            .catch(reportError);

        function reportError(error) {
            console.error(`Could not opt-out: ${error}`);
        }

    });
}

/**
 * There was an error executing the script.
 * Display the popup's error message, and hide the normal UI.
 */
function reportExecuteScriptError(error) {
    document.querySelector("#popup-content").classList.add("hidden");
    document.querySelector("#error-content").classList.remove("hidden");
    console.error(`Failed to execute opt-out content script: ${error.message}`);
}

/**
 * When the popup loads, inject a content script into the active tab,
 * and add a click handler.
 * If we couldn't inject the script, handle the error.
 */
listenForClicks();
