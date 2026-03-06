const input = document.getElementById("imageInput");
const preview = document.getElementById("preview");

preview.style.display = "none";

input.addEventListener("change", function (event) {
    const file = event.target.files[0];

    if (file) {
        preview.src = URL.createObjectURL(file);
        preview.style.display = "block";
    }
});