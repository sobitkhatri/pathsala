// var overlay = document.getElementsByClassName("overlay")[0];
var comment = document.getElementsByClassName("comment")[0];
// var images=[];
// images[0]='images/overlay1.png';
// images[1]='images/overlay2.png';
// images[2]='images/overlay3.png';
var i=0;
var comments=[];
comments[0]="Find schools that are in your locality easily!";
comments[1]="Manage the data and records of your students!";
comments[2]="Ask questions and clear your doubts right away!";



function changeImg(){
	comment.children[0].innerText=comments[i];
	// overlay.style.backgroundImage='url(' + images[i] + ')';
	if(i<2){
		i++;
	}else{
		i=0;
	}

	setTimeout("changeImg()",4000);
}

window.onload=changeImg;
window.addEventListener('resize', function () {console.log(window.innerWidth)});