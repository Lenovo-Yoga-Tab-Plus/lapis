(function () {
  var button = document.getElementById("theme-toggle");
  if (!button) return;

  function apply(theme) {
    document.documentElement.dataset.theme = theme;
    try { localStorage.setItem("lapis-theme", theme); } catch (error) {}
    button.setAttribute("aria-pressed", theme === "dark" ? "true" : "false");
  }

  button.addEventListener("click", function () {
    apply(document.documentElement.dataset.theme === "dark" ? "light" : "dark");
  });
  apply(document.documentElement.dataset.theme || "dark");
})();
