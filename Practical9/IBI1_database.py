class IBIstudent:
#create a class for IBIstudent
    def __init__(self,name,major,portfolio_score,group_project_score,exam_score):
        #definite a function for the information
        #portfolio_score, group_project_score and exam_score should be our of 100
        self.name=name
        self.major=major
        self.portfolio_score=portfolio_score
        self.group_project_score=group_project_score
        self.exam_score=exam_score
    def details(self):
        #print them in one line
        print(f"Name: {self.name}, Major: {self.major}, Score of code portfolio: {self.portfolio_score}, Score of group project: {self.group_project_score}, Exam Score: {self.exam_score}")
#Example: You can create a new Student instance
student1=IBIstudent("Merry","BMI",100,100,100)
#Then you can see the details of this student
student1.details()