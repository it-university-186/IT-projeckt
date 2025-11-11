import json, pathlib

def check(answers: dict) -> int:
    here = pathlib.Path(__file__).parent
    correct = json.loads((here / "answers.json").read_text(encoding="utf-8"))
    return sum(1 for k, v in correct.items() if answers.get(k) == v)

if __name__ == "__main__":
    demo = {
        "1": "Копирует удалённый репозиторий на локальный компьютер",
        "2": "Запрос на слияние изменений"
    }
    print("Score:", check(demo), "/ 2")
