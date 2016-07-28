spam = ['apples','bananas','tofu','cats']
def comma(spamref):
    spamref.insert(len(spamref)-1,'and')
    for i in range(len(spamref)):
        print(spamref[i])
        spamref.insert(i,',')
comma(spam)
