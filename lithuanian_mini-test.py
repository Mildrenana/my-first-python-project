words = {
    "Labas": "Привет",
    "Ačiū": "Спасибо",
    "Mokykla": "Школа",
    "Programuotojas": "Программист",
"Vienas": "Один",
    "Du": "Два",
    "Trys": "Три",
    "Keturi": "Четыре",
    "Penki": "Пять",
    "Šeši": "Шесть",
    "Septyni": "Семь",
    "Aštuoni": "Восемь",
    "Devyni": "Девять",
    "Dešimt": "Десять"
}

print("--- Мини-тест по литовскому ---")
for lit, rus in words.items():
    answer = input(f"Как переводится '{lit}'? ")
    if answer.lower() == rus.lower():
        print("Правильно! ✅")
    else:
        print(f"Ошибка. Правильный ответ: {rus} ❌")
