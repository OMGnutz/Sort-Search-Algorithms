import menu as m
import random

records = [ ['Z' , 'roy' , 10 , 300] , ['C' , 'tom' , 2 , 500] , ['S', 'peter' , 4 , 100] , ['r' , 'angus' , 30 , 40] , ['D' , 'mary' , 1 , 90] , ['a' , 'may' , 7 , 50] , ['x' , 'nick' , 6 , 68] , ['Q' , 'noah' , 6 , 85] , ['P' , 'nicholas' , 8 , 150] , ['m' , 'brian' , 4 , 125]]
#Loop through records and make all the string lowercase

for x in records:
        for i in range (0 , len(x) , 1 ):
            check_string = isinstance(x[i] , str)
            if check_string:
                 x[i] = x[i].lower()
def get_nested_records(number):

    #Loop through the list and get the items that you want, appending it to a new list
    needed_list = []
    for x in records:
        needed_list.append(x[number])

    return needed_list


def sort_mainlist(listx , number):
    #Get the sorted records and match it with the main records to sort it
    sortedrecords = []
    index_list = []
    for y in records:
        if y[number] in listx:
            posy = listx.index(y[number])
            index_list.append(posy)


    zippedsortedrecords = [z for z in sorted(zip(index_list , records))]

    #Zipped list returns tuples so we need to retrieve only the data we want which is list

    for x in zippedsortedrecords:
        for y in x:
            if isinstance(y , list):
                sortedrecords.append(y)

    return sortedrecords


def bubble_sort(list):
    #Check the from left to right to see if the previous value is higher
    #If previous value is higher swap the places of the list items
    passes = 0
    for j in range(0, len(list) - 1, 1):
        if list[j] > list[j + 1]:
            tmp = list[j]
            list[j] = list[j + 1]
            list[j + 1] = tmp
            passes += 1

    if passes == 0:
        return list

    #Recursive function to call itself until list is fully sorted
    if passes != 0:
        return bubble_sort(list)



def selection_sort(list):
    passes = 0
    #Assume the first item is the smallest
    for i in range(len(list)):
        small = i
        #Loop through the list after the first item to see if there are any items that are smaller
        for j in range(i + 1 , len(list) , 1):
            if list[j] < list[small]:
                small = j
        #Swap item places if smaller item is found
        if list[small] != list[i]:
            temp = list[i]
            list[i] = list[small]
            list[small] = temp
            passes += 1

    #Recursive function to call itself until list is fully sorted
    if passes == 0:
        return list

    else:
        return selection_sort(list)


def insertion_sort(list):
    #Segregate the list into two, your hand and the unsorted part of the list
    for i in range(1 , len(list) , 1):
        selected = list[i]
        previous = i - 1

    #Continu shifting the items until your hand is sorted
        while previous >= 0 and selected < list[previous]:
            list[previous + 1] = list[previous]
            previous -= 1
        list[previous + 1] = selected

    return list


def linear_search(name , list):
    #Compare your input with the database one by one
    for i in list:
        if name.lower() == i:
            return 1

    #If its not found in the list return not found
    return -1




def binary_search( theValues, target ):
    #Only works in sorted list
    low = 0
    high = len(theValues) - 1

    while low <= high:
        #Return the item if the item is found in the middle
        mid = (high + low) // 2
        if target == theValues[mid]:
            return target
        #Else if the item value is lower then the mid value change the high value to be lower than the mid value and get a new mid value
        elif target < theValues[mid]:
            high = mid - 1

        #Else if the item value is higher then the mid value change the low value to be higher than the mid value and get a new mid value
        elif target > theValues[mid]:
            low = mid + 1



    return -1


