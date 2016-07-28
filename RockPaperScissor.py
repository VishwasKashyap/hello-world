import random

rps = {1:'rock',2:'paper',3:'scissors'}
while True:
    print('''Enter 
             1 for rock
             2 for paper
             3 for scissor 
             Press Enter to quit''')
    user_rps = int(input())
    rand_int = random.randint(1,3)
    if user_rps == '':
        break
    if user_rps == random.randint(1,3):
        print("It's a tie ! " + rps[user_rps])
    else:
        print("Let me decide the winner later!")
     
