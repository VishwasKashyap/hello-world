def lexicon(english):
    lexicon = {"merry":"god", "christmas":"jul","and":"och","happy":"gott","new":"nytt","year":"ar"}
    for word in english:
       # print(lexicon[word])
        print(lexicon.get(word,"word specified not in lexicon"))
    
english = ['merry','christmas','and','happy','new','year','hello']
lexicon(english)
