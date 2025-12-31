function detect() {
  const output = document.getElementById("output");
  output.innerHTML = "⏳ Analyzing traffic...";

  // MUST match trained model input size
  let features = Array.from({ length: 79 }, () => Math.random());

  fetch("http://127.0.0.1:5000/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ features })
  })
  .then(res => res.json())
  .then(data => {
    let cssClass = "safe";

    if (data.prediction.toLowerCase().includes("unknown")) {
      cssClass = "unknown";
    } else if (data.prediction.toLowerCase().includes("attack")) {
      cssClass = "known";
    }

    output.innerHTML = `
      <div class="${cssClass}">
        <strong>Prediction:</strong> ${data.prediction}<br>
        <strong>Distance:</strong> ${data.distance.toFixed(3)}
      </div>
    `;
  })
  .catch(() => {
    output.innerHTML = "❌ Backend not reachable";
  });
}
