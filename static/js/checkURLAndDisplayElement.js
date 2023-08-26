
  // Function to check the current URL and display/hide an element based on the URL
  function checkURLAndDisplayElement() {
    var currentUrl = window.location.href;
    var li = document.getElementById("hiddenLi");
  
    if (currentUrl.includes("/display_goodstransectionte_summary")) {
      li.style.display = "list-item";
    } else {
      li.style.display = "none";
    }
  }
  
  // Function to hide the print link on a specific URL path
  function hidePrintLinkOnSpecificPath() {
    if (window.location.pathname !== '/comapny_name/main/reports/cashflow/display_goodstransectionte_summary') {
      document.getElementById('print-link').style.display = 'none';
    }
  }
  
  // Function to fetch data
  function fetchData() {
    // ... Add your fetchData implementation here ...
  }
  
  // Call the functions when the window loads
  window.onload = function() {
    addDropdownEventListeners();
    checkURLAndDisplayElement();
    hidePrintLinkOnSpecificPath();
  };
  
  // Global variable to keep track of click count
  var clickCount = 0;
  