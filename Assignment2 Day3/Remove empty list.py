# Python program to remove empty List from List

# Initializing list
test_list = ["", "LetsUpgrad", "", "is", "a", "", "community", "Oriented", "Educational", "Platfrom"]

# printing original list
print("The original list is: " + str(test_list))

# Remove empty List from List using list comprehension
test_list = [i for i in test_list if i]

# printing result
print("Modified list is: "+str(test_list))
