'''
    Ask the user for 4 words and print them out in alphabetical order.
'''

# Input the words
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
word3 = input("Enter the third word: ")
word4 = input("Enter the fourth word: ")

# Compare and output the result
print("Words in alphabetical order:")
# 1. when word1 is place in the first order, follow the pattern to compare the others words
if word1 <= word2 and word1 <= word3 and word1 <= word4:
    if word2 <= word3 and word2 <= word4:
        if word3 <= word4:
            print(word1, word2, word3, word4)
        else:
            print(word1, word2, word4, word3)
    elif word3 <= word2 and word3 <= word4:
        if word2 <= word4:
            print(word1, word3, word2, word4)
        else:
            print(word1, word3, word4, word2)
    elif word4 <= word2 and word4 <= word3:
        if word2 <= word3:
            print(word1, word4, word2, word3)
        else:
            print(word1, word4, word3, word2)

# 2. when word2 is place in the first order, follow the pattern to compare the others words
elif word2 <= word1 and word2 <= word3 and word2 <= word4:
    if word1 <= word3 and word1 <= word4:
        if word3 <= word4:
            print(word2, word1, word3, word4)
        else:
            print(word2, word1, word4, word3)
    elif word3 <= word1 and word3 <= word4:
        if word1 <= word4:
            print(word2, word3, word1, word4)
        else:
            print(word2, word3, word4, word1)
    elif word4 <= word1 and word4 <= word3:
        if word1 <= word3:
            print(word2, word4, word1, word3)
        else:
            print(word2, word4, word3, word1)

# 3. when word3 is place in the first order, follow the pattern to compare the others words
elif word3 <= word1 and word3 <= word2 and word3 <= word4:
    if word1 <= word4 and word1 <= word4:
        if word2 <= word4:
            print(word3, word1, word2, word4)
        else:
            print(word3, word1, word4, word2)
    elif word2 <= word1 and word2 <= word4:
        if word1 <= word4:
            print(word3, word2, word1, word4)
        else:
            print(word3, word2, word4, word1)
    elif word4 <= word1 and word4 <= word2:
        if word2 <= word1:
            print(word3, word4, word2, word1)
        else:
            print(word3, word4, word1, word2)

# 4. when word4 is place in the first order, follow the pattern to compare the others words
elif word4 <= word1 and word4 <= word2 and word4 <= word3:
    if word1 <= word3 and word1 <= word2:
        if word2 <= word3:
            print(word4, word1, word2, word3)
        else:
            print(word4, word1, word3, word2)
    elif word2 <= word1 and word2 <= word3:
        if word1 <= word3:
            print(word4, word2, word1, word3)
        else:
            print(word4, word2, word3, word1)
    elif word3 <= word1 and word3 <= word2:
        if word1 <= word2:
            print(word4, word3, word1, word2)
        else:
            print(word4, word3, word2, word1)
