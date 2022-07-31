class Question:
    def __init__(self, text, choices, answer):
        self.text=text
        self.choices=choices
        self.answer=answer

    def checkAnswer(self,answer):
        return self.answer==answer

class Quiz:
    def __init__(self, questions):
        self.questions=questions
        self.score=0
        self.questionIndex= 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question=self.getQuestion()
        print(f'soru {self.questionIndex+1}: {question.text}')
        for q in question.choices:
            print('-'+ q)
        answer = input('cevap: ')
        self.guess(answer)
        self.loadQuestion()

    def guess(self, answer):

        question = self.getQuestion()
        if question.checkAnswer(answer):
            self.score+=1
        self.questionIndex+=1


    def loadQuestion(self):
        if len(self.questions)==self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()
    def showScore(self):
        print("score:", self.score)

    def displayProgress(self):
        totalQuestion=len(self.questions)
        questionNumber=self.questionIndex
        if questionNumber>=totalQuestion:

            print("Quiz bitti")
        print(f'{totalQuestion} sorudan {totalQuestion - questionNumber} soru kaldı')
q1=Question("En iyi programlama dili nedir?", ['java', 'python', 'javascript','c#'], 'ptyhon')
q2=Question("En popüler programlama dili nedir?", ['java', 'python', 'javascript','c#'], 'ptyhon')
q3=Question("En kazançlı programlama dili nedir?", ['java', 'python', 'javascript','c#'], 'ptyhon')
q4=Question("En eski programlama dili nedir?", ['java', 'python', 'javascript','c#'], 'ptyhon')
questions=[q1,q2,q3,q4]

quiz=Quiz(questions)
question=quiz.getQuestion()
quiz.displayQuestion()