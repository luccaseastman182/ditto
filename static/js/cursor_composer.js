document.addEventListener('DOMContentLoaded', function() {
    const dragAndDropArea = document.getElementById('drag-and-drop-area');

    dragAndDropArea.addEventListener('dragover', function(event) {
        event.preventDefault();
        dragAndDropArea.classList.add('dragover');
    });

    dragAndDropArea.addEventListener('dragleave', function(event) {
        event.preventDefault();
        dragAndDropArea.classList.remove('dragover');
    });

    dragAndDropArea.addEventListener('drop', function(event) {
        event.preventDefault();
        dragAndDropArea.classList.remove('dragover');

        const files = event.dataTransfer.files;
        handleFiles(files);
    });

    function handleFiles(files) {
        for (let i = 0; i < files.length; i++) {
            const file = files[i];
            const reader = new FileReader();

            reader.onload = function(event) {
                const fileContent = event.target.result;
                console.log('File content:', fileContent);
                // Add your logic to handle the file content here
            };

            reader.readAsText(file);
        }
    }
});
