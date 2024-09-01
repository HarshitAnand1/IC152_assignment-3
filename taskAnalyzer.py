# Part a
def pallindrome_checker():
    str_1 = input("Enter the string: ")
    str_1_low = str_1.lower()
    str_2 = str_1_low [ : : -1]

    if str_2 == str_1_low:
        print("Given string is a palindrome")
    else:
        print("Given string is not a palindrome")

# Part b
def odd_even_checker():
    N = input("Enter a positive integer: ")
    if N.isnumeric() == False:
        print("Please enter a positive integer! \nStrings, negative integers and floating point numbers are not accepted")
        odd_even_checker()
    elif int(N)&1 == 1:
        print("The given number is odd") 
    elif int(N)&1 ==0:
        print("The given number is even")


# Part c
def chr_checker():
    text = input("Enter a single word: ")
    if text.isalpha() == True:
        print("Alphabet only")
    else:
        print("Contains non-alphabetic characters")


# Part d
def long_word():
    sent = input("Please enter a sentence: ")
    words = sent.split()
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    print(longest_word)
    


# Part e
def word_num():
    phrase = input("Please enter a phrase: ")
    phrase_new = phrase.strip()
    n = phrase_new.count(" ")
    print(f"The total number of words in the given phrase is {n+1}")


pallindrome_checker()
odd_even_checker()
chr_checker()
long_word()
word_num()