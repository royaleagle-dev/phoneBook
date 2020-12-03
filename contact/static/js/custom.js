function openTab(elemId, className){
	var elements = document.getElementsByClassName(className);
	for (var i =0; i<elements.length; i++){
		elements[i].style.display = 'none'
	}
	document.getElementById(elemId).style.display = 'block'
}

function openContact(elemId){
	$('#infoCenter').show('fast');
	
	const element = document.getElementById(elemId);
	const contactName = document.querySelector("#contactName");
	const phone = element.dataset.phone;
	const address = element.dataset.address;
	const phoneBtn = document.getElementById("phoneBtn");
	const phoneDisplay = document.querySelector("#phone");
	const addressDisplay = document.querySelector("#address");
	
	contactName.textContent = element.textContent
	phoneDisplay.textContent = phone;
	phoneBtn.setAttribute('href', `tel://${phone}`);
	addressDisplay.textContent = address;
}

$('#infoCenter').hide('fast')

$('#clickContact').click(function(){
	openTab('contact', 'contactSection')
})

$('#clickExtras').click(function(){
	openTab('extras', 'contactSection');
})

$("input[name='searchTerm").focus()