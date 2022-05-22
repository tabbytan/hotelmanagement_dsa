def menu():
    print("Welcome to hotel management system1.\n "
          "1. Display all records\n"
          "2. Sort record by Customer Name using Bubble sort\n"
          "3. Sort record by Package Name using Selection sort\n"
          "4. Sort record by Package Cost using Insertion sort\n"
          "5. Search record by Customer Name using Linear Search and update record\n"
          "6. Search record by Package Name using Binary Search and update record\n"
          "7. List records range from $X to $Y. e.g $100-200\n"
          "0. Exit Application")
    option = input("Insert choice here:")
    return option


class Record:
    def __init__(self, PackageName, CustomerName, NumberOfPax, PackageCostPerPax):
        self.PackageName = PackageName
        self.CustomerName = CustomerName
        self.NumberOfPax = NumberOfPax
        self.PackageCostPerPax = PackageCostPerPax


dict = {}


def option1():
    for item in dict:
        print(item.value)


def option2():
    pass


def option3():
    pass


def option4():
    pass


def option5():
    pass


def option6():
    pass


def option7():
    pass


# main menu loop
menuflag = True
while menuflag:
    choice = menu()
    if choice == "1":
        option1()
    elif choice == "3":
        option3()
    elif choice == "4":
        option4()
    elif choice == "5":
        option5()
    elif choice == "6":
        option6()
    elif choice == "7":
        option7()
    elif choice == "0":
        exit()
