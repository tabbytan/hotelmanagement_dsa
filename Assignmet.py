from re import L
from struct import pack
from tkinter import Pack


def menu():
    print("Welcome to hotel management system1.\n "
          "1. Display all records\n"
          "2. Sort record by Customer Name using Bubble sort\n"
          "3. Sort record by Package Name using Selection sort\n"
          "4. Sort record by Package Cost using Insertion sort\n"
          "5. Search record by Customer Name using Linear Search and update record\n"
          "6. Search record by Package Name using Binary Search and update record\n"
          "7. List records range from $X to $Y. e.g $100-200\n"
          "8. Use Quick Sort to sort total price from lowest to highest\n"
          "9. Exit Application")
    option = input("Insert choice here:")
    return option


def update(name):
    attribute = input("change which attribute?").lower()
    name = name.lower()
    if attribute == 'packagename':
        for item in list:
            if name == item.CustomerName:
                item.PackageName = input("Change package name here: ")
    elif attribute == 'customername':
        for item in list:
            if name == item.CustomerName:
                item.CustomerName = input("change customer name here: ")
    elif attribute == 'numberofpax':
        for item in list:
            if name == item.CustomerName:
                validation = True
                while validation:
                    value = input('insert no of pax here')
                    if value.isnumeric():
                        item.NumberOfPax = value
                    else:
                        print('error not a number')
    elif attribute == 'packagecostperpax':
        for item in list:
            if name == item.CustomerName:
                validation = True
                while validation:
                    value = input('insert no of pax here')
                    if value.isnumeric():
                        item.PackageCostPerPax = value
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
        return f'{self.PackageName},{self.CustomerName},{self.NumberOfPax},{self.PackageCostPerPax}'

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
                tmp = listname[j].CustomerName.lower()
                listname[j].CustomerName = listname[j + 1].CustomerName.lower()
                listname[j + 1].CustomerName = tmp.lower()
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
            tmp = listpackage[i].PackageName
            listpackage[i].PackageName = listpackage[smallNdx].PackageName
            listpackage[smallNdx].PackageName = tmp
    print(listpackage)
    input('press anything continue')


def option4():
    listpackagecost = list
    n = len(listpackagecost)
    # Starts with the first item as the only sorted entry.
    for i in range(1, n):
        # Save the value to be positioned
        value = listpackagecost[i].PackageCostPerPax
        # Find the position where value fits in the
        # ordered part of the list.
        pos = i
        while pos > 0 and value < listpackagecost[pos - 1].PackageCostPerPax:
            # Shift the items to the right during the search
            listpackagecost[pos].PackageCostPerPax = listpackagecost[pos -
                                                                     1].PackageCostPerPax
            pos -= 1
            # Put the saved value into the open slot.
            listpackagecost[pos].PackageCostPerPax = value
    print(listpackagecost)
    input('press anything to continue')


def option5():
    listname = list
    n = len(listname)
    target = input('name here').lower()

    for i in range(n):
        # If the target is in the ith element, return True
        if listname[i].CustomerName.lower() == target:
            update(target)
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
            'insert attribute to change here press 0 to escape\nPackageName, CustomerName, NumberOfPax, PackageCostPerPax: ').lower()
        if attribute == 'customername':
            name = input('insert customer name here')
            sortedlist[index].CustomerName = name
        elif attribute == 'packagename':
            packagename = input('insert package name here')
            sortedlist[index].PackageName = packagename
        elif attribute == 'numberofpax':
            validation = True
            while validation:
                numberofpax = input('insert number of pax here')
                if numberofpax.isnumeric():
                    sortedlist[index].NumberOfPax = numberofpax
                    validation = False
                else:
                    print('not a number')
        elif attribute == 'packagecostperpax':
            validation = True
            while validation:
                packagecostperpax = input('insert cost per pax')
                if packagecostperpax.isnumeric():
                    sortedlist[index].PackageCostPerPax = packagecostperpax
                    validation = False
                    list.clear()
                    list.append(list)
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
                        if x < item.PackageCostPerPax < y:
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

 # main menu loop
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
        exit()
