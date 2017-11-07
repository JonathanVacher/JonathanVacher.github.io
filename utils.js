function sidebar(){
	document.write('<div id="sidebar"> <div id="sidebar-fixed"> <img src="myphoto.jpg" title="my photo" id="my_photo" /> <h3>Contact</h3> <p> Albert Einstein College of Medicine, <br /> Block Research Pavilion, <br /> Department of Systems and Computational Biology, <br /> 1301 Morris Park Avenue, <br /> 10461 Bronx, NY <br /> USA <br /> firstname.lastname@einstein.yu.edu<br /> <a href="#">https://jonathanvacher.github.io/</a></p> <h3>Acknowledgements</h3> <p> Thanks to Manon Esnouf for the amazing photo ! </p> </div></div>');	
		}


function banner(){
	document.write('<div id="banner"> <div id="name"> <h1>Jonathan Vacher</h1> <p>PhD</p> <p>Department of Systems and Computational Biology </p> <p>Albert Einstein College of Medicine, New York</p> </div> <div id="welc"> <h1>Welcome</h1> </div> </div>');	
		}

function news(title,text){

document.write('<div id="news"> <p> <t2>' + title + '</t2> <br /><br />' + text + '</p> </div>');

}

function rss(){

var x=10; // your X iteration limit

// load the xml data. it is parsed by jquery
$.get("news.xml", function(data) {
    var $xml = $(data);

    $xml.find("item").each(function(i, val) { // find the items in the rss and loop

        // create an item object with all the necessary information out of the xml
        var $this = $(this),
            item = {
                title: $this.find("title").text(),
                link: $this.find("link").text(),
                description: $this.find("description").text()
        };
        // replace the CDATA in the item title
        item.title = item.title.replace("<![CDATA[", "").replace("]]>", "");

        // #feed selects the ul element with the id feed
        // and append() appends a newly created li element
        // to the ul
        $('#feed').append($('<li><a href="' +item.guid +'">' +item.title +'</a></li>'));

        return i<(x-1); // (stop after x iterations)
    });
})
}		
					
