from django.urls import path
from . import views

app_name = 'GPA'
urlpatterns = [
    path('',views.index,name='index'),
    path('<int:semester_id>/',views.TermView,name='term'),
    path('<int:semester_id>/<int:term_id>/',views.CourseView,name='course'),
    path('<int:semester_id>/<int:term_id>/add/',views.addCourse,name='add')
]