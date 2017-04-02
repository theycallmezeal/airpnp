function validateForm() {
	var radios = document.getElementsByName('cleanliness');
	var cleanliness = 0;
	for (var i = 0, length = radios.length; i < length; i++) {
		if (radios[i].checked) {
			cleanliness = radios[i].value;
			break;
		}
	}
	radios = document.getElementsByName('amenities');
	var amenities = 0;
	for (var i = 0, length = radios.length; i < length; i++) {
		if (radios[i].checked) {
			amenities = radios[i].value;
			break;
		}
	}
	
	if (cleanliness == 0 || amenities == 0) {
		document.getElementById("error").innerHTML = "You must include a rating in both categories to submit."
		return false;
	}
	return true;
}