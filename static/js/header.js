    var url = window.location.href;
    var links = document.querySelectorAll("#mainnav li a, #submainNavcards li a");
    for (var i = 0; i < links.length; i++) {
        if (url == links[i].href) {
            links[i].parentNode.classList.add("active");
        }
    }
    
