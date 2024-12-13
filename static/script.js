document.getElementById('myForm').addEventListener('submit', async function(event) {
    event.preventDefault(); // Prevent default form submission

    const selectedModel = document.getElementById('model').value;
    const selectedVectorizer = document.getElementById('vectorizer').value;
    const inputText = document.getElementById('inputText').value;
    const resultContainer = document.getElementById('result');
    const data = {
        model: selectedModel,
        vectorizer: selectedVectorizer,
        text: inputText
    };
    
    try {
        const response = await fetch('http://127.0.0.1:5000/submit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });
        resultContainer.innerText="Loading...";

        if (response.ok) {
            const result = await response.json();
            resultContainer.innerText=result.category;
        } else {
            resultContainer.innerText=result.statusText;
        }
    } catch (error) {
        resultContainer.innerText=error.message;
    }
});
