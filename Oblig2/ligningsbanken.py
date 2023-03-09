import random

def eq2text(L): 
    eq = f"{L[0]}x + {L[1]} = {L[2]}x + {L[3]}"
    eq = eq.replace("1x", "x")
    eq = eq.replace("+ -", "- ")
    return eq

def ok(L):
    #check if any number is zero
    for num in L:
        if num == 0:
            return False
        
    #check if 1st and 3rd elements are the same
    if L[0] == L[2]:
        return False
    
    #check if 2nd and 4th elements are the same
    if L[1] == L[3]:
        return False  

    #else return true
    return True

def make_eq():
    return [random.randint(-9, 9) for _ in range(4)]

def make_n_eqs(n):
    equations = []
    while n > 0:
        eq = make_eq()
        if ok(eq):
            equations.append(eq)
            n -= 1
    return equations

def make_test(students, n):
    return {student: make_n_eqs(n) for student in students}

def answer_questions(D):
    #get student name
    stud_name = ""
    while stud_name == "":
        name = input("Enter your name: ")
        if name in D:
            stud_name = name

    question_letter = 97 # I expect that no one is going to create a test with over 1,114,112 questions.
    for question in D[stud_name]:
        print(f"{chr(question_letter)}) {eq2text(question)}")
        answer = float(input("x = "))
        question.append(answer)
        question_letter += 1

def main():
    tests = make_test(['Ola', 'Kari', 'Fredrik'], 5)
    answer_questions(tests)
    print(tests)

main()
