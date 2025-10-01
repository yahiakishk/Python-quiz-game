questions = ('What is my name? ',
             'How old am I? ',
             'What is my favorite colour? ',
             'How many cats do I have? ',
             'What grade am I in? ')

options = (('A. Yahia', 'B. Yahio', 'C. Yohia', 'D. Yahiah'),
           ('A. 16', 'B. 17', 'C. 18', 'D. 19'),
           ('A. Cyan', 'B. Yellow', 'C. Red', 'D. Blue'),
           ('A. 4', 'B. 3', 'C. 2', 'D. 1'),
           ('A. 10', 'B. 12', 'C. 9 ', 'D. 11'))

answers = ('A', 'B', 'D', 'C', 'D')
guesses = []
score = 0
question_number = 0

for question in questions:
    print("===========================")
    print(question)
    for option in options[question_number]:
        print(option)
    while True:
        guess = input("Enter your answer (A, B, C, D) (q to quit): ").upper()
        if guess == "Q":
            break
        elif guess not in ("A", "B", "C", "D"):
            print("Input invalid please only enter these: A, B, C, D")
        else:
            break
    guesses.append(guess)
    if guess == answers[question_number]:
        score += 1
        print("*******************Correct!*******************")
    else:
        print("*******************Incorrect!*******************")

    question_number += 1
print(f'You got {score} question right out of 5 questions')
