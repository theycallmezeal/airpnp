window.onload = function(event) {
	document.getElementById("submit").onclick = function(event) {
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
				cleanliness = radios[i].value;
				break;
			}
		}
		
		if (cleanliness == 0 || amenities == 0) {
			/* false */
		}
	}
}