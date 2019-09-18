
//Server request check function
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
            if (JSON.parse(xhr.response).predictions[0] === true){
                node.classList.add("processed-true");
                let tweetText = node.querySelector('[data-testid="tweet"] > div ~ div > div ~ div');
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
let option = "tw";

styleTweet = function(element, option) {
    if (option.includes('tw')) element.classList.add("opt-out-tw");
    else element.classList.remove("opt-out-tw");
    if (option.includes('tc')) element.classList.add("opt-out-tc");
    else element.classList.remove("opt-out-tc");
    if (option.includes('tr')) element.classList.add("opt-out-trem");
    else element.classList.remove("opt-out-trem");
};

browser.runtime.onMessage.addListener((message) => {
    if (option !== message.command){
        option = message.command;
        let posts = document.getElementsByClassName("processed-true");
        for (let i = 0, len = posts.length | 0; i < len; i = i + 1 | 0) {
            let tweetText = posts[i].querySelector('[data-testid="tweet"] > div ~ div > div ~ div');//selecting text inside tweet
            styleTweet(tweetText, option);

        }
    }
});


if (document.querySelector('body').classList.contains('logged-out')){
    console.log('offline');
    //Un-logged user processing

    let checkPosts = function () {
        let posts = document.getElementsByClassName("js-tweet-text-container");

        let hideSiblings = function (elem, selector) {
            // Get the next sibling element
            let sibling = elem.nextElementSibling;
            // If there's no selector, return the first sibling
            if (!selector) return sibling;
            // If the sibling matches our selector, use it
            // If not, jump to the next sibling and continue the loop
            while (sibling) {
                if (sibling.matches(selector)) sibling.remove();//sibling.style.display = "none !important";
                sibling = sibling.nextElementSibling
            }
        };


        for (let i=0, len=posts.length|0; i<len; i=i+1|0) {//TODO: re-work hideSiblings by using selectors
            posts[i].parentElement.style.border = "5px solid red";
            //hideSiblings(posts[i], '.QuoteTweet');
            hideSiblings(posts[i], '.AdaptiveMediaOuterContainer');
            hideSiblings(posts[i], '.CardContent');
            hideSiblings(posts[i], '.SummaryCard-image');
            posts[i].style.display = 'none';
        }

    };

    checkPosts();// hid tweets on load
    addEventListener("scroll", function(e){//hide tweets ons scroll
        checkPosts();
    });

} else {
    //logged user processing
    let processTweets = function () {
        let posts = document.querySelectorAll('[data-testid="tweet"]');//selecting tweet object
        for (let i = 0, len = posts.length | 0; i < len; i = i + 1 | 0) {
            if (posts[i].classList.contains('processed-true'))
                continue;
            if (posts[i].classList.contains('processed-false'))
                continue;
            let tweetText = posts[i].querySelector('[data-testid="tweet"] > div ~ div > div ~ div');//selecting text inside tweet
            checkText(posts[i]);

        }
    };
    const root = document.getElementById('react-root');
    const checkTweetList = function(mutationsList) {
        for(let mutation of mutationsList) {
            if (mutation.type === 'childList'){
                    processTweets();
            }
        }
    };
    const checkTweetListObserver = new MutationObserver(checkTweetList);
    checkTweetListObserver.observe(root, { childList: true, subtree: true });
}


