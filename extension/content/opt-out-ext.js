let selector;
const root = document.getElementById('doc') || document.getElementById('react-root');

if (document.querySelector('body').classList.contains('logged-out')) {
    console.log('offline');
    selector = '.tweet';
} else {
    console.log('online');
    selector = '[data-testid="tweet"]';
}
/*
function which calls server for given node, and depending on the response, applies pre-defined action
 */
let checkText = function(node) {
    console.log('Sending Request');
    let link = "https://api.optoutools.com/predict";
    let xhr = new XMLHttpRequest();
    xhr.open('POST', link, true);
    xhr.setRequestHeader("Content-type", "application/json;charset=UTF-8");
    xhr.withCredentials = true;
    xhr.onreadystatechange = function (e) {
        if (xhr.readyState !== 4) {
            return;
        }
        if (xhr.status === 200) {
            console.log("Response received as ", JSON.parse(xhr.response).predictions[0]);
            if (JSON.parse(xhr.response).predictions[0]){
                node.classList.add("processed-true");
                let tweetText = node.querySelector(selector + ' > div ~ div > div ~ div');
                styleTweet(tweetText, option);
            }
            else {
                node.classList.add("processed-false");
            }
        } else {
            console.log("Failed response", xhr);
        }
    };
    xhr.send(
        JSON.stringify({
            texts: [node.innerText]
        })
    );
};

/*
Depending on `option` sets classes to tweet nodes
 */
let option = "tw";
styleTweet = function(element, option) {
    if (option.includes('tw'))
        element.classList.add("opt-out-tw");
    else
        element.classList.remove("opt-out-tw");
    if (option.includes('tc'))
        element.classList.add("opt-out-tc");
    else
        element.classList.remove("opt-out-tc");
    if (option.includes('tr'))
        element.classList.add("opt-out-trem");
    else
        element.classList.remove("opt-out-trem");
};

/*
* Predefines action and changes it depending on user action
 */
browser.runtime.onMessage.addListener((message) => {
    if (option !== message.command){
        option = message.command;
        let posts = document.getElementsByClassName("processed-true");
        for (let i = 0; i <  posts.length || 0 ; i++ | 0) {
            let tweetText = posts[i].querySelector(selector + ' > div ~ div > div ~ div');//selecting text inside tweet
            styleTweet(tweetText, option);
        }
    }
});


let processTweets = function () {
    let posts = document.querySelectorAll(selector);//selecting tweet object
    for (let i = 0; i < posts.length || 0; i++ | 0) {
        if (posts[i].classList.contains('processed-true'))
            continue;
        if (posts[i].classList.contains('processed-false'))
            continue;
        checkText(posts[i]);
    }
};

const checkTweetList = function (mutationsList) {
    for (let mutation of mutationsList) {
        if (mutation.type === 'childList') {
            processTweets();
        }
    }
};
const checkTweetListObserver = new MutationObserver(checkTweetList);
checkTweetListObserver.observe(root, {childList: true, subtree: true});





