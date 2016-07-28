def collatz(number):
    if(number%2 == 0):
        result = number//2
        print(result)
        if(result!=1):
            collatz(result)
    else:
        result = 3*number+1
        print(result)
        if(result!=1):
            collatz(result)

print("Let's show some magic!!")
print("Enter a number")
num = int(input())
collatz(num)
