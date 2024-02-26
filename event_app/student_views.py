from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from event_app.models import student


@login_required(login_url='Login_view')
def studentpage(request):
    u=request.user
    show= student.objects.get(name2=u)
    return render(request,'studenttemplate/studentpage.html',{"show":show})
