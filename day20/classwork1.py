my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print("Even numbers:")
print([num for num in my_list if num % 2 == 0])

print("\nMultiples of 5:")
print([num for num in my_list if num % 5 == 0])

print("\nSum of the numbers:", sum(my_list))

print("\nSum of the even numbers:", sum(num for num in my_list if num % 2 == 0))

print("\nList of odd numbers:", [num for num in my_list if num % 2 != 0])

print("\nMultiples of 3 and 5:", [num for num in my_list if num % 3 == 0 and num % 5 == 0])
