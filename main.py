__author__ = 'rob00000'
#this program can accept 4 options.
#1. show all employees
#2. Add new employee
#3. delete existing
#4. find employee
#5. quit/exit program

# input to the console

employee_db = {"Rob" : 39, "Amit" : 33, "Bruce" : 50, "Terry" : 51, "Harbie" : 29}

print employee_db["Rob"]

def show_all():
    print "show_all"

def add_employee(name, age):
    print "add_employee"

def delete_employee():
    print "delete_employee"

def find_employee():
    print "find_employee"

def exit():
    print "exit"


print "Welcome to Employee Database System"
while True:
    def menu_options():
        print "1. Show All Employees" + "\n" + "2. Add New Employee" + "\n" + "3. Delete Existing Employee" + "\n" + "4. Find Employees" + "\n" + "5. Exit Employee Database";
        selection = raw_input("Enter a number 1-5 ");
        return selection;

    user_selection = int(menu_options())

    print user_selection

    if user_selection == 1:
        show_all()

    elif user_selection == 2:
        add_employee()

    elif user_selection == 3:
        delete_employee()

    elif user_selection == 4:
        find_employee()

    elif user_selection == 5:
        print "Good-bye"
        break


