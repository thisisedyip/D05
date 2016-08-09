#!/usr/bin/env python3
# HW05_ex00_logics.py


##############################################################################
def even_odd():
    """ Print even or odd:
        Takes one integer from user
            accepts only non-word numerals
            must validate
        Determines if even or odd
        Prints determination
        returns None
    """
    user_input = ''
    while True:
        try:
            user_input = int(input("Please provide an integer: "))
            if user_input % 2 == 0:
                print("You've provided an even integer.")
                return None
                break
            else:
                print("You've provided an odd integer.")
                return None
                break
        except:
            print("Please provide a non-word integer.  Please try again.")

    pass


def ten_by_ten():
    raw_list = range(1,101)
    count = 0

    for numbers in raw_list:
        print("{:<4} ".format(numbers), end = " ")
        count += 1
        if count % 10 == 0:
            print()
            count = 0
    pass


def find_average():
    """ Takes numeric input (non-word numerals) from the user, one number
    at a time. Once the user types 'done', returns the average.
    """
    number_list = []
    count = 0

    while True:
        try:
            user_input = int(input("Please provide some integers"
            "(Type 'done' when you are done): "))
            number_list.append(user_input)
            count += 1    
            #if str(user_input) != 'done':
            #    print("Please try again.")
            #    continue
            #if user_input == 'done':
        except:
            break

    if count == 0:
        print("You haven't entered any numbers.  Good bye.")
    else:
        average = sum(number_list)/len(number_list)
        print("You've entered ", count, " numbers.  The average of your inputs is: ", str(average))
    pass


##############################################################################
def main():
    """ Calls the following functions:
        - even_odd()
        - ten_by_ten()
    Prints the following function:
        - find_average()
    """
    even_odd()
    ten_by_ten()
    print(find_average())
    pass

if __name__ == '__main__':
    main()
