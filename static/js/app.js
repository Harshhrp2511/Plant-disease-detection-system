document.querySelector('input[type="file"]').addEventListener('change', (event) => {
    const fileName = event.target.files[0].name;
    alert(`File selected: ${fileName}`);
});
