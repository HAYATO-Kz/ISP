from django.db import models

# Create your models here.
class Semester(models.Model):
    semester = models.IntegerField()
    def __str__(self):
        return str(self.semester)

class Term(models.Model):
    semester = models.ForeignKey(Semester,on_delete=models.CASCADE)
    term = models.IntegerField(default=1)
    def __str__(self):
        return str(self.semester)+ "." + str(self.term)

class Course(models.Model):
    term = models.ForeignKey(Term,on_delete=models.CASCADE)
    course_id = models.IntegerField()
    course_title = models.CharField(max_length=100)
    grade = models.CharField(max_length=1)
    credit = models.IntegerField(default=1)

    def __str__(self):
        return self.course_title + " : " + self.grade