// Function to toggle the 'yes' or 'no' class on a row based on the value of the dropdown menu
function togglePaid(cell) {
    var span = cell.querySelector("span");
    var select = cell.querySelector("select");
  
    if (clickCount === 0) {
      span.style.display = "none";
      select.style.display = "";
      clickCount++;
    } else if (clickCount === 1) {
      clickCount++;
    } else {
      span.style.display = "";
      select.style.display = "none";
      clickCount = 0;
    }
  }
  
  // Function to toggle the display of span and input elements in a cell
  function toggleInput(cell) {
    var span = cell.querySelector("span");
    var input = cell.querySelector("input");
    span.style.display = "none";
    input.style.display = "";
  }
  
  // Function to add event listeners to each dropdown menu
  function addDropdownEventListeners() {
    var dropdowns = document.querySelectorAll('select[name="paid"]');
  
    for (var i = 0; i < dropdowns.length; i++) {
      // Store the original value of the dropdown menu
      dropdowns[i].dataset.originalValue = dropdowns[i].value;
  
      dropdowns[i].addEventListener('change', function() {
        // Get the row element
        var row = this.closest('tr');
  
        // Remove any existing color classes from the row
        row.classList.remove('yes', 'no');
  
        // Add the appropriate color class depending on the value of the dropdown menu
        if (this.value === '1') {
          row.classList.add('yes');
        } else if (this.value === '0') {
          row.classList.add('no');
        }
      });
    }
  }
  
