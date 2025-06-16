from lib.todo_list import TodoList
from lib.todo import Todo


'''
Add a todo to list
'''
def test_add_todo_to_list():
    todo_list = TodoList()
    todo = Todo("Learn Git")
    todo_list.add(todo)
    assert todo in todo_list.incomplete()


'''
Only returns incomplete todos
'''
def test_returns_incomplete_todos_only():
    todo1 = Todo("Task 1")
    todo2 = Todo("Task 2")
    todo2.mark_complete()
    todo_list = TodoList()
    todo_list.add(todo1)
    todo_list.add(todo2)
    assert todo1 in todo_list.incomplete()
    assert todo2 not in todo_list.incomplete()

'''
Only returns complete todos
'''

def test_returns_complete_todos_only():
    todo1 = Todo("Task 1")
    todo2 = Todo("Task 2")
    todo1.mark_complete()
    todo_list = TodoList()
    todo_list.add(todo1)
    todo_list.add(todo2)
    assert todo1 in todo_list.complete()
    assert todo2 not in todo_list.complete()

'''
All complete (give up marks all)
'''

def test_give_up_marks_all_complete():
    todo1 = Todo("Sleep")
    todo2 = Todo("Eat")
    todo_list = TodoList()
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.give_up()
    assert all(t.complete for t in todo_list.complete())