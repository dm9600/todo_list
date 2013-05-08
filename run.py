#Avoiding .pyc files because they're annoying
import sys
sys.dont_write_bytecode = True

# Starts a new TodoList instance
from todo_functions import *
from io_functions import *
import todo
import todolist

newTodoList()
