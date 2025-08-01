# 🏃‍♂️ Fitness Tracker Module - Модуль фитнес-трекера

Программный модуль для фитнес-трекера, который обрабатывает данные и рассчитывает результаты тренировок для трёх типов активности: **бег**, **спортивная ходьба**, **плавание**.

---

## 🚀 Возможности

Программа моделирует работу фитнес-трекера:

- Поддерживает 3 вида тренировок:
  - 🏃‍♂️ Бег (Running)
  - 🚶‍♂️ Спортивная ходьба (SportsWalking)
  - 🏊‍♂️ Плавание (Swimming)
- Рассчитывает основные показатели:
  - Пройденная дистанция (км)
  - Средняя скорость (км/ч)
  - Потраченные калории
- Формирует детальный отчёт о тренировке

---

## 📦 Установка

```bash
git clone https://github.com/your-username/Fitness-tracker-module.git
cd Fitness-tracker-module
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows
pip install -r requirements.txt
```

## ▶️ Запуск

```bash
python main.py
```

## 🧪 Тестирование

```bash
pytest
```

## 📁 Структура проекта

```
Fitness-tracker-module/
├── main.py               # Точка входа в программу: обработка тренировок и вывод результатов
├── tests/                # Каталог с тестами
│   ├── conftest.py       # Общие фикстуры для тестов (если нужны)
│   └── test_main.py      # Модульные тесты для проверки работы основного кода
├── requirements.txt      # Список зависимостей проекта
├── pytest.ini            # Конфигурация pytest
├── .flake8               # Настройки линтера flake8 для проверки стиля кода
├── .gitignore            # Файлы и папки, исключаемые из Git-репозитория
├── README.md             # Документация по проекту
└── setup.cfg             # Общая конфигурация проекта
```
## Результат тестирования
!(https://github.com/BEZBIG/Fitness-tracker-module/blob/main/tests/test_results.png)