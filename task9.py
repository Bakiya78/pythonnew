Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
if input is 4 then it should print. Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)

solution:
def print_pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end='')
        print()
print_pattern(3)
print_pattern(4)
