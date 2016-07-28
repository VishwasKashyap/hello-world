import random
def cb(number):
    random_number = random.randrange(1000,2000,4)
    rmlist =  [int(x) for x in str(random_number)]
    print(rmlist)
    numlist = [int(i) for i in str(number)]
    print(numlist)
    cows = 0
    bulls = 0
    for i in range(len(rmlist)):
        if rmlist[i]==numlist[i]:
            cows+=1
        elif rmlist[i] in numlist:
            bulls+=1
    result = [cows,bulls]
    return(result)

number = int(input("Enter the number"))
cows_bulls = cb(number)
print("The number of cows = "+str(cows_bulls[0])+" bulls = "+str(cows_bulls[1])) 
