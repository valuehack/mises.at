function openTag(){
  if(window.location.hash) {
    var tag = document.getElementById(window.location.hash.substr(1));
    
    if(tag){
      var content = document.getElementById(window.location.hash.substr(1) + "-content")
      //var element = document.querySelector(window.location.hash)
      tag.classList.add('content-visible');
      content.style.display="block";
      setTimeout(function(){
        window.scrollBy(0,-100);
      }, 10);
      
      console.log(window.location.hash + " worked!");
    }
    //console.log(window.location.hash + " Tag: " + tag);
  } else {
    console.log("Element not found.");
  }
}

window.onload = openTag();
