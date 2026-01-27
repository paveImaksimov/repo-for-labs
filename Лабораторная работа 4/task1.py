# TODO решите задачу
import json


def task() -> float:
    with open('input.json') as f:
        json_data = json.load(f)
        return round(sum([dict['score']*dict['weight'] for dict in json_data]), 3)


print(task())
