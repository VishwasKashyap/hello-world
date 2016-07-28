import re

result = re.search("yo", "How are you?")
if result:
    print("Your string is somewhere in that statement!")
    print("Let's decipher out where exactly it is!")
    print(
else:
    print("I am sorry! It's nowhere to be seen!")

