# Given a string: 'Hello World!'. Display the following:
# a. Only a character: W
# b. The string: World!
# c. Reversed String: !dlroW olleH
# d. Every third character: HlWl

character = 'Hello World!'
print(character[6])
print(character[6:12])
print(character[::-1])
print(character[::3])



# Given a list [1, 2, 3, 4, 5, 6, 7, 8, 9]. Print even alternate items in a list.
# The result should be [2, 4, 6, 8].

number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(number[1::2])


# Given a dictionary {'apples': 4, 'oranges': 10, 'mangos': 25, 'avocados':10}
# Remove the key 'oranges' from dictionary.

fruits = {'apples': 4, 'oranges': 10, 'mangos': 25, 'avocados': 10}
print(fruits)
del fruits["oranges"]
print(fruits)



# Given a nested list [1, 3, ['hello', [[2, 4, 'five', 'seven'], 2]]]
# Replace 'seven' with 7.


nested_list = [1, 3, ['hello', [[2, 4, 'five', 'seven'], 2]]]
nested_list[2][1][0][3] =7
print(nested_list)
