from Questions import Question

question_prompts = [

    "What day is it?\n(a) Thursday\n(b) Friday\n(c) Saturday\n\n",
    "What month is it?\n(a) June\n(b) September\n(c) November\n\n",
    "What year is it?\n(a) 2020\n(b) 2022\n(c) 2023\n\n"

]

Questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "b"),
]

def run_test(Questions):
    Score = 0
    for Question in Questions:
        answer = input(Question.prompt)
        if answer == Question.answer:
            Score += 1
    print("Thanks for completing the test, you got " + str(Score) + "/" + str(len(Questions)) + " questions correctly.")

run_test(Questions)