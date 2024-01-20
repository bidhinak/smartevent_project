from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from event_app.forms import UserCreationForm, customform, Teacherform, Studentform, Clubform, Eventform, \
    Notificationform, Feedbackform, Adminfeedbackform
from event_app.models import teacher, student, club, event, notification, Feedback


# Create your views here.
def home (request):
    return render(request,"homepage.html")

def Login(request):
    return render(request,'loginpage.html')

def teacher_signup(request):
    login_form=customform()
    teacher_form=Teacherform()
    if request.method == "POST":
        login_form=customform(request.POST)
        teacher_form=Teacherform(request.POST)
        if login_form.is_valid() and teacher_form.is_valid():
            user2=login_form.save(commit=False)
            user2.is_teacher=True
            user2.save()
            user1=teacher_form.save(commit=False)
            user1.name1=user2
            user1.save()
            return redirect('Login')
    return render(request,'teachertemplate/teacher.html',{"login_form":login_form,"teacher_form":teacher_form})


def students_signup(request):
    login_form=customform()
    student_form=Studentform()
    if request.method == "POST":
        login_form=customform(request.POST)
        student_form=Studentform(request.POST)
        if login_form.is_valid() and student_form.is_valid():
            user2=login_form.save(commit=False)
            user2.is_student=True
            user2.save()
            user1=student_form.save(commit=False)
            user1.name2=user2
            user1.save()
            return redirect('Login')
    return render(request,'studenttemplate/student.html',{"login_form":login_form,"student_form":student_form})

# for login
def Login_view(request):
    if request.method == 'POST':
        username=request.POST.get('uname')
        password=request.POST.get('pass')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('adminpage')
            elif user.is_teacher:
                return redirect('teacherpage')
            elif user.is_student:
                return redirect('studentpage')
        else:
            messages.info(request,'Invalid Credentials')
    return render(request,'loginpage.html')

def adminpage(request):
    return render(request,'admintemplate/adminview.html')

def studentpage(request):
    return render(request,'studenttemplate/studentpage.html')

def teacherpage(request):
    return render(request,'teachertemplate/teacherpage.html')

# teacher and student view in admin
def studentview(request):
    data=student.objects.all()
    return render(request,'admintemplate/studentview.html',{"data":data})

def teacherview(request):
    data2=teacher.objects.all()
    return render(request,'admintemplate/teacherview.html',{"data":data2})

# admin student update and delete button
def adminstdupdate(request,id):
    value=student.objects.get(id=id)
    show=Studentform(instance=value)
    if request.method =='POST':
        show=Studentform(request.POST,instance=value)
        if show.is_valid():
            show.save()
            return redirect('studentview')
    return render(request,'admintemplate/studentupdate.html',{"show":show})

def adminstddelete(request,id):
    data=student.objects.get(id=id)
    data.delete()
    return redirect('studentview')

def admintchrupdate(request,id):
    value=teacher.objects.get(id=id)
    show2=Teacherform(instance=value)
    if request.method =='POST':
        show2=Teacherform(request.POST,instance=value)
        if show2.is_valid():
            show2.save()
            return redirect('teacherview')
    return render(request,'admintemplate/teacherupdate.html',{"show":show2})

def admintchrdelete(request,id):
    data2=teacher.objects.get(id=id)
    data2.delete()
    return redirect('teacherview')

# club view in admin
def adminclubview(request):
    view=club.objects.all()
    return render(request,'admintemplate/viewclub.html',{"view":view})

def adminclubadd(request):
    addview = Clubform()
    if request.method=='POST':
        addview = Clubform(request.POST,request.FILES)
        if addview.is_valid():
            addview.save()
            return redirect('adminpage')
    return render(request,'admintemplate/addclub.html',{"addview":addview})

# club update and delete
def clubupdate(request,id):
    view=club.objects.get(id=id)
    viewhere=Clubform(instance=view)
    if request.method=='POST':
        viewhere=Clubform(request.POST,request.FILES,instance=view)
        if viewhere.is_valid():
            viewhere.save()
            return redirect('viewclub')
    return render(request,'admintemplate/clubupdate.html',{"viewhere":viewhere})

def clubdelete(request,id):
    delt=club.objects.get(id=id)
    delt.delete()
    return redirect('viewclub')

# teacher and student clubview
def teacherclubview(request):
    view = club.objects.all()
    return render(request,'teachertemplate/teacherclubview.html',{"view":view})

def studentclubview(request):
    view = club.objects.all()
    return render(request,'studenttemplate/studentclubview.html',{"view":view})

def tchreventdetails(request,id):
    data=club.objects.get(id=id)
    show=Eventform
    if request.method == 'POST':
        show=Eventform(request.POST)
        if show.is_valid():
            d=show.save(commit=False)
            d.club_name=data
            d.save()
            # return redirect('')
    return render(request,'teachertemplate/tchreventdetails.html',{"show":show})

def tchreventview(request):
    view=event.objects.all()
    return render(request,'teachertemplate/tchreventview.html',{"view":view})

def tchreventupdate(request,id):
    data=event.objects.get(id=id)
    view=Eventform(instance=data)
    if request.method =='POST':
        view=Eventform(request.POST,instance=data)
        if view.is_valid():
            view.save()
            return redirect('tchreventview')
    return render(request,'teachertemplate/eventupdate.html',{"view":view})

def tchreventdelete(request,id):
    delt=event.objects.get(id=id)
    delt.delete()
    return redirect('tchreventview')

# admin notification views
def adminnotification(request):
    notf=Notificationform()
    if request.method == 'POST':
        notf=Notificationform(request.POST)
        if notf.is_valid():
            notf.save()
            return redirect('adminnotificationview')
    return render(request,'admintemplate/adminnotification.html',{"view":notf})

def adminnotificationview(request):
    show=notification.objects.all()
    return render(request,'admintemplate/adminnotfview.html',{"show":show})

def adminnotificationupdate(request,id):
    take=notification.objects.get(id=id)
    give=Notificationform(instance=take)
    if request.method == 'POST':
        give=Notificationform(request.POST,instance=take)
        if give.is_valid():
            give.save()
            return redirect('adminnotificationview')
    return render(request,'admintemplate/notificationupdate.html',{"up":give})

def adminnotificationdelete(request,id):
    delt=notification.objects.get(id=id)
    delt.delete()
    return redirect('adminnotificationview')

 # notification  view to student and teacher
def teachernotificationview(request):
    notf=notification.objects.all()
    return render(request,'teachertemplate/tchrnotificationview.html',{"view":notf})

def studentnotificationview(request):
    notf=notification.objects.all()
    return render(request,'studenttemplate/stdnotfview.html',{"view":notf})

# study ginga
# feedback

def studentfeedback(request):
    feed=Feedbackform()
    user1=request.user
    if request.method == 'POST':
        feed=Feedbackform(request.POST)
        if feed.is_valid():
            data=feed.save(commit=False)
            data.user=user1
            data.save()
            return redirect('stdfeedbackview')
    return render(request,'studenttemplate/studentfeedback.html',{"view":feed})

def studentfeedbackview(request):
    u=request.user.id
    feedview=Feedback.objects.filter(user=u)
    return render(request,'studenttemplate/stdfeedbackview.html',{"show":feedview})

def adminfeedbackview(request):
    adminview=Feedback.objects.all()
    return render(request,'admintemplate/adminfeedbackview.html',{"view":adminview})

def adminfeedbackreply(request,id):
    feed=Feedback.objects.get(id=id)
    print(feed)
    # show=Adminfeedbackform(instance=feed)
    if request.method == 'POST':
        show=Adminfeedbackform(request.POST,instance=feed)
        print(show)
        if show.is_valid():

            show.save()
            return redirect('adminfeedbackview')
    return render(request,'admintemplate/feedbackreply.html',{"reply":feed})

# def adminfeedbackreply(request,id):
#     feed=Feedback.objects.get(id=id)
#     if request.method=='POST':
#         r=request.POST.get('reply')
#         feed.reply=r
#         feed.save()
#
#     return render(request,'admintemplate/feedbackreply.html',{"reply":feed})

def adminfeedbackdelete(request,id):
    delt=Feedback.objects.get(id=id)
    delt.delete()
    return redirect('adminfeedbackview')

def teacherfeedbackview(request):
    show=Feedback.objects.all()
    return render(request,'teachertemplate/teacherfeedbackview.html',{"here":show})