#function to code
def code(text):

    import string
    import random

    #splitting words into list from whitespaces
    split_text = text.split(" ")

    for i in range(0, len(split_text)):

        #taking 1 word on count each time
        word = split_text[i]

        if len(word) == 1:
            print(word)
        elif len(word) == 2:
            appended = word[1]+word[0]
            print(appended)
        elif len(word) > 2:
            appended = (random.choice(string.ascii_letters))+(random.choice(string.ascii_letters))+(random.choice(string.ascii_letters))+word[1:]+word[0]+(random.choice(string.ascii_letters))+(random.choice(string.ascii_letters))+(random.choice(string.ascii_letters))
            print(appended)


#function to decode
def decode(text):

    # splitting words into list from whitespaces
    split_text = text.split(" ")

    for i in range(0, len(split_text)):

        # taking 1 word on count each time
        word = split_text[i]

        if len(word) == 1:
            print(word)
        elif len(word) == 2:
            appended = word[1]+word[0]
            print(appended)
        elif len(word) > 2:
            appended = word[3: len(word)-3]
            result = appended[-1] + appended[0: len(appended)-1]
            print(result)


text = input("Enter the Texts: ")
whatToDo = int(input("Enter 0 to code   :\nEnter 1 to decode : "))

if whatToDo == 0:
    code(text)
elif whatToDo == 1:
    decode(text)
else:
    raise ValueError("Value only should be 0 or 1!!!")