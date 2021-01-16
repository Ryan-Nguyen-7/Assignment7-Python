#!/usr/bin/env python3

# Created by Ryan Nguyen
# Created on January 2021
# This program checks if a multi digit number is a palindrome


def Palindrome_check(char_in_list):
    # checks if given number is a palindrome

    char_in_list_bw = []  # bw = backwards
    bw_counter = len(char_in_list) - 1
    check_counter = 0
    palindrome = True

    # create reversed version of string of numbers
    while bw_counter > 0:
        char_in_list_bw.append(char_in_list[bw_counter])

        # increment counter
        bw_counter -= 1

    # compare every character in original to reversed string
    for check_counter in range(0, len(char_in_list) - 1):
        if char_in_list[check_counter] != char_in_list_bw[check_counter]:
            palindrome = False
            break

    return palindrome


def main():
    # gets input and displays final output

    char_in_list = []
    counter = 0

    print("Palindrome check\n")
    string = input("Enter multi-digit number or word(s) \
                   you would like to check: ")

    print("")

    for counter in range(0, len(string)):
        char_in_list.append(string[counter])

    # call function
    palindrome = Palindrome_check(char_in_list)

    if palindrome is True:
        print("{0} is a palindrome".format(string))
    else:
        print("{0} is not a palindrome".format(string))


if __name__ == "__main__":
    main()
