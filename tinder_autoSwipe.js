/*
*	AutoSwipe[Right]_Tinder
*	Developed By JOHN MELODY ME
*/

setInterval(function() { 
	button = document.querySelector('button[aria-label^="like"]') 
	/*For [Dislikes] :{
    	button = document.querySelector('button[aria-label^="dislike"]')
     */
	button.smash = button.click
	button.smash();
	}, 100)