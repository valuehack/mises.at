/*
 * Set the style to active of the nav element according to the current page
 */
function setActive() {
	aObj = document.getElementById('nav').getElementsByTagName('a');
		for(i=0;i<aObj.length;i++) { 
			if(document.location.href.indexOf(aObj[i].href)>=0) {
				aObj[i].className='nav--active';
            }
        }
}
window.onload = setActive;

/*
 * For small screens, show nav after click on burger icon
 */            

function showNav() {
	if (document.documentElement.clientWidth < 740) {
		aObj = document.getElementById('nav');
		if (aObj.style.display == 'none' || aObj.style.display == '') {
			aObj.style.display = 'block';
		}
		else {
			aObj.style.display = 'none';
		}
	}
}

/*
 * Simple jQuery show/hide function
 */
$(document).ready(function(){
        $('.hidden').addClass("hide");

        $('.showhide').click(function() {
            var $this = $('.hidden');

            if ($this.hasClass("hide")) {
                $('.hidden').removeClass("hide").addClass("show");

            } else {
                $('.hidden').removeClass("show").addClass("hide");
            }
        });
    });
		
function tagLink(){
	setTimeout(function(){
		if (typeof openTag === "function") { 
		    openTag();
		}
	}, 10);
}
