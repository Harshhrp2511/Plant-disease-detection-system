function previewImage(event) {
    const file = event.target.files[0];
    if (!file) {
        alert("Please select a file to preview.");
        return;
    }
    const validImageTypes = ["image/jpeg", "image/png", "image/gif"];
    if (!validImageTypes.includes(file.type)) {
        alert("Invalid file type. Please upload an image file (JPEG, PNG, or GIF).");
        return;
    }
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
document.addEventListener("DOMContentLoaded", () => {
    const uploadForm = document.getElementById("uploadForm");
    const fileInput = document.querySelector('input[type="file"]');
    if (uploadForm) {
        uploadForm.addEventListener("submit", handleFormSubmit);
    }
    if (fileInput) {
        fileInput.addEventListener("change", previewImage);
    }
});
