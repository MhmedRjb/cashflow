const dropZones = document.querySelectorAll('.drop-zone');

dropZones.forEach(dropZone => {
  const input = dropZone.querySelector('.drop-zone__input');
  const prompt = dropZone.querySelector('.drop-zone__prompt');

  dropZone.addEventListener('click', () => {
    input.click();
  });

  input.addEventListener('change', () => {
    const file = input.files[0];
    if (file) {
      prompt.textContent = file.name;
    }
  });

  dropZone.addEventListener('dragover', e => {
    e.preventDefault();
    dropZone.classList.add('drop-zone--over');
  });

  ['dragleave', 'dragend'].forEach(type => {
    dropZone.addEventListener(type, () => {
      dropZone.classList.remove('drop-zone--over');
    });
  });

 dropZone.addEventListener('drop', e => {
   e.preventDefault();

   if (e.dataTransfer.files.length) {
     input.files = e.dataTransfer.files;
     prompt.textContent = e.dataTransfer.files[0].name;
   }

   dropZone.classList.remove('drop-zone--over');
 });
});
