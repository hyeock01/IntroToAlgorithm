# A while loop is similar to an if statement.
# it executes some code if some condition is true.
# It will continue to execute the code for as long as the condition is true.

num = 1

while num <= 10:
    print(num)
    num += 1

# Exercise
# Print all squares from 1 to 99 (1, 4, 9, 16, ... )

i = 1
while i ** 2 < 100:
    print(i ** 2, end=" ")
    i += 1
print()


j = 0
list = [i for i in range(20)]
some = 0

while j < len(list):
    if list[j] == 13:
        j += 1
    else:
        some += list[j]
    j += 1


a = 45_86_73_45
print(a)