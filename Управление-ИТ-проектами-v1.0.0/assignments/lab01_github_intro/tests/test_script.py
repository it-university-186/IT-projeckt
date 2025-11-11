import json, sys, pathlib

def grade(user_answers: dict) -> int:
    here = pathlib.Path(__file__).parent
    with open(here / "answers.json", encoding="utf-8") as f:
        correct = json.load(f)
    score = 0
    for k, v in correct.items():
        if user_answers.get(k) == v:
            score += 1
    return score

if __name__ == "__main__":
    # Пример локальной проверки (студент может заменить свой словарь ответов):
    user_answers = {
        "1": "Запрос на слияние изменений в основную ветку",
        "2": "В Issues"
    }
    print(f"Результат: {grade(user_answers)}/{2}")
