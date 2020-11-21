class Student:
    nqtScore = 100
    interviewScore = 100

    @property
    def totalScore(self):
        return self.nqtScore + self.interviewScore

    @totalScore.setter
    def totalScore(self,val):
        self.nqtScore = val -  self.nqtScore
        
s = Student()
s.totalScore = 700
print(s.totalScore)
