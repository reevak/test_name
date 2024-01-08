from Student import Chef,SuperChef

myChef = Chef()
supChef = SuperChef()

myChef.make_special()
supChef.make_special()



from Student import Student

Student1 = Student("John","Business",gpa=3.1,is_on_probation=True)
Student2 = Student("Pam","Law",gpa=2,is_on_probation=False)

print(Student1.gpa)
print(Student2.on_honor_roll())

from Student import Question

questions_prompts = [
    "What color are apples?\na) Green\nb) Magenta\nc) Yellow",
    "What color are sharks?\na) White\nb) Pink\nc) Blue",
    "What color are strawberries?\na) Teal\nb) Red\nc) Brown",
]

questions = [
    Question(questions_prompts[0],"a"),
    Question(questions_prompts[1],"c"),
    Question(questions_prompts[2],"b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt + "\n")
        if answer == question.answer:
            score += 1
            if score == len(questions):
                print("You win!")
        else:
            print("Wrong answer, try again!")
            return False

run_test(questions)