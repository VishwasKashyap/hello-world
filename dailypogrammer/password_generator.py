import random
import string
def password(type_number):
    list_of_passwords = ['anamika123', 'Inspire123','abc123']
    if type_number == 1:
        print("You have requested for a weak random password")
        generated_password = list_of_passwords[random.randint(0,len(list_of_passwords)-1)]
        print(generated_password)
    elif type_number == 2:
        print("You have requested for a medium strong password!")
        generated_password = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))
        print(generated_password)
    elif type_number == 3:
        print("You have requested for a very strong password!")
        generated_password =  ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
        print(generated_password)

print("""  1 to generate a weak password
               2 to generate a medium strong password
               3 to generate a very strong password """)
type_number = int(input("Enter your choice!"))
password(type_number)
