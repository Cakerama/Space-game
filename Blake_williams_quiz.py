#things I need to acomplish:
#display a question
#True? increase score
#False? do do anything
#proceed to the next question
#repeat
question_num = 1
score = 0
print("welcome to Blake's Trivia!")
for i in range(3):
    if question_num == 1:
        question = input("What is the largest big cat?")
        answer = "tiger"

    if question_num == 2:
        question = input("What land animal can open its mouth the widest?")
        answer = "hippo"

    if question_num == 3:
        question = input("What is the only flying mammal?")
        answer = "bat"

    question_num += 1

    if question.lower()== answer:
        score += 1
        print(score)
        print("Good Job")
        
    else:
        print("Wrong!")


print("your score is")
print(score)
print("you've completed Blake's Trivia")


