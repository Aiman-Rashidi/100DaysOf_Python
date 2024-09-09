qno = [["1)question1\n", "option1.1", "option1.2", "option1.3", "option1.4"],
       ["2)question2\n", "option2.1", "option2.2", "option2.3", "option2.4"],
       ["3)question3\n", "option3.1", "option3.2", "option3.3", "option3.4"],
       ["4)question4\n", "option4.1", "option4.2", "option4.3", "option4.4"],
       ["5)question5\n", "option5.1", "option5.2", "option5.3", "option5.4"],
       ["6)question6\n", "option6.1", "option6.2", "option6.3", "option6.4"],
       ["7)question7\n", "option7.1", "option7.2", "option7.3", "option7.4"],
       ["8)question8\n", "option8.1", "option8.2", "option8.3", "option8.4"],
       ["9)question9\n", "option9.1", "option9.2", "option9.3", "option9.4"],
       ["10)question10\n", "option10.1", "option10.2", "option10.3", "option10.4"]]

answer = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2]
levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0

for i in range(0, len(qno)):

    #setting question and question price to show
    question = qno[i]
    print(f"\nQuestion for Rs.{levels[i]}\n")

    #print question
    print(question[0])

    #print options
    print(f"1) {question[1]}     2) {question[2]}\n3) {question[3]}     4) {question[4]}\n")

    #getting player's reply
    reply = int(input("Enter your Answer (1-4) or (0) to quit: "))

    #checking input Answer
    if reply == 0:
        print("Quiting the game...")
        break
    if answer[i] == reply:
        print(f"Correct Answer!\nBalance={levels[i]}")
        print("\n\n\n")
    else:
        print("Wrong Answer!")
        break

    #levels where money freezes.
    if i == 4:
        money = levels[i]
    elif i == 7:
        money = levels[i]
    elif i == 9:
        money = levels[i]

#printing final money won!
print(f"YOUR TAKE HOME MONEY IS Rs.{money}")