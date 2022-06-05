
import random


def update(name):
    print(f'1.package name\n2.customer name\n3.no of pax\n4.packagecost per pax ')
    attribute = input("change which attribute?").lower()
    name = name.lower()
    if attribute == '1':
        for item in list:
            if name == item.CustomerName:
                item.PackageName = input("Change package name here: ")
    elif attribute == '2':
        for item in list:
            if name == item.CustomerName:
                item.CustomerName = input("change customer name here: ")
    elif attribute == '3':
        for item in list:
            if name == item.CustomerName:
                validation = True
                while validation:
                    value = input('insert no of pax here')
                    if value.isnumeric():
                        item.NumberOfPax = value
                        item.totalprice = item.NumberOfPax * item.PackageCostPerPax
                        validation = False
                    else:
                        print('error not a number')
    elif attribute == '4':
        for item in list:
            if name == item.CustomerName:
                validation = True
                while validation:
                    value = input('insert no of pax here')
                    if value.isnumeric():
                        item.PackageCostPerPax = value
                        item.totalprice = item.PackageCostPerPax * item.NumberOfPax
                        validation = False
                    else:
                        print('error not a number')


class Record:
    def __init__(self, PackageName, CustomerName, NumberOfPax, PackageCostPerPax):
        self.PackageName = PackageName
        self.CustomerName = CustomerName
        self.NumberOfPax = NumberOfPax
        self.PackageCostPerPax = PackageCostPerPax
        self.totalprice = NumberOfPax*PackageCostPerPax

    def __str__(self):
        return f'\nPackagename: {self.PackageName}\nCustomer Name: {self.CustomerName}\n Number of pax: {self.NumberOfPax}\n Package cost: {self.PackageCostPerPax}\n Total price: {self.totalprice}\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-='

    __repr__ = __str__


list = [Record("normal", "frank", 2, 900),
        Record("advanced", 'richard', 4, 2700),
        Record("suite", 'smith', 3, 2500),
        Record("suite", 'alex', 2, 2500)]


def option1():
    for item in list:
        print(item)
    input("press enter to continue")


def option2():
    # take out required attributes
    listname = list
    n = len(list)
    # Perform n-1 bubble operations on the sequence
    for i in range(n - 1, 0, -1):
        # Bubble the largest item to the end
        for j in range(i):
            if listname[j].CustomerName.lower() > listname[j + 1].CustomerName.lower():
                # Swap the j and j+1 items
                tmp = listname[j]
                listname[j] = listname[j + 1]
                listname[j + 1] = tmp
    print(listname)
    input('press anything to continue')


def option3():
    print('u are at option2')
    listpackage = list

    n = len(listpackage)
    for i in range(n - 1):
        # Assume the ith element is the smallest.
        smallNdx = i
        # Determine if any other element contains a smaller value.
        for j in range(i + 1, n):
            if listpackage[j].PackageName < listpackage[smallNdx].PackageName:
                smallNdx = j
                # Swap the ith value and smallNdx value only if the smallest
        # value is not already in its proper position.
        if smallNdx != i:
            tmp = listpackage[i]
            listpackage[i] = listpackage[smallNdx]
            listpackage[smallNdx] = tmp
    print(listpackage)
    input('press anything continue')


def option4():
    arr = list
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i].PackageCostPerPax

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j].PackageCostPerPax:
            arr[j+1].PackageCostPerPax = arr[j].PackageCostPerPax
            j -= 1
        arr[j+1].PackageCostPerPax = key
    print(arr)


def option5():
    listname = list
    n = len(listname)
    target = input('name here: ').lower()

    for i in range(n):
        # If the target is in the ith element, return True
        if listname[i].CustomerName.lower() == target:
            update(target)
    else:
        print('error cannot find')


def option6():
    # take out required attributes
    listname = list
    n = len(list)
    # Perform n-1 bubble operations on the sequence
    for i in range(n - 1, 0, -1):
        # Bubble the largest item to the end
        for j in range(i):
            if listname[j].PackageName.lower() > listname[j + 1].PackageName.lower():
                # Swap the j and j+1 items
                tmp = listname[j].PackageName.lower()
                listname[j].PackageName = listname[j + 1].PackageName.lower()
                listname[j + 1].PackageName = tmp.lower()
    # Start with the entire sequence of elements
    theValues = listname
    target = input("input package name here: ").lower()
    low = 0
    high = len(theValues) - 1
    # Repeatedly subdivide the sequence in half until the target is found
    while low <= high:
        # Find the midpoint of the sequence
        mid = (high + low) // 2

        # Does the midpoint contain the target? If yes, return midpoint (i.e. index of the list)
        if theValues[mid].PackageName.lower() == target:
            updatebinary(mid, listname)
            return 'update complete'
        # Or is the target before the midpoint?
        elif target < theValues[mid].PackageName.lower():
            high = mid - 1
        # Or is the target after the midpoint?
        else:
            low = mid + 1

    # If the sequence cannot be subdivided further, target is not in the list of values
    return print("error cannot be found")
    # update record here


def updatebinary(index, sortedlist):
    attribute = -1
    while attribute != '0':
        attribute = input(
            'insert attribute to change here press 0 to escape\nNa1.CustomerName, 2.Package name, 3.NumberOfPax, 4.PackageCostPerPax: ').lower()
        if attribute == '1':
            name = input('insert customer name here')
            sortedlist[index].CustomerName = name

        elif attribute == '2':
            packagename = input('insert package name here')
            sortedlist[index].PackageName = packagename

        elif attribute == '3':
            validation = True
            while validation:
                numberofpax = input('insert number of pax here')
                if numberofpax.isnumeric():
                    sortedlist[index].NumberOfPax = int(numberofpax)
                    sortedlist[index].totalprice = sortedlist[index].NumberOfPax * \
                        sortedlist[index].PackageCostPerPax
                    validation = False

                else:
                    print('not a number')
        elif attribute == '4':
            validation = True
            while validation:
                packagecostperpax = input('insert cost per pax')
                if packagecostperpax.isnumeric():
                    sortedlist[index].PackageCostPerPax = int(
                        packagecostperpax)
                    sortedlist[index].totalprice = sortedlist[index].PackageCostPerPax * \
                        sortedlist[index].NumberOfPax
                    validation = False

                else:
                    print('not a number')


def option7():
    numberlist = []
    validation = True
    while validation == True:
        x = input('insert smaller number: ')
        if x.isnumeric:
            x = int(x)
            y = input('insert bigger number: ')
            if y.isnumeric:
                y = int(y)
                if x > y:
                    print('small value is bigger than big value')
                else:
                    validation = False
                    for item in list:
                        if x <= item.PackageCostPerPax <= y:
                            numberlist.append(item)
                    print(numberlist)


# pancake sort

def flip(arr, i):
    # reverse arr[0...i]
    start = 0
    while start < i:
        temp = arr[start]
        arr[start] = arr[i]
        arr[i] = temp
        start += 1
        i -= 1

# work in progress pancake sort


def option8(arr):
    # the main function that complete sorting
    # start from the array and one by one reduce the current size
    output = []
    curr_size = len(arr) - 1
    # find the index of the maxmium element inside the arr[0..curr_size -1]
    while curr_size > 0:
        mi = findMaxUpTo(arr, curr_size)
        if mi != curr_size:
            flip(arr, mi)
            # once I flip it
            # now move the maximum number to the end by reversing current array
            flip(arr, curr_size)
        curr_size -= 1
    return arr


def findMaxUpTo(arr, rightBound):
    best_index = 0
    max_val = 0
    for i in range(rightBound + 1):
        if arr[i].totalprice > max_val:
            best_index = i
            max_val = arr[i].totalprice
    return best_index

    # quick sort (cant be used..)
    # array = list
    # less = []
    # pivotList = []
    # more = []
    # if len(array) <= 1:
    #     return array
    # else:
    #     pivot = array[0]
    #     for i in array:
    #         if (i.totalprice) < (pivot.totalprice):
    #             less.append(i)
    #         elif (i.totalprice) > (pivot.totalprice):
    #             more.append(i)
    #         else:
    #             pivotList.append(i)
    #     less = option8(less)
    #     more = option8(more)
    #     return less + pivotList + more


def option9():
    a = list
    n = len(a)
    while (is_sorted(a) == False):
        shuffle(a)
    print(a)
# check


def is_sorted(a):
    n = len(a)
    for i in range(0, n-1):
        if (a[i].PackageCostPerPax > a[i+1].PackageCostPerPax):
            return False
    return True
# permutation


def shuffle(a):
    n = len(a)
    for i in range(0, n):
        r = random.randint(0, n-1)
        a[i], a[r] = a[r], a[i]
    # main menu loop


def option10():
    A = list
    up = range(len(A)-1)
    while True:
        for indices in (up, reversed(up)):
            swapped = False
            for i in indices:
                if A[i].CustomerName > A[i+1].CustomerName:
                    A[i], A[i+1] = A[i + 1], A[i]
                    swapped = True
            if not swapped:
                return A


def menu():
    print("Welcome to hotel management system1.\n"
          "1. Display all records\n"
          "2. Sort record by Customer Name using Bubble sort\n"
          "3. Sort record by Package Name using Selection sort\n"
          "4. Sort record by Package Cost using Insertion sort\n"
          "5. Search record by Customer Name using Linear Search and update record\n"
          "6. Search record by Package Name using Binary Search and update record\n"
          "7. List records range from $X to $Y. e.g $100-200\n"
          "8. Use Pancake SOrt to sort total price from lowest to highest\n"
          "9. Bogo sort package cost per pax\n"
          "10.Cocktail shaker customer name\n"
          "11.Exit")
    option = input("Insert choice here:")
    return option


menuflag = True
while menuflag:
    choice = menu()
    if choice == "1":
        option1()
    elif choice == '2':
        option2()
    elif choice == "3":
        option3()
    elif choice == "4":
        option4()
    elif choice == "5":
        option5()
    elif choice == "6":
        print(option6())
    elif choice == "7":
        option7()
    elif choice == '8':
        print(option8(list))
    elif choice == "9":
        option9()
    elif choice == "10":
        print(option10())
    elif choice == "11":
        exit()
