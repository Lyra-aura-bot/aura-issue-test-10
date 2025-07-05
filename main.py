import sys
from storage import load_todos, save_todos
from todo import TodoItem

COMMANDS = ['list', 'add', 'done']


def list_todos():
    todos = load_todos()
    if not todos:
        print("No to-dos!")
    for idx, todo in enumerate(todos, start=1):
        print(f"{idx}. {todo}")


def add_todo(title):
    todos = load_todos()
    todos.append(TodoItem(title))
    save_todos(todos)
    print(f"Added: {title}")


def mark_done(index):
    todos = load_todos()
    try:
        item = todos[index]
        item.mark_done()
        save_todos(todos)
        print(f"Marked done: {item.title}")
    except IndexError:
        print("Error: No to-do with that index.")


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in COMMANDS:
        print("Usage: python main.py <list|add|done> [arguments]")
        return

    cmd = sys.argv[1]
    if cmd == 'list':
        list_todos()
    elif cmd == 'add':
        if len(sys.argv) < 3:
            print("Error: Missing to-do title.")
        else:
            add_todo(' '.join(sys.argv[2:]))
    elif cmd == 'done':
        if len(sys.argv) < 3:
            print("Error: Missing to-do index.")
        else:
            index = int(sys.argv[2])
            mark_done(index)


if __name__ == '__main__':
    main()