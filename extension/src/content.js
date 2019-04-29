import domLoaded from 'dom-loaded';

import {
	observeEl,
	safeElementReady
} from './utils';

async function init() {
	await safeElementReady('body');

	// Add class to DOM
	document.documentElement.classList.add('block-it');

	await domLoaded;
	onDomReady();
}

function onRouteChange(cb) {
	observeEl('#doc', cb, {attributes: true});
}

function onNewTweets(cb) {
	observeEl('#stream-items-id', cb);
}

function processAllTweets() {
	const styledClassName = 'bl-it-replaced';

	$('.tweet-text').each((i, el) => {
		if ($(el).hasClass(styledClassName)) {
			return;
		}

		const text = $(el).text();
		if (text) {
			// TODO send text to API
			const replaced = $(el).html().replace(/you/g, 'me');
			$(el).html(replaced);
		}

		$(el).addClass(styledClassName);
	});
}

function onDomReady() {
	console.log('DOM Ready!');
	processAllTweets();

	onRouteChange(() => {
		console.log('Route change!');
		processAllTweets();

		onNewTweets(() => {
			console.log('New Tweets!');
			processAllTweets();
		});
	});
}

init();
