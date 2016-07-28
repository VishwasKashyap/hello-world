#Write a version of a palindrome recognizer that also accepts phrase palindromes such as "Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori", "Rise to vote sir", or the exclamation "Dammit, I'm mad!". Note that punctuation, capitalization, and spacing are usually ignored.
import re
def palindrome(sentence):
    if re.findall('[\W]',sentence):
        punctuations = re.findall('[\W]',sentence) #check for any special characters in the sentence
        print("there are some special charaters in the sentence which needs to be removed! "+ str(re.findall('[\W]',sentence)))
        modified_sentence = re.sub('[!,@\'\s]','',sentence, flags = re.IGNORECASE) #replace the special characters with a null value
        #modified_sentence = re.sub(punctuations,'',sentence, flags = re.IGNORECASE)
        modified_sentence = modified_sentence.upper() #convert the entire sentence to upper case for comparison
        print(modified_sentence)
    if modified_sentence == modified_sentence[::-1]: #check for palindrome by actually reversing the string
        print("Volia! You could recognize a palindrome!")
    else:
        print("You don't know what a palindrome is??")

random_sentence = "Dammit, I'm mad!" #input sentence
palindrome(random_sentence)
