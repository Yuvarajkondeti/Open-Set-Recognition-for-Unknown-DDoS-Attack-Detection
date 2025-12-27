function detect() {

  // 🔑 MUST MATCH TRAINING FEATURES (79)
  let features = Array.from({ length: 79 }, () => Math.random());

  fetch("http://127.0.0.1:5000/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ features: features })
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("output").innerHTML =
      `Prediction: ${data.prediction}<br>Distance: ${data.distance}`;
  });
}
