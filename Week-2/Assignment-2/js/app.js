const heading = document.querySelector('#heading');
const hidebtn =  document.querySelector('#hidebtn');
const hidingArea = document.querySelector('#hiding');

heading.addEventListener ('click', ()=> {
    heading.innerHTML = "<h1>Have a Good Time!</h1>"
});

hidebtn.addEventListener('click', ()=>{
	if (hidingArea.style.display === 'none'){
		hidingArea.style.display = 'block';
	} else {
		hidingArea.style.display = 'none';
	}
})
