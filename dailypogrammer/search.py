def search(number,numbers):
    if number in numbers:
        print("Number found at position "+numbers.index[number] )
    else:
        print("Not found")

number = 5
numbers = [1,2,3,4,5]
search(number,numbers)
