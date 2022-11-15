# !/user/bin/env.python3
# Created By: Samuel Nkongolo
# Date: Nov. 11, 2022
# This program uses a while loop to add up all the whole numbers,
# starting from 0, until that number and display the sum to the user.


def main():
    # set loop counter to know how many times to loop
    loop_counter = 0
    sum = 0

    # get user number
    user_Input = input("Enter a positive Integer: ")
    print("")
    # Tries to convert the user input to an int.
    try:
        user_number = int(user_Input)
    except Exception:
        print()
        print("This is a string. Please input a positive integer.")
        return main()
    if user_number < 0:
        print("Please input a positive integer.")
    else:
        # Tracks the amount of loops.
        while loop_counter <= user_number:
            print("")
            print("{0} times through the loop.".format(loop_counter))
            loop_counter = loop_counter + 1
        print("")
        sum = sum + loop_counter
        print("The sum is")
        print(sum)


if __name__ == "__main__":
    main()
