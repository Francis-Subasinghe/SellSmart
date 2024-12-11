
document.getElementById('predictionForm').addEventListener('submit', async function (e) {
    e.preventDefault();

    const formData = {
        "Row ID": parseInt(document.getElementById('rowID').value),
        "Postal Code": parseInt(document.getElementById('postalCode').value),
        "Quantity": parseInt(document.getElementById('quantity').value),
        "Discount": parseFloat(document.getElementById('discount').value),
        "Profit": parseFloat(document.getElementById('profit').value),
        "Year": parseInt(document.getElementById('year').value),
        "Month": parseInt(document.getElementById('month').value),
        "Day": parseInt(document.getElementById('day').value),
    };

    try {
        const response = await fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify([formData]),
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const result = await response.json();
        document.getElementById('predictionResult').innerText =
            `Predicted Sales: ${result.predictions[0]}`;
    } catch (error) {
        document.getElementById('predictionResult').innerText =
            `Error: ${error.message}`;
    }
});