def update_records(name , number):
    #Get the record that you want to update
    position = get_nested_records(number).index(name)
    record = records[position]
    m.update_menu()
    while True:
        try:
            userinput = int(input("Select an option: "))
            assert userinput >=0 and userinput <=4
        except ValueError:
            print("Please enter a number")

        except AssertionError:
            print("Please enter a number within the range")

        else:
        #Update the list based on userinput
            if userinput == 1:
                while True:
                    newinput = input("Please enter the customer's new name: ")
                    if newinput == "":
                        print("Please enter something")

                    else:
                        for x in records:
                            if newinput == x[1]:
                                print("Name is already existing. Please choose a new name")
                                break

                        else:
                            record[1] = newinput
                            records[position] = record
                            break


            elif userinput == 2:
                while True:
                    newinput = input("Please enter the package's new name: ")
                    if newinput == "":
                        print("Please enter something")

                    else:
                        for x in records:
                            if newinput == x[0]:
                                print("Package is already existing. Please choose a new name")
                                break

                        else:
                            record[0] = newinput
                            records[position] = record
                            break

            elif userinput == 3:
                while True:
                    try:
                        newinput = int(input("Please enter the new number of pax: "))
                        record[2] =  newinput
                        records[position] = record
                        assert newinput > 0
                        break
                    except ValueError:
                        print("Please enter a number")

                    except AssertionError:
                        print("Please enter a valid number")

            elif userinput == 4:
                while True:
                    try:
                        newinput = int(input("Please enter the new Package cost per pax: "))
                        record[3] =  newinput
                        records[position] = record
                        assert newinput > 0
                        break
                    except ValueError:
                        print("Please enter a number")

                    except AssertionError:
                        print("Please enter a valid number")

            else:
                print("\n")
                break


def list_range():
    #Get the range to be sorted based on user input
    while True:
        try:
            min = int(input("Enter min no."))
            assert min >= 0
            break
        except ValueError:
            print("Please enter a number")

        except AssertionError:
            print("Please enter a number equal or more than 0")

    while True:
        try:
            max = int(input("Enter max no."))
            assert max >= 0 and max >= min
            break
        except ValueError:
            print("Please enter a number")

        except AssertionError:
            print("Please enter a number equal or more than minimum ")

    range_list = []
    for i in records:
        if i[3] >= min and i[3] <= max:
            range_list.append(i)

    range_list = sorted(range_list , key=lambda x: x[3])

    return range_list

def print_list(listx):
    #Print the list if existing
    listx = list(listx)
    if listx != []:
        print("Records are below! ↓")
        print()
        print(f"{'Package Name' : <20}{'Customer Name' : <20}{'Number Of Pax' : <20}{'Package Cost' : <20}")
        for x in listx:
            print(f"{x[0] : <20}{x[1] : <20}{x[2] : <20}{x[3] : <20}")
        print()

    else:
        print()
        print("There are no records")
        print()
    return


def radix_sort(list):
    #Uses counting sort but upgrade it to sort any number with multiple indexes at a faster speed


    #Reject the list that is string to prevent error
    for x in list:
        if isinstance(x , str):
            print("List contains strings which cannot be sorted using this method")
            return

    else:
        #Get the highest number to see how many indexes the function need to loop
        place = 1
        maxi = max(list)
        while maxi // place > 0:
            counting_sort(list , place)
            place *= 10
        return list


def counting_sort(list, place):
    listlength = len(list)
    output = [0] * listlength
    count = [0] * 10

    #Count the number of times the number appear
    for i in range(0 , listlength):
        index = list[i] // place
        count[index % 10] +=1


    #Add up the numbers for each occurence of the number that appear
    for i in range(1 , 10):
        count[i] += count[i - 1]


    #The added occurence of the number is the position of the list item
    #Match the occurence of the number to the list item itself
    y = listlength - 1
    while y >= 0:
        index = list[y] // place
        output[count[index % 10] - 1] = list[y]
        count[index % 10] -= 1
        y -= 1

    for x in range(0 , listlength):
        list[x] = output[x]




def bogo_sort(list):
    #Is a stupid sort and the time complexity is O(∞) for the worst case

    #Keep randomly shuffling the list until it is sorted
    while bogo_sort_issorted(list) == -1:
        bogo_sort_shuffle(list)

    return list

def bogo_sort_issorted(list):
    #Check if the list is sorted
    listlength = len(list)
    for i in range (0 , listlength -1):
        if list[i] > list[i + 1]:
            return -1

    return 1


def bogo_sort_shuffle(list):
    #Shuffle the list
    listlength = len(list)
    for i in range(0 , listlength):
        rand = random.randint(0 , listlength -1)
        temp = list[i]
        list[i] = list[rand]
        list[rand] = temp


