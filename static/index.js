document.addEventListener("DOMContentLoaded", function () {
    const calculateBtn = document.getElementById("calculateBtn");
    const heightInput = document.getElementById("height");
    const weightInput = document.getElementById("weight");
    const resultDiv = document.getElementById("result");

    calculateBtn.addEventListener("click", function () {
        const height = parseFloat(heightInput.value);
        const weight = parseFloat(weightInput.value);

        if (isNaN(height) || isNaN(weight) || height <= 0 || weight <= 0) {
            resultDiv.innerText = "Please enter valid height and weight values.";
        } else {
            const bmi = calculateBMI(height, weight);
            resultDiv.innerText = `Your BMI is: ${bmi.toFixed(2)}`;
        }
    });

    function calculateBMI(height, weight) {
        return weight / ((height / 100) ** 2);
    }
});