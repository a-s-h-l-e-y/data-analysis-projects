proto_list1 = "3,6,9,12"
proto_list2 = "A;C;M;E"
proto_list3 = "space delimited string"
proto_list4 = "Comma-spaces, might, require, typing, caution"

strings = [proto_list1, proto_list2, proto_list3, proto_list4]

# a) Use the 'in' method to check to see if the words in each string are separated by commas (,), semicolons (;) or just spaces.

list_array = proto_list1.split(",")
#for word in list_array:
#    print(word)



# b) If the string uses commas to separate the words, split it into an array, reverse the entries, and then join the array into a new comma separated string.


# using join() + reversed() + split()
# Reverse string split
final_string =  ", ".join(reversed(proto_list1.split(",")))
 
# print result
print("The string after reverse split is: " + str(final_string))


# c) If the string uses semicolons to separate the words, split it into an array, alphabetize the entries, and then join the array into a new comma separated string.

final_string2 =  "-".join(sorted(proto_list2.split(";")))

# print result
print("The string after alphabetized split is: " + str(final_string2))

# d) If the string uses spaces to separate the words, split it into an array, reverse alphabetize the entries, and then join the array into a new space separated string.

final_string3 =  " ".join(sorted(proto_list3.split(" "), reverse=True))


# print result
print("The string after reverse split is: " + str(final_string3))

# e) If the string uses ‘comma spaces’ to separate the list, modify your code to produce the same result as part “b”, making sure that the extra spaces are NOT part of the final string.

#Remove the white space from the string before you split it.

final_string4_list = proto_list4.replace(' ','').split(',')

# using join() + reversed() + split()
# Reverse string split
final_string4_list =  ",".join(reversed(proto_list4.split(",")))
 
# print result
print("The string after reverse split is: " + str(final_string4_list))