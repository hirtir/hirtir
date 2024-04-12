document.addEventListener('DOMContentLoaded', function() {
    var supportToggle = document.getElementById('support-toggle');
    var questionFormContainer = document.getElementById('question-form-container');
  
    // При клике на кружок
    supportToggle.addEventListener('click', function() {
      // Если окно поддержки уже открыто, закрываем его
      if (questionFormContainer.style.display === 'block') {
        questionFormContainer.style.opacity = '0'; // Делаем окно полупрозрачным
        setTimeout(function() {
          questionFormContainer.style.display = 'none'; // Скрываем окно поддержки
        }, 300); // Ждем окончания анимации
      } else {
        // Иначе открываем его
        questionFormContainer.style.display = 'block'; // Показываем окно поддержки
        setTimeout(function() {
          questionFormContainer.style.opacity = '1'; // Делаем окно непрозрачным
        }, 0); // Выполняем это немедленно
      }
    });
  });
  