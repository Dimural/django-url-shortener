

// Function to copy the shortened URL to the clipboard
function copyToClipboard() {
    let inputField = document.getElementById("shortened-url");
    if (navigator.clipboard) {
        navigator.clipboard.writeText(inputField.value).then(() => {
        }).catch(err => {
            console.error("Failed to copy: ", err);
        });
    } else {
        // Fallback method for older browsers (i only added this since it was recommended on google)
        inputField.select();
        document.execCommand("copy");
    }
}



