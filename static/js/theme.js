// Theme toggle functionality
(function() {
  const themeToggle = document.querySelector('#theme-toggle');
  if (!themeToggle) return;

  const preferDark = window.matchMedia("(prefers-color-scheme: dark)");

  function toggleTheme(theme) {
    if (theme === "dark") {
      document.body.classList.add('dark');
    } else {
      document.body.classList.remove('dark');
    }
    sessionStorage.setItem("theme", theme);
  }

  // Handle theme toggle button click
  themeToggle.addEventListener('click', () => {
    const currentTheme = sessionStorage.getItem("theme");
    const isDark = document.body.classList.contains('dark');
    const newTheme = isDark ? "light" : "dark";
    toggleTheme(newTheme);
  });

  // Listen for system preference changes
  preferDark.addEventListener("change", e => {
    if (!sessionStorage.getItem("theme")) {
      toggleTheme(e.matches ? "dark" : "light");
    }
  });

  // Initialize theme on page load
  const savedTheme = sessionStorage.getItem("theme");
  if (savedTheme) {
    toggleTheme(savedTheme);
  } else if (preferDark.matches) {
    toggleTheme("dark");
  }
})();
