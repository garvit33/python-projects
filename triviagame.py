import random

questions = {
    "What does CPU stand for?":"central processing unit",
    "Which device is known as the “brain of the computer”?":"cpu",
    "What does RAM stand for?":"random access memory",
    "What is the full form of IP in computer networking?": "Internet Protocol",
    "Which type of software controls computer hardware?": "Operating System",
    "What is the smallest unit of data in a computer?": "Bit",
    "Which key is used to refresh a webpage?": "F5",
    "Name two output devices.": "Monitor and Printer",
    "What does URL stand for?": "Uniform Resource Locator",
    "What is the shortcut key for copy in Windows?": "Ctrl + C"
}

def python_trivia_game():
    questionslist = list(questions.keys())
    totalquestion = 5 
    score = 0
    selected_questions= random.sample(questionslist,totalquestion)

    for index,question in enumerate(selected_questions):
        print(f"{index+1}. {question}")
        useranswer = input("your answer: ").lower().strip()
        correctanswer = questions[question]

        if useranswer == correctanswer.lower().strip():
            print("your answer is correct\n")
            score += 1
        else:
            print(f"sorry wrong answwer the correct answer is {correctanswer}. \n")
             
    print(f"game over your total score is {score}/{totalquestion}")  
    

python_trivia_game()


