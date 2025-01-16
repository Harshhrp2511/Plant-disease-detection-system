// Function to preview image before uploading
function previewImage(event) {
    const file = event.target.files[0];

    // Check if a file is selected
    if (!file) {
        alert("Please select a file to preview.");
        return;
    }

    // Validate file type (only image files)
    const validImageTypes = ["image/jpeg", "image/png", "image/gif"];
    if (!validImageTypes.includes(file.type)) {
        alert("Invalid file type. Please upload an image file (JPEG, PNG, or GIF).");
        return;
    }

    // Read and display the image preview
    const reader = new FileReader();
    reader.onload = function (e) {
        const preview = document.getElementById("image-preview");
        preview.src = e.target.result;
        preview.style.display = "block";
    };
    reader.readAsDataURL(file);
}

// Function to handle form submission and show loading spinner
function handleFormSubmit(event) {
    event.preventDefault(); // Prevent default form submission

    const loadingSpinner = document.getElementById("loading");
    const resultSection = document.getElementById("result");
    const predictionResult = document.getElementById("prediction-result");
    const suggestionText = document.getElementById("suggestion");

    // Show loading spinner
    loadingSpinner.style.display = "block";
    resultSection.style.display = "none"; // Hide previous results, if any

    // Simulate prediction process
    setTimeout(function () {
        loadingSpinner.style.display = "none"; // Hide spinner

        // Display simulated prediction result
        predictionResult.textContent = "Disease Detected: Blight";
        suggestionText.textContent = "Apply fungicide and remove infected leaves.";
        resultSection.style.display = "block";
    }, 3000); // Simulated 3-second delay
}

// Function to alert the selected file name
function handleFileChange(event) {
    const file = event.target.files[0];
    if (file) {
        alert(`File selected: ${file.name}`);
    }
}

// Attach event listeners
document.addEventListener("DOMContentLoaded", () => {
    const uploadForm = document.getElementById("uploadForm");
    const fileInput = document.querySelector('input[type="file"]');

    uploadForm.addEventListener("submit", handleFormSubmit);
    fileInput.addEventListener("change", handleFileChange);
});
