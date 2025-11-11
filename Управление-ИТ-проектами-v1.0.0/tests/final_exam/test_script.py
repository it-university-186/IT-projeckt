import json, pathlib, sys

def check(answers: dict) -> int:
    here = pathlib.Path(__file__).parent
    correct = json.loads((here / "answers.json").read_text(encoding="utf-8"))
    return sum(1 for k, v in correct.items() if answers.get(k) == v)

if __name__ == "__main__":
    # пример: студент может локально подставить свои ответы
    demo = {
        "1": "Fork → Ветка → PR → Автотесты → Ревью → Merge",
        "2": "Нужны правки перед принятием"
    }
    print("Score:", check(demo), "/ 2")
