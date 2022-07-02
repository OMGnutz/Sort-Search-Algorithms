def number_handling(input , min , max):

    if input <= max and input >= min:
        return input

    else:
        print("Please enter a number within the given range.")
        return -1

def negative_error(input):
    if input < 0:
        return -1


def yes_no():
    while True:
        userinput = input("Do you wish to update the record? (Y/N) ")
        userinput = userinput.lower()
        if userinput != 'y' and userinput != 'n':
            continue
        else:
            break

    return userinput
