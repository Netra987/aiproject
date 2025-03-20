function solveEquation() {
    const equation = document.getElementById("equationInput").value;
    
    fetch('/solve', {
        method: 'POST',
        body: JSON.stringify({ equation }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("solution").innerHTML = JSON.stringify(data.solution, null, 2);
    })
    .catch(error => console.error('Error:', error));
}
