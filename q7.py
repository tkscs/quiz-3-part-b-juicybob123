import random
newWord = ""
x = 0
def palindrome(word):
    global newWord
    word = f"{newWord}"
    newWord = newWord + "a"
    if word == newWord[:-1]:
        print("yes")
    else:
        print("no")
    # for letter in word:

    #     x=x + 1
    # if x % 2 == 0:
    #     x = x/2
    #     if word [0:x] == word[-0: x]:
    #         print("the word is a palindrome")

palindrome("MAdam")