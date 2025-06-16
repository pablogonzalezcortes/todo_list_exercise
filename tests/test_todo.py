from lib.todo import Todo

#Tests


'''
When todo starts incomplete
check if it returns False
'''

def test_when_starts_incomplete():
    todo = Todo("Learn TDD")
    assert todo.task == "Learn TDD"
    assert todo.complete == False

