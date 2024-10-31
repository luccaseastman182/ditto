document.addEventListener('DOMContentLoaded', function() {
    const uploadForm = document.getElementById('uploadForm');
    const fileInput = document.getElementById('fileInput');
    const fileList = document.getElementById('fileList');

    uploadForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData();
        formData.append('file', fileInput.files[0]);

        fetch('/bolt_new/upload', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
            } else {
                alert(data.message);
                const listItem = document.createElement('li');
                listItem.textContent = data.filename;
                fileList.appendChild(listItem);
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});
