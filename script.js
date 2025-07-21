function showQuote() {
  fetch('/get-quote')
    .then(res => res.json())
    .then(data => {
      document.getElementById("quote-text").innerText = data.quote;
      document.getElementById("quote-box").classList.remove("hidden");
    });
}

function backToFocus() {
  document.getElementById("quote-box").classList.add("hidden");
}
