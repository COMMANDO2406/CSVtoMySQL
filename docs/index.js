document.querySelectorAll("nav a").forEach((link) => {
  link.addEventListener("click", function (event) {
    event.preventDefault();
    const doc = this.getAttribute("data-doc");
    document.querySelector("zero-md").src = `my-docs/${doc}`;
  });
});
