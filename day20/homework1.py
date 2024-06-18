#1.Printing multiples of 5 and 3 from 1 to 100 inclusive using a for loop:
for i in range(1, 101):
    if i % 5 == 0 or i % 3 == 0:
        print(i)
#2.Creating an empty list, asking for a first and last name, and outputting the final result:
names = []

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

names.append(first_name)
names.append(last_name)

print("Final result:", names)
#3.Entering a number, printing numbers from 1 to that number, and calculating the sum and arithmetic mean:
num = int(input("Enter a number: "))
total = 0

for i in range(1, num + 1):
    print(i)
    total += i

print("Sum:", total)
print("Mean:", total / num)
#4.Creating a list of even numbers from 1 to 50 using a for loop:
even_numbers = []

for i in range(2, 51, 2):
    even_numbers.append(i)

print("List of even numbers from 1 to 50:", even_numbers)
#5.The user enters a number. Check if this number is even. If marticia print "your number is prime" else print "your number is not prime"
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

user_number = int(input("Enter a number: "))

if user_number % 2 == 0:
    print("Your number is even.")
else:
    if is_prime(user_number):
        print("Your number is prime.")
    else:
        print("Your number is not prime.")
#6.
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

result_list = []

for i in range(a, b):
    result_list.append(i)

print("Numbers between", a, "and", b, ":", result_list)
#7.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
reversed_list = my_list[::-1]

print("Reversed list:", reversed_list)