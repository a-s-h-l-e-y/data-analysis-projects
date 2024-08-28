my_string = "LaunchCode"


# a) Use string methods to remove the first three characters from the string and add them to the end.
my_string_slice = my_string[:3]

print(my_string_slice)

my_string_slice_NEW = my_string[3:10] + my_string_slice

# Use a template literal to print the original and modified string in a descriptive phrase.

print(f"The word {my_string} in pig latin is {my_string_slice_NEW}")



# b) Modify your code to accept user input. Query the user to enter the number of letters that will be relocated.

number_of_letters = int(input("Enter the number of letters: "))

#print(number_of_letters)

# c) Add validation to your code to deal with user inputs that are longer than the word. In such cases, default to moving 3 characters. Also, the template literal should note the error.

while number_of_letters > len(my_string):
    print("Number Longer Than Word")
    number_of_letters = 3

# print(number_of_letters)

