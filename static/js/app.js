// Function to preview image before uploading
function previewImage(event) {
    const file = event.target.files[0];
    const reader = new FileReader();
    reader.onload = function(e) {
        const preview = document.getElementById('image-preview');
        preview.src = e.target.result;
        preview.style.display = 'block';
    };
    reader.readAsDataURL(file);
}

// Show loading spinner during prediction
document.getElementById('uploadForm').onsubmit = function() {
    document.getElementById('loading').style.display = 'block';
    setTimeout(function() {
        // Simulating prediction process completion
        document.getElementById('loading').style.display = 'none';
        // Display prediction result
        document.getElementById('prediction-result').textContent = 'Disease Detected: Blight';
        document.getElementById('suggestion').textContent = 'Apply fungicide and remove infected leaves.';
        document.getElementById('result').style.display = 'block';
    }, 3000); // Simulated 3-second delay for prediction
};
document.querySelector('input[type="file"]').addEventListener('change', (event) => {
    const fileName = event.target.files[0].name;
    alert(`File selected: ${fileName}`);
});