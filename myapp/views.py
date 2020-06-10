from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Grade, Student


# Create your views here.


def index(request):
    return HttpResponse("wo ke qu ni de ba！")


def grades(request):
    # 找到所有班级
    gradesList = Grade.objects.all()
    print("------", gradesList)
    print("1111111", request)
    return render(request, 'myapp/grades.html', {"grades": gradesList})


def students(request):
    studentsList = Student.objects.all()

    return render(request, 'myapp/students.html', {'students': studentsList})


def studentDetail(request, sid):
    stu = Student.objects.get(pk=sid)
    return render(request, 'myapp/studentDetail.html', {'stu': stu})


def gstudents(request, gid):
    stusList = Student.objects.all().filter(grade_id=gid)
    print("22222222222", stusList)
    # 返回界面
    return render(request, 'myapp/students.html', {'stus': stusList})
