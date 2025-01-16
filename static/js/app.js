// Function to preview image before uploading
function previewImage(event) {
    const file = event.target.files[0];

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
        if (preview) {
            preview.src = e.target.result;
            preview.style.display = "block";
        }
    };
    reader.readAsDataURL(file);
}

// Function to handle form submission and show a loading spinner
function handleFormSubmit(event) {
    event.preventDefault(); // Prevent default form submission

    const loadingSpinner = document.getElementById("loading");
    const resultSection = document.getElementById("result");
    const predictionResult = document.getElementById("prediction-result");
    const suggestionText = document.getElementById("suggestion");

    if (loadingSpinner && resultSection && predictionResult && suggestionText) {
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
    } else {
        console.error("Some elements are missing in the DOM.");
    }
}

// Dropdown menu functionality
function setupDropdownMenu() {
    const dropdown = document.querySelector('.dropdown');
    if (dropdown) {
        const toggle = dropdown.querySelector('.dropdown-toggle');
        const dropdownContent = dropdown.querySelector('.dropdown-content');

        if (toggle && dropdownContent) {
            toggle.addEventListener('click', (e) => {
                e.preventDefault();
                dropdownContent.classList.toggle('show'); // Toggle dropdown visibility
            });

            // Close dropdown if clicked outside
            document.addEventListener('click', (e) => {
                if (!dropdown.contains(e.target)) {
                    dropdownContent.classList.remove('show');
                }
            });
        } else {
            console.error("Dropdown toggle or content element is missing.");
        }
    }
}

// Attach event listeners
document.addEventListener("DOMContentLoaded", () => {
    const uploadForm = document.getElementById("uploadForm");
    const fileInput = document.querySelector('input[type="file"]');

    if (uploadForm) {
        uploadForm.addEventListener("submit", handleFormSubmit);
    }

    if (fileInput) {
        fileInput.addEventListener("change", (event) => {
            previewImage(event);
        });
    }

    // Initialize dropdown functionality
    setupDropdownMenu();
});
