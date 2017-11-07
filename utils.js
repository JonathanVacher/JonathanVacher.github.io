function sidebar(){
	document.write('<div id="sidebar"> <div id="sidebar-fixed"> <img src="myphoto.jpg" title="my photo" id="my_photo" /> <h3>Contact</h3> <p> Albert Einstein College of Medicine, <br /> Block Research Pavilion, <br /> Department of Systems and Computational Biology, <br /> 1301 Morris Park Avenue, <br /> 10461 Bronx, NY <br /> USA <br /> firstname.lastname@einstein.yu.edu<br /> <a href="#">https://jonathanvacher.github.io/</a></p> <h3>Acknowledgements</h3> <p> Thanks to Manon Esnouf for the amazing photo ! </p> </div></div>');	
		}


function banner(){
	document.write('<div id="banner"> <div id="name"> <h1>Jonathan Vacher</h1> <p>PhD</p> <p>Department of Systems and Computational Biology </p> <p>Albert Einstein College of Medicine, New York</p> </div> <div id="welc"> <h1>Welcome</h1> </div> </div>');	
		}

function news(title,text){

document.write('<div id="news"> <p> <t2>' + title + '</t2> <br /><br />' + text + '</p> </div>');

}

		
$.get('news.txt',function(data){
    var perLine=data.split('\n');
    var myVars=[];
    for(i=0;i<perLine.length;i++)
    {
    var line=perLine[i].split(' ');
    myVars[i]={
        'time':line[0],
        'event':line[1],
        'color':line[2]
        }
    }
    console.log(myVars);
    console.log(myVars[0].time);
    console.log(myVars[0].event);
    console.log(myVars[0].color);
});			
