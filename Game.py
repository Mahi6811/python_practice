import random
word=["apple","tree","door","last"]
out_word=random.choice(word)
print(out_word)

display_word=[]

guessed_letter=input("Enter a letter :")

if guessed_letter in out_word:
    print(guessed_letter+" is matched")
else:
    print("Not matched")