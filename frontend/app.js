
const button = document.getElementById("calculate");
const resultElement = document.getElementById("result");

button.addEventListener("click", async () => {
    const aInput = document.getElementById("a");
    const bInput = document.getElementById("b");
    const operation = document.getElementById("operation").value;

    if (
        aInput.value.trim() === "" ||
        bInput.value.trim() === "" ||
        !Number.isFinite(Number(aInput.value)) ||
        !Number.isFinite(Number(bInput.value))
    ) {
        resultElement.textContent = "Enter two valid numbers.";
        return;
    }

    button.disabled = true;
    resultElement.textContent = "Calculating...";

    try {
        const response = await fetch("/api/calculate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                a: Number(aInput.value),
                b: Number(bInput.value),
                operation
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || "Calculation failed");
        }

        resultElement.textContent = `Result: ${data.result}`;
    } catch (error) {
        resultElement.textContent = `Error: ${error.message}`;
    } finally {
        button.disabled = false;
    }
});
