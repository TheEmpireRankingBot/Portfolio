(() => {
  const chipGroup = document.querySelector('.chips');
  if (chipGroup) {
    const chips = chipGroup.querySelectorAll('.chip');
    chips.forEach((chip) => {
      chip.addEventListener('click', () => {
        chips.forEach((c) => c.setAttribute('aria-pressed', 'false'));
        chip.setAttribute('aria-pressed', 'true');
      });
    });
  }

  const form = document.querySelector('.form');
  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const btn = form.querySelector('.form__submit span');
      if (!btn) return;
      const original = btn.textContent;
      btn.textContent = 'Received — we will be in touch';
      form.querySelectorAll('input, select, button').forEach((el) => {
        el.disabled = true;
      });
      setTimeout(() => {
        btn.textContent = original;
      }, 6000);
    });
  }
})();
