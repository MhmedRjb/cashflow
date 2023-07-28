
 // create a question mark element
 var questionMark = document.createElement('span');
 questionMark.textContent = '?';
 questionMark.className = 'question-mark';
 questionMark.style.cursor = 'pointer';
 
 // append the question mark to a specific cell in the table
 document.querySelector('table tr th:nth-child(1)').appendChild(questionMark);
 
 // create a tooltip element
 var tooltip = document.createElement('div');
 tooltip.style.position = 'absolute';
 tooltip.style.display = 'none';
 tooltip.style.backgroundColor = 'white';
 tooltip.style.border = '1px solid black';
 tooltip.style.padding = '5px';
 document.body.appendChild(tooltip);
 
 // add a mouseover event listener to the question mark
 questionMark.addEventListener('mouseover', function(event) {
 // update the text of the tooltip
 tooltip.innerHTML = '<ul style="direction: rtl;"><li   ><span style="color: green; font-weight: bold;">الأخضر:</span> الملف المطلوب وتم رفعه في  اخر ربع ساعة.</li><li><span style="color: #FFD700; font-weight: bold;">الأصفر:</span>الملفات صحيحة لكن لم تحدث </li><li><span style="color: red; font-weight: bold;">الأحمر:</span> ليس الملف المطلوب</li></ul>';
 
 // position and show the tooltip
 tooltip.style.left = event.pageX + 'px';
 tooltip.style.top = event.pageY + 'px';
 tooltip.style.display = 'block';
 });
 
 // add a mouseout event listener to the question mark
 questionMark.addEventListener('mouseout', function() {
 // hide the tooltip
 tooltip.style.display = 'none';
 });
 