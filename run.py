#Avoiding .pyc files because they're annoying
import sys
sys.dont_write_bytecode = True

# Starts a new TodoList instance
from todo_functions import *
from io_functions import *
import todo
import todolist

def main():
    newTodoList()

if __name__ == "__main__":
    main()
