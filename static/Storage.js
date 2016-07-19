function SaveItem() {
			
	var name = document.forms.news.name.value;
	var data = document.forms.news.data.value;
	localStorage.setItem(name, data);
	doShowAll();
	
	
}



function ClearAll() {
	localStorage.clear();
	doShowAll();
	
}

function doShowAll() {

	var key = "";
		var list = "<tr><th></th><th></th></tr>\n";
		var i = 0;
		for (i = 0; i <= localStorage.length - 1; i++) {
			key = localStorage.key(i);
			list += "<tr><td>" + key + " says: "+"</td>\n<td>"
					+ localStorage.getItem(key) + "</td></tr>\n";
		}
		if (list == "<tr><th></th><th></th></tr>\n") {
			list += "<tr><td><i></i></td>\n<td><i></i></td></tr>\n";
		}
		document.getElementById('list').innerHTML = list;
}



        var display=document.getElementbyId("searchnamedisplay");
        display.innerHTML=document.getElementbyId("searchname").value;
// function CheckBrowser() {
// 	if ('localStorage' in window && window['localStorage'] !== null) {
// 		// we can use localStorage object to store data
// 		return true;
// 	} else {
// 			return false;
// 	}
// }