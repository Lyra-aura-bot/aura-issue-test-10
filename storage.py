import json
from todo import TodoItem

STORAGE_FILE = 'todos.json'


def load_todos():
    try:
        with open(STORAGE_FILE, 'r') as f:
            data = json.load(f)
            return [TodoItem(**item) for item in data]
    except FileNotFoundError:
        return []


def save_todos(todos):
    with open(STORAGE_FILE, 'w') as f:
        data = [{'title': t.title, 'completed': t.completed} for t in todos]
        json.dump(data, f, indent=2)
