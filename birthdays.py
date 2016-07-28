birthdays = {'yogesh':'Apr 1', 'Sumesh':'May1','Nikhil':'June1'}
while True:
    print("Enter a name:(Blank to quit)")
    name = input()
    if(name == ''):
        break
    if name in birthdays:
        print(birthdays[name] + ' is the day ' + name +' was born')
    else:
        print("I do not have info about " + name)
        print ("Please enter the birthday!")
        bday = input()
        birthdays[name] = bday
        print("Birthday database updated")

