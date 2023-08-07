    var flashMessage = document.querySelector('.flash-message.success');
    if (flashMessage) {
        var inputField = document.querySelector('#code').style.display = 'none';
        var label = document.querySelector('label[for="code"]').style.display = 'none';
        var authorizationTitle = document.querySelector('.authorization-title').style.display = 'none';
        var submitButton = document.querySelector('input[type="submit"]').style.display = 'none';
    }
