from django.shortcuts import render
from .models import Semester, Term, Course
from django.http import  HttpResponseRedirect
from django.urls import reverse

def index (request):
    semester_all = Semester.objects.all()
    context = {'semester_all' : semester_all}
    return render(request,'GPA/index.html',context)

def TermView(request,semester_id):
    semester = Semester.objects.get(id=semester_id)
    context = {'semester' : semester}
    return render(request,'GPA/term.html',context)

def CourseView(request,semester_id,term_id):
    semester = Semester.objects.get(id=semester_id)
    term = semester.term_set.get(id=term_id)
    context = {'semester' : semester,
               'term' : term}
    return render(request,'GPA/course.html',context)

def addCourse(request,semester_id,term_id):
    id = request.POST['id']
    title = request.POST['title']
    g = request.POST['grade']
    c = request.POST['credit']
    semester = Semester.objects.get(id=semester_id)
    term = semester.term_set.get(id=term_id)
    c1 = term.course_set.create(course_id=id,course_title=title,grade=g,credit=c)
    c1.save()
    return HttpResponseRedirect(reverse('GPA:course', args=(semester_id,term_id,)))
    