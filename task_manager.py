# Compulsory task 1:

# WARNING : each task stored inside the tasks.txt file is now composed by
# 7 elements and no more 6 as before because I added the new element
# "task number". To count and recognize if there are tasks inside the file and
# so on, my program checks if there are 7 elements in each line of the text,
# because I have assumed that a line is considered a task only if it has the
# specific 7 elements. To count the tasks I could have been less strict, but I
# chose this way because I think that a task without the 7 main elements is no
# longer a valid task.

import datetime

# In this program I built 7 functions, one of this 7 is used to get the
# login from the user and the other 6 represent the 6 main voices of the
# user's menu(admin and normal)

# The first function (log_in()). In this function I used  while True
# loops, input variables and if-else statements to check and to get the user
# username and password, giving back messages of errors in case the data
# don't have correspondence into the system. To do the checks I read the
# data from the file "user.txt" with the open() function.


def log_in():

    while True:
        user_name = input("Enter an username: ")
        with open("user.txt", "r") as file:
            button = False
            for user in file:
                if user_name == user.strip().split(", ")[0]:
                    button = True
                    break
        if button:
            break
        else:
            print("We are sorry, your username has not been recognized, please"
                  " try again!")
    while True:
        password = input("Enter a password: ")
        with open("user.txt", "r") as file:
            credentials = f"{user_name}, {password}"
            for credentials_data in file:
                if credentials == credentials_data.strip():
                    print("\nCongratulations, your credentials have "
                          "been recognised, you are logged in.")
                    return user_name
            print("We are sorry, your password has not been "
                  "recognized, please try again!")

# The second function(reg_user()) is used to register new users into the
# system. I also used for this function while True loops, input variables and
# if-else statements to get a new user registration, but previously checking
# that the user doesn't exist already and in case displaying an appropriated
# message of warning. To do the checks I read the data from the file
# "user.txt" with the open() function.


def reg_user():
    print("\nREGISTER A NEW USER:")
    while True:
        button = False  # I used this variable to break two different loops.
        new_user = input("\nEnter a new username: ")
        with open("user.txt", "r") as file:
            for user in file:
                if user.strip().split(",")[0] == new_user:
                    button = True
                    print("Sorry, the user that you are trying to add already"
                          " exists, try again!")
                    break
        if button:
            continue
        new_user_check = input("Enter again the new username: ")
        if new_user == new_user_check:
            break
        else:
            print("The usernames don't match, please try again!")
    while True:
        new_password = input("Enter a new password: ")
        new_password_check = input("Enter again the new password: ")
        if new_password == new_password_check:
            with open("user.txt", "a") as file:
                file.write(f"{new_user}, {new_password}\n")
            print("\nThe operation has been completed!")
            break
        else:
            print("The passwords don't match, please try again!")

# This function (add_task()) is used to create new tasks for the users.
# To build this function I used different user inputs for the tasks elements
# and I imported and called the datetime.now() function from the datetime
# module so that every task has an authomatic current date. In the end, I also
# enumerated each new task in ascending order. To do these operations I used
# the open() function in read and write mode.


def add_task():
    print("\nADD A NEW TASK:")
    c_date = datetime.datetime.now()
    sent_date = f"{c_date.strftime('%d')} {c_date.strftime('%b')}" \
                f" {c_date.strftime('%Y')}"
    user_for_task = input("Enter the user to whom you want to assign the "
                          "task: ")
    task_title = input("Enter the task title: ")
    task_description = input("Enter a task description: ")
    task_due_by = input(
        "Enter the date by which to complete the task(e.g. date "
        "format: 21 Jan 2022): ")
    with open("tasks.txt", "r") as tasks:
        with open("tasks.txt", "a") as file:
            task_num = tasks.read().split("\n")
            file.write(f"{user_for_task}, {task_title}, {task_description}, "
                       f"{sent_date}, {task_due_by}, No, "
                       f"task number: {len(task_num)}\n")
        print("\nThe operation has been completed!")

# The view_all() function is useful when a user needs to check the list of
# general tasks. Each task has 7 elements(indexes), so to print out all the
# tasks I read the file and I checked if the lines had 7 elements. In this
# case a line can be classified as a task. In case there are no tasks, the
# variable counter would be stay equal to zero and no tasks will be printed.


def view_all():
    print("\nLIST OF TASKS: ")
    with open("tasks.txt", "r") as file:
        counter = 0
        for task in file:
            if len(task.strip().split(", ")) == 7:
                counter += 1
                print(f"""\nTask number: {task.strip().split(", ")[-1][-1]}
Task title: {task.strip().split(", ")[1]}
Assigned to: {task.strip().split(", ")[0]}
Date assigned: {task.strip().split(", ")[3]}
Due date: {task.strip().split(", ")[4]}
Task completed? {task.strip().split(", ")[5]}
Task description: {task.strip().split(", ")[2]}""")
        if counter == 0:
            print(
                "\nThere are not tasks at the moment, please try "
                "to check later.")
        else:
            print("\nYou can find all tasks above."
                  " The operation has been completed!")

# The function view_mine() is used when the user wants to check
# the tasks specifically assigned to him/her. When this part of the menu is
# open a sub-menu will be displayed and the program will give to the user
# different options. For example the user can view all tasks assigned as
# we said before but can also check and modify a specific task. In particular
# a second sub-menu will appear if the user decides to view a specific
# task and then will be able to change the user responsible for that task,
# the due date of the task and to mark the task as completed. Notice that
# the program will allow the user to modify a task only if the task has not
# already been marked as completed. To make the task modification I before
# passed all the tasks to a list with the read() function, then I wrote back a
# new file(overwriting the previous one) when the modifications were completed.
# Clearly also in this function there are several loops and conditional
# statements to cover the various menu/sub-menu choices.


def view_mine():

    while True:

        l_tasks = []

        with open("tasks.txt", "r") as f:
            for task in f:
                l_tasks.append(task.strip().split(", "))

        option = input("\nSelect one of the following options:"
                       "\n 1 - view all your tasks"
                       "\n 2 - view a specific task"
                       "\n-1 - to return back to the previous menu"
                       "\nEnter your choice: ")
        if option == "1":
            print("\nLIST OF YOUR TASKS: ")
            with open("tasks.txt", "r") as file:
                counter_2 = 0
                for task in file:
                    if username == task.strip().split(", ")[0]:
                        counter_2 += 1
                        print(f"""\nTask number: {task.strip().split(", ")
                        [-1][-1]}
Task Title: {task.strip().split(", ")[1]}
Assigned to: {task.strip().split(", ")[0]}
Date assigned: {task.strip().split(", ")[3]}
Due date: {task.strip().split(", ")[4]}
Task completed? {task.strip().split(", ")[5]}
Task description: {task.strip().split(", ")[2]}""")
                if counter_2 == 0:
                    print("\nThere are not tasks for you at the moment, try to"
                          " check later.")
                    return
                else:
                    print("\nYou can find all tasks above."
                          " The operation has been completed!")
        elif option == "2":
            with open("tasks.txt", "r") as file:
                counter_3 = 0
                for task in file:
                    if username == task.strip().split(", ")[0]:
                        counter_3 += 1
            if counter_3 != 0:
                task_num = input("Enter the number of the task that you want "
                                 "to display: ")
                with open("tasks.txt", "r") as file:
                    counter_4 = 0
                    for task in file:
                        if task_num == task.strip().split(", ")[-1][-1] and \
                                username == task.strip().split(", ")[0]:
                            counter_4 += 1
                            print(f"""\nTask number: {task.strip().split(", ")
                            [-1][-1]}
    Task Title: {task.strip().split(", ")[1]}
    Assigned to: {task.strip().split(", ")[0]}
    Date assigned: {task.strip().split(", ")[3]}
    Due date: {task.strip().split(", ")[4]}
    Task completed? {task.strip().split(", ")[5]}
    Task description: {task.strip().split(", ")[2]}""")
                if counter_4 == 0:
                    print("\nNo task for you with this parameter was found! "
                          "Be sure that you have tasks assigned checking the "
                          "option 1.")
                if counter_4 != 0:
                    modify = input("\nSelect one of the following options:"
                                   "\n 1 - mark the task as completed"
                                   "\n 2 - edit the task"
                                   "\n - press any other character to go "
                                   "back to"
                                   " the view my task menu"
                                   "\n Enter your choice: ")
                    if modify == "1":
                        for string in l_tasks:
                            if username == string[0] and task_num == string[-1][
                                          -1] and string[5] == "Yes":
                                print("\nThe task ask already been completed!")
                                break
                            elif username == string[0] and task_num == string[
                                          -1][-1] and string[5] == "No":
                                string[5] = "Yes"
                                with open("tasks.txt", "w") as f:
                                    for phrase in l_tasks:
                                        f.write(str(", ".join(phrase)) + "\n")
                                print("\nThe operation has been completed!")
                                break

                    elif modify == "2":
                        for string in l_tasks:
                            if username == string[0] and task_num == string[-1][
                                               -1] and string[5] == "Yes":
                                print("\nYou can't modify the task, it has"
                                      " already been completed!")
                                break
                            elif username == string[0] and task_num == string[
                                                -1][-1] and string[5] == "No":
                                edit = input("\nChoose the parameter to edit: "
                                             "\n1 - username task assignation"
                                             "\n2 - task due date"
                                             "\n- press any other character "
                                             "to go "
                                             "back to the view my task menu"
                                             "\nEnter your choice: ")
                                if edit == "1":
                                    new_charge = input("Enter the new user "
                                                       "responsible for "
                                                       "the task: ")
                                    for phrase in l_tasks:
                                        if username == phrase[0] and \
                                                task_num == phrase[-1][-1]:
                                            phrase[0] = new_charge
                                            with open("tasks.txt", "w") as f:
                                                for period in l_tasks:
                                                    f.write(str(", ".join(
                                                        period)) + "\n")
                                            print("\nThe operation has been "
                                                  "completed!")
                                            break
                                elif edit == "2":
                                    new_due_date = input("Enter the new task "
                                                         "due date(e.g. date "
                                                         "format: 21 Jan "
                                                         "2022): ")
                                    for phrase in l_tasks:
                                        if username == phrase[0] and \
                                                task_num == phrase[-1][-1]:
                                            phrase[4] = new_due_date
                                            with open("tasks.txt", "w") as f:
                                                for period in l_tasks:
                                                    f.write(str(", ".join(
                                                        period)) + "\n")
                                            print("\nThe operation has been "
                                                  "completed!")
                                            break
            else:
                print("\nThere are no task for you at the moment, try to check"
                      " later!")
                return
        elif option == "-1":
            return
        else:
            print("\nYou entered a wrong choice, please try again!")


# The gen_reports() function is used to create/update two different types of
# files.txt that contain different information about the task manager program.
# The first,the task overview file shows specific details about the generality
# of the tasks. The second, the user overview file shows specific details about
# the tasks for each user present inside the system. As before, I used different
# loops, open() function in read and write mode, conditionals statements but
# also something new, the try-except block to avoid the ZeroDivisionError
# in case one or more values at the denominator of few variable were equal to
# zero. One of the main important information of these files is to check if
# the tasks are overdue. To get this check I used the datetime module,
# comparing the current date with the due date of the task; but for this result
# I previously converted the task due date to a specific format recognized by
# the datetime() function.

def gen_reports():
    print("\nGENERATE REPORTS:")

    while True:
        reports = input("\nSelect one of the following options:"
                        "\n 1 - generate/update task overview"
                        "\n 2 - generate/update users overview"
                        "\n-1 - to return back to the previous menu"
                        "\nEnter your choice: ")
        if reports == "1":
            with open("tasks.txt", "r") as data:
                tasks_counter = 0
                completed_tasks = 0
                uncompleted_tasks = 0
                overdue_tasks = 0
                overdue_tasks_not_completed = 0
                for tasks in data:
                    due_date = str(tasks.strip().split(", ")[4])
                    m_num = datetime.datetime.strptime(due_date[3:6],
                                                       '%b').month
                    due_date_conv = datetime.datetime(int(due_date[7:]),
                                                      m_num, int(due_date[0:2]))
                    now = datetime.datetime.now()
                    if len(tasks.strip().split(", ")) == 7:
                        tasks_counter += 1
                    if tasks.strip().split(", ")[5] == "Yes":
                        completed_tasks += 1
                    if tasks.strip().split(", ")[5] == "No":
                        uncompleted_tasks += 1
                    if tasks.strip().split(", ")[5] == "No" \
                            and now > due_date_conv:
                        overdue_tasks_not_completed += 1
                    if now > due_date_conv:
                        overdue_tasks += 1
                try:
                    p_uncompleted_tasks = round((uncompleted_tasks /
                                                 tasks_counter) * 100, 2)
                    p_overdue_tasks = round((overdue_tasks / tasks_counter)
                                            * 100, 2)
                except ZeroDivisionError:
                    p_uncompleted_tasks = 0
                    p_overdue_tasks = 0
            with open("task_overview.txt", "w") as file:
                file.write(f"The total number of tasks generated and tracked "
                           f"is: {tasks_counter}\n")
                file.write(f"The total number of completed tasks "
                           f"is: {completed_tasks}\n")
                file.write(f"The total number of uncompleted tasks "
                           f"is: {uncompleted_tasks}\n")
                file.write(f"The total number of tasks that haven't been "
                           f"completed and are overdue "
                           f"is: {overdue_tasks_not_completed}\n")
                file.write(f"The percentage of tasks that are "
                           f"incomplete is: {p_uncompleted_tasks} %\n")
                file.write(f"The percentage of tasks that are "
                           f"overdue is: {p_overdue_tasks} %\n")
            print("\nThe operation has been completed!")
        elif reports == "2":
            with open("user.txt", "r") as data:
                users_counter = 0
                for users_num in data:
                    if len(users_num.strip().split(", ")[0]) >= 1:
                        users_counter += 1
            with open("tasks.txt", "r") as data:
                tasks_counter = 0
                for tasks_num in data:
                    if len(tasks_num.strip().split(", ")) == 7:
                        tasks_counter += 1
            with open("user_overview.txt", "w") as file:
                file.write(f"The total number of registered users "
                           f"is: {users_counter}\n")
                file.write(f"The total number of tasks generated and tracked "
                           f"is: {tasks_counter}\n")
            with open("user.txt", "r") as file:
                for user in file:
                    with open("tasks.txt", "r") as data:
                        tasks_counter = 0
                        user_tasks_counter = 0
                        completed_tasks = 0
                        uncompleted_tasks = 0
                        overdue_tasks = 0
                        overdue_tasks_not_completed = 0
                        for tasks in data:
                            due_date = str(tasks.strip().split(", ")[4])
                            m_num = datetime.datetime.strptime(due_date[3:6],
                                                               '%b').month
                            due_date_conv = datetime.datetime(int(due_date[7:]),
                                                              m_num,
                                                              int(due_date[
                                                                  0:2]))
                            now = datetime.datetime.now()
                            if len(tasks.strip().split(", ")) == 7:
                                tasks_counter += 1
                            if len(tasks.strip().split(", ")) == 7 and \
                                    user.strip().split(", ")[0] == \
                                    tasks.strip().split(", ")[0]:
                                user_tasks_counter += 1
                            if tasks.strip().split(", ")[5] == "Yes" and \
                                    user.strip().split(", ")[0] == \
                                    tasks.strip().split(", ")[0]:
                                completed_tasks += 1
                            if tasks.strip().split(", ")[5] == "No" and \
                                    user.strip().split(", ")[0] == \
                                    tasks.strip().split(", ")[0]:
                                uncompleted_tasks += 1
                            if tasks.strip().split(", ")[5] == "No" \
                                    and now > due_date_conv and \
                                    user.strip().split(", ")[0] == \
                                    tasks.strip().split(", ")[0]:
                                overdue_tasks_not_completed += 1
                            if now > due_date_conv and user.strip().split(", ")[
                                    0] == tasks.strip().split(", ")[0]:
                                overdue_tasks += 1
                        try:
                            p_total_task = round((user_tasks_counter /
                                                  tasks_counter) * 100, 2)
                            p_user_task_completed = round((
                                completed_tasks / user_tasks_counter) * 100, 2)
                            p_user_task_not_completed = round((
                               uncompleted_tasks / user_tasks_counter) * 100, 2)
                            p_uncompleted_tasks_overdue = round(
                                (overdue_tasks_not_completed /
                                 user_tasks_counter) * 100, 2)
                        except ZeroDivisionError:
                            p_total_task = 0
                            p_user_task_completed = 0
                            p_user_task_not_completed = 0
                            p_uncompleted_tasks_overdue = 0
                        with open("user_overview.txt", "a") as f:
                            f.write(f"\nUSER REPORT FOR:"
                                    f" {user.strip().split(', ')[0]}\n")
                            f.write(f"Total number of tasks "
                                    f"assigned: {user_tasks_counter}\n")
                            f.write(f"Percentage of tasks "
                                    f"assigned: {p_total_task} %\n")
                            f.write(f"Percentage of tasks "
                                    f"completed: {p_user_task_completed} %\n")
                            f.write(f"Percentage of tasks not"
                                    f" completed: {p_user_task_not_completed}"
                                    f" %\n")
                            f.write(f"Percentage of tasks not completed and"
                                    f" overdue: {p_uncompleted_tasks_overdue}"
                                    f" %\n")
            print("\nThe operation has been completed!")
        elif reports == "-1":
            return
        else:
            print("\nYou entered a wrong choice, please try again!")

#In the end, the statistics() function is called when the user choose to display
# the statistics about the task manager. In this section the user can decide to
# display which of the two reports file(task and user overview). If the reports
# haven't been generated yet the function will call the gen_reports() function
# and the user then can generate the reports and to display them on the console.
# Another option of this function is to update the reports in case they are
# not updated, to do this we can call again the gen_reports() function and
# then to display the new reports using the statistics() function. In case
# we want to generate the reports or update them through the statistics()
# function, once the operation has been completed we can close the gen_reports()
# function entering the value "-1" and to go back to the statistics() function
# to view the results without passing through the main menu.


def statistics():
    print("\nSTATISTICS:")
    while True:
        reports = input("\nSelect one of the following options:"
                        "\n 1 - display task overview report"
                        "\n 2 - display user overview report"
                        "\n 3 - update statistics"
                        "\n-1 - to return back to the previous menu"
                        "\nEnter your choice: ")
        if reports == "1":
            try:
                with open("task_overview.txt", "r") as file:
                    print("\nTASK REPORT OVERVIEW:")
                    print("\n" + file.read())
            except FileNotFoundError:
                print("\nThe file that you are trying to open doesn't exist, "
                      "you are redirected to "
                      "the 'generate reports' section!")
                gen_reports()

        elif reports == "2":
            try:
                with open("user_overview.txt", "r") as file:
                    print("\nUSER REPORT OVERVIEW:")
                    print("\n" + file.read())
            except FileNotFoundError:
                print("\nThe file that you are trying to open "
                      "doesn't exist, you are redirected to"
                      " the 'generate reports' section!")
                gen_reports()
        elif reports == "3":
            print("\nUpdate the statistics generating more recent files.")
            gen_reports()
        elif reports == "-1":
            return
        else:
            print("\nYou entered a wrong choice, please try again!")


print("\nWELCOME TO THE LOGIN SECTION!")
print()

# Based on which type of user is logged-in the program will display a different
# type of menu; a simplified version in case is a normal user, an articulated
# version in case the user is the admin. To get the username recognized by
# the program I stored the log_in() function into the username variable,
# returning the username input value from the log_in() function.

username = log_in()

# Here we can see the two different models of menu.
if username == "admin":
    menu = """\nSELECT ONE OF THE FOLLOWING OPTIONS FROM THE LIST BELOW:
r - register user
a - add task 
va - view all tasks
vm - view my tasks
gr - generate reports
ds - display statistics
e - exit """
else:
    menu = """\nMENU, SELECT ONE OF THE FOLLOWING OPTIONS FROM THE LIST BELOW:
a - add task
va - view all tasks
vm - view my tasks
e - exit """

# In the end, using a while True loop I displayed the menu to the user, based
# on which type of user is logged-in. Using a big if-elif-else statement
# structure we can call and run all the different functions that compose the
# menu depending on which menu voice the user chooses.
while True:
    print(menu)
    choice = input("enter your choice: ").lower()

    if choice == 'r' and username == "admin":
        reg_user()

    elif choice == "gr" and username == "admin":
        gen_reports()

    elif choice == "ds" and username == "admin":
        statistics()
    elif choice == 'a':
        add_task()

    elif choice == 'va':
        view_all()

    elif choice == 'vm':
        view_mine()

    elif choice == 'e':
        print("\nThank you, goodbye!!!")
        exit()

    else:
        print("\nYou have made a wrong choice, please try again!")
