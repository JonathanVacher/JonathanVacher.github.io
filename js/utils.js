function sidebar(){
	document.write( '<div id="sidebar">' +
			'<img src="myphoto.jpg" title="my photo" id="my_photo" />' +
			'<h3>Contact</h3>' +
			'<p> Albert Einstein College of Medicine, <br />' +
			'Block Research Pavilion, <br />' +
			'Department of Systems and Computational Biology, <br />' +
			'1301 Morris Park Avenue, <br />' +
			'10461 Bronx, NY <br />' +
			'USA <br />' +
			'firstname.lastname@einstein.yu.edu<br />' +
			'<a href="#">https://jonathanvacher.github.io/</a></p>' +
			'<h3>Acknowledgements</h3>' +
			'<p> Thanks to Manon Esnouf for the amazing photo ! </p>' +
			'</div>');	
		}


function banner(){
	document.write( '<div id="banner">' +
			'<div id="name">' +
			'<h1>Jonathan Vacher</h1>' +
			'<p>PhD</p>' + 
			'<p>Department of Systems and Computational Biology </p>' +
 			'<p>Albert Einstein College of Medicine, New York</p>' + 
			'</div> <div id="welc"> <h1>Welcome</h1>' +
			'</div>' + 
			'</div>');	
		}

function news(title,text){

document.write('<div id="news"> <p> <t2>' + title + '</t2> <br /><br />' + text + '</p> </div>');

}

function newsf(title,text){

document.write('<div id="news_f"> <p> <t2>' + title + '</t2> <br /><br />' + text + '</p> </div>');

}
		

