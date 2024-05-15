#global list that will store todo items
todo_list = []

#add a todo function 
#append is used to add an element to an array
def addItem(item):
    todo_list.append(item)
    print(f"Added: {item}, to your todo list")

#remove todo from list
#remove is used to remove an element from a list 
#need try, except to check for errors

def delete(item):
    try:
        todo_list.remove(item)
        print(f'Removed: {item}, from your todo list')
    except ValueError:
        print(f'Item: {item}, not found in your to-do list :()')

#list todos and their index
def listTodos():
    print('To-Do List:')
    for i, item in enumerate(todo_list):
        print(f'{i}, {item}')

#displays a menu with options to user
def display_menu():
    print("\nTo-Do List Menu")
    print("1. Add item")
    print("2. Mark item as completed")
    print("3. Show to-do list")
    print("4. Quit")


#main function 

def main():
    while True: 
        display_menu()
        try: 
            choice = int(input('Enter your choice (1-4): ').strip())
        except ValueError:
            print('Invalid input. Please enter a number between 1 and 4')
            continue
        if choice == 1:
            item = input('Enter the item to add: ').

