document.addEventListener('DOMContentLoaded', () => {
    const jsonInput = document.getElementById('jsonInput');
    const xmlOutput = document.getElementById('xmlOutput');
    const convertBtn = document.getElementById('convertBtn');
    const loadExampleBtn = document.getElementById('loadExampleBtn');
    const copyBtn = document.getElementById('copyBtn');
    const errorMessage = document.getElementById('errorMessage');

    // Example JSON Data
    const exampleData = {
        "organization": {
            "name": "Securin",
            "type": "Inc",
            "building_number": 4,
            "floating": -17.4,
            "null_test": null
        },
        "security_related": true,
        "array_example0": ["red", "green", "blue", "black"],
        "array_example1": [1, "red", [{"nested": true}], {"obj": false}]
    };

    // Load example data into the textarea
    loadExampleBtn.addEventListener('click', () => {
        jsonInput.value = JSON.stringify(exampleData, null, 4);
        errorMessage.classList.add('hidden');
    });

    // Copy XML to clipboard
    copyBtn.addEventListener('click', () => {
        if (xmlOutput.value) {
            navigator.clipboard.writeText(xmlOutput.value);
            const originalText = copyBtn.innerText;
            copyBtn.innerText = "Copied!";
            setTimeout(() => { copyBtn.innerText = originalText; }, 2000);
        }
    });

    // Main Conversion Logic (API Integration)
    convertBtn.addEventListener('click', async () => {
        const jsonText = jsonInput.value.trim();
        if (!jsonText) return;

        let parsedJson;
        try {
            // Step 1: Validate JSON locally
            parsedJson = JSON.parse(jsonText);
            errorMessage.classList.add('hidden');
        } catch (e) {
            errorMessage.innerText = "Invalid JSON Format!";
            errorMessage.classList.remove('hidden');
            return;
        }

        // Step 2: Make API Request to Python Backend
        try {
            convertBtn.disabled = true;
            xmlOutput.value = "Converting...";

            // API INTEGRATION happens here:
            const response = await fetch('/api/convert', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(parsedJson) // Send data to server
            });

            const data = await response.json();

            // Step 3: Handle the Server Response
            if (response.ok) {
                // Success! Display the XML
                xmlOutput.value = data.xml;
            } else {
                // Server returned an error
                errorMessage.innerText = `Server Error: ${data.error}`;
                errorMessage.classList.remove('hidden');
                xmlOutput.value = "";
            }

        } catch (error) {
            errorMessage.innerText = "Network Error: Could not connect to the API.";
            errorMessage.classList.remove('hidden');
            xmlOutput.value = "";
        } finally {
            convertBtn.disabled = false;
        }
    });
});
