# print("add", "subtract", "multiply", "divide", "end")
# operation = input("Please select an operation ")
# num1 = int(input("enter a number "))
# num2 = int(input("enter another number "))

# while True:
#     if operation == "add":
#         print(num1+num2)
#     elif operation == "subtract":
#         print(num1-num2)
#     elif operation == "multiply":
#         print(num1*num2)
#     elif operation == "divide":
#         print(num1/num2)
#     elif operation == "end":
#         break


import os

my_list = []

def clear_console():
    os.system("clear")

def showmenu():
    clear_console()
    print("""
Enter SHOW to view list
Enter REMOVE to remove an item
Enter QUIT to leave program
            """)
    
def showlist(my_list):
    clear_console()
    if len(my_list) == 0:
        print("you have 0 items in your list")
    else:
        print("items in list: \n")
        for n in my_list:
            print(n)

def remove_from_list():
    clear_console()
    print("what would you like to remove? \n")
    item = input("item to remove: ")
    if item in my_list:
        my_list.remove(item)
        clear_console()
        print("removed successfully")

showmenu()
while True:
    user = input("add an item ")
    if user == 'QUIT':
        print("Bye!")
        break
    elif user == 'SHOW':
        showlist(my_list)
    elif user == 'REMOVE':
        remove_from_list(my_list)
    else:
        my_list.append(user)
        

    










    



    
