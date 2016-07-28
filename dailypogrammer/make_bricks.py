def makebricks(small,big,goal):
    small_size = 1
    big_size = 5
    if goal == small*small_size + big*big_size: #goal = small + big
        print("True!, You can add up the bricks to match your goal!")
    elif goal < small*small_size + big*big_size:
        if goal <= small*small_size:
            print("True!, you can add up the bricks to match your goal!")
        elif goal > small*small_size and goal < small*small_size+big*big_size:
            if goal % 5 <= small*small_size:
                print("True!, you can add up the bricks to match your goal!")
            else:
                print("Sorry, your goal can't be reached!")
            
    else:
        print("Sorry, your goal can't be reached!")

makebricks(1,1,7)  
