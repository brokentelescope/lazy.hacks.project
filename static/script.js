// Function to handle file reading
function readCSVFile(file) {
    const reader = new FileReader();

    // Event triggered when file reading is complete
    reader.onload = function(event) {
        const csvContent = event.target.result;
        document.getElementById('output').textContent = csvContent;
    };

    // Read the file as text
    reader.readAsText(file);
}

// Add event listener to the file input
document.getElementById('csvFileInput').addEventListener('change', function(event) {
    const file = event.target.files[0];  // Get the uploaded file
    if (file) {
        readCSVFile(file);  // Read the file if it's selected
    }
});