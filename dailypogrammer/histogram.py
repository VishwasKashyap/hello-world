#Define a procedure histogram() that takes a list of integers and prints a histogram to the screen.

#input: histogram([4,5,7])
#output: ****
        #*****
        #*******

def histogram(a):
    for i in range(len(a)):
        print('*'*a[i])
    
alist = [4,9,7]
histogram(alist)
