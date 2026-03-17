// Quick-add buttons on add_food page
document.querySelectorAll('.quick-add').forEach(btn => {
  btn.addEventListener('click', () => {
    const set = (selector, val) => {
      const el = document.querySelector(selector);
      if (el) el.value = val;
    };
    set('#id_name',    btn.dataset.name);
    set('#id_calories', btn.dataset.cal);
    set('#id_protein',  btn.dataset.pro);
    set('#id_carbs',    btn.dataset.carb);
    set('#id_fats',     btn.dataset.fat);
    document.querySelector('#id_name')?.focus();
  });
});

// Auto-dismiss alerts after 4s
document.querySelectorAll('.alert').forEach(alert => {
  setTimeout(() => {
    const bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
    bsAlert.close();
  }, 4000);
});

// Animate progress bars on load
window.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.progress-bar').forEach(bar => {
    const target = bar.style.width;
    bar.style.width = '0%';
    bar.style.transition = 'width 0.8s ease';
    requestAnimationFrame(() => {
      setTimeout(() => { bar.style.width = target; }, 80);
    });
  });
});
