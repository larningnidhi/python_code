
	function myfunction() 
	{
		var fname = document.getElementById("fname");
		var lastname = document.getElementById("lastname");
		if(fname.value==""|| lastname.value=="" )
		{
			alert("no blank value allowed");
		}
		else
		{
			location.replace("p1.html");
		}

		var email = document.getElementById("email");
				
		var date = document.getElementById("date");
		var number = document.getElementById("number");
		if(date.value==""|| number.value=="" )
		{
			alert("no blank value allowed");
		}
		else
		{
			location.replace("p1.html");
		}
	}
		

		// $('#fname').val()

		// jQuery

		// 1. onSubmit - Validation about all form inputs are filled
		// 2. Hide the form and put the values in div using jQuery
	