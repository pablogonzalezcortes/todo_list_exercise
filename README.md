Todo List (TDD Project)

This is a simple Python project developed using Test-Driven Development (TDD). It consists of two core classes: Todo and TodoList. The aim of this project is to practise writing clean, testable code by following the TDD cycle: Red → Green → Refactor.

Features:
✅ Create todo items with a task description

✅ Mark tasks as complete

✅ Add tasks to a todo list

✅ View complete and incomplete tasks

✅ Give up and mark all tasks as complete

Technologies Used:
-Python 3
-Pytest for testing

Running the Tests:
Make sure you have pytest installed:

pip install pytest

Then, run the tests from the root of the project:

pytest


Project Structure:

project/
│
├── lib/
│   ├── todo.py          # The Todo class
│   └── todo_list.py     # The TodoList class
│
└── tests/
    ├── test_todo.py     # Unit tests for Todo
    └── test_todo_list.py # Unit tests for TodoList

Purpose:
This project was built as part of a learning exercise to better understand:

-Object-oriented programming in Python

-Writing effective unit tests

-Applying the TDD methodology

Author:
Developed by Pablo Gonzalez
