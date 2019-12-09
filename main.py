#Ruben Navarro
# 12/09/2019
# main.py
# CTCI-PermutationPalindrome
# Checks if a string is a permutation of a palindrome

# Checks if string is empty
def check_if_empty(s):
    if len(s) < 1:
        return False

# Checks if length of string is > 1
def check_length(s):
    if len(s) == 1:
        return True
    else:
        return False

# Prints out error message if string is not a valid palindrome
def exit_error_message(s):
    print("{0} Not a valid Palindrome".format(s))


# Driver
str = "Taco Cat"

check_if_empty(str)
check_length(str)


counter = 0
i = 0

s = set(str.lower())
print(s)

for c in s:

# performs algorithm if charactor is not empty
    if c != ' ':
        i = str.lower().count(c)
        print(i)
        if i % 2 != 0:
            counter += 1

        if counter > 1:
            exit_error_message(str)
            exit()

        i = 0

print("{0} is a valid Permutation of a Palindrome".format(str))
exit()