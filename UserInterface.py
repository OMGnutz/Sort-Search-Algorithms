from menu import menu
import ErrorHandling as er
import Algorithm as al


menu()


while True:
    try:
        userinput = int(input("Enter choice: "))

    except ValueError:
        print("Please enter a number between 0 to 7")

    else:

        if er.number_handling(userinput , 0 , 9) == -1:
            continue

        if userinput == 1:
            al.print_list(al.records)


        elif userinput == 2:
            sorted = al.bubble_sort(al.get_nested_records(1))
            new = al.sort_mainlist(sorted , 1)
            al.print_list(new)


        elif userinput == 3:
            sorted = al.selection_sort(al.get_nested_records(0))
            new = al.sort_mainlist(sorted , 0)
            al.print_list(new)

        elif userinput == 4:
            sorted = al.insertion_sort(al.get_nested_records(3))
            new = al.sort_mainlist(sorted , 3)
            al.print_list(new)

        elif userinput == 5:
            while True:
                cust = input("Enter the customer you are looking for (ENTER to exit): ")
                processor = al.linear_search(cust , al.get_nested_records(1))

                if cust == "":
                    break
                if processor == -1:
                    print("Customer %s not found" %cust)

                else:
                    print("Record found! ")
                    if er.yes_no() == 'y':
                        al.update_records(cust , 1)
                        break



        elif userinput == 6:
           while True:
               pack = input("Enter the package you are looking for (ENTER to exit): ")
               list = al.get_nested_records(0)
               list.sort()
               processor = al.binary_search(list , pack)
               if processor == -1:
                   if pack =="":
                       break
                   print("Package %s not found" %pack)

               else:
                   print("Record found! ")
                   if er.yes_no() == 'y':
                       al.update_records(pack , 0)
                       break

        elif userinput == 7:
            sorted = al.list_range()
            al.print_list(sorted)

        elif userinput == 8:
            sorted = al.radix_sort(al.get_nested_records(3))
            new = al.sort_mainlist(sorted , 3)
            al.print_list(new)

        elif userinput == 9:
            sorted = al.bogo_sort(al.get_nested_records(2))
            new = al.sort_mainlist(sorted , 2)
            al.print_list(new)

        else:
            break
