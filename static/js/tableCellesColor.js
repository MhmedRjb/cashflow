
 // Get all the buttons
 const buttons = document.querySelectorAll('input[type="submit"]');

 // Add a click event listener to each button
 buttons.forEach(button => {
 button.addEventListener('click', event => {
 // Change the background color of the clicked button to red
 event.target.style.backgroundColor = 'red';
 });
 });
 // get the current time in milliseconds
 var currentTime = new Date().getTime();
 
 // get all the rows in the table
 var rows = document.querySelectorAll('table tr');
 
 // loop through each row
 for (var i = 0; i < rows.length; i++) {
 // get the item and mtime cells in the row
 var itemCell = rows[i].querySelector('td:nth-child(1)');
 var mtimeCell = rows[i].querySelector('td:nth-child(2)');
 
 // check if the item and mtime cells exist
 if (itemCell && mtimeCell) {
   // get the item and mtime values
   var itemValue = itemCell.textContent;
   var mtimeValue = new Date(mtimeCell.textContent).getTime();
 
   // calculate the time difference in minutes
   var timeDifference = (currentTime - mtimeValue) / (1000 * 60);
 
   // check if the item value is SBAccMFDtlRpt.xls or SBJRNLITMRPTTAX.xls
   if (itemValue === 'SBAccMFDtlRpt.xls' || itemValue === 'SBJRNLITMRPTTAX.xls') {
       // check if the time difference is less than or equal to 15 minutes
       if (timeDifference <= 15) {
           // add the yes class to the row
           rows[i].classList.add('yes');
       } else {
           // add the maybe class to the row
           rows[i].classList.add('maybe');
       }
   } else {
       // add the no class to the row
       rows[i].classList.add('no');
   }
 }
 }
