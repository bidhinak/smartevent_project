from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from event_app import views

urlpatterns=[
    path("", views.home,name="home"),
    path("Login",views.Login,name="Login"),
    path("signupteacher",views.teacher_signup,name="teacher_signup"),
    path("signupstudent",views.students_signup,name="student_signup"),
    path("Loginview",views.Login_view,name="Login_view"),
    path("teacherpage",views.teacherpage,name="teacherpage"),
    path("studentpage", views.studentpage, name="studentpage"),
    path("adminpage", views.adminpage, name="adminpage"),
    path("studentview",views.studentview,name="studentview"),
    path("teacherview",views.teacherview,name="teacherview"),
    path("adminstudentupdate/<int:id>/",views.adminstdupdate,name="adminstdupdate"),
    path("adminstudentdelete/<int:id>/",views.adminstddelete,name="adminstddelete"),
    path("adminteacherupdate/<int:id>/", views.admintchrupdate, name="admintchrupdate"),
    path("adminteacherdelete/<int:id>/", views.admintchrdelete, name="admintchrdelete"),
    path("viewclub",views.adminclubview,name="viewclub"),
    path("addclub",views.adminclubadd,name="addclub"),
    path("updateclub/<int:id>/",views.clubupdate,name="clubupdate"),
    path("deleteclub/<int:id>/",views.clubdelete,name="clubdelete"),
    path("teacherclubview",views.teacherclubview,name="teacherclubview"),
    path("studentclubview",views.studentclubview,name="studentclubview"),
    path("teachereventdetails/<int:id>/",views.tchreventdetails,name="tchreventdetails"),
    path("teachereventview",views.tchreventview,name="tchreventview"),
    path("teachereventupdate/<int:id>/",views.tchreventupdate,name="tchreventupdate"),
    path("teachereventdelete/<int:id>/",views.tchreventdelete,name="tchreventdelete"),
    path("adminnotification",views.adminnotification,name="adminnotification"),
    path("adminnotificationview",views.adminnotificationview,name="adminnotificationview"),
    path("notificationupdate/<int:id>/",views.adminnotificationupdate,name="notificationupdate"),
    path("notificationdelete/<int:id>/",views.adminnotificationdelete,name="notificationdelete"),
    path("teachernotificationview",views.teachernotificationview,name="tchrnotificationview"),
    path("studentnotificationview", views.studentnotificationview, name="stdnotificationview"),
    path("studentfeedback",views.studentfeedback,name="stdfeedback"),
    path("studentfeedbackview",views.studentfeedbackview,name="stdfeedbackview"),
    path("adminfeedbackview",views.adminfeedbackview,name="adminfeedbackview"),
    path("adminfeedbackreply/<int:id>/",views.adminfeedbackreply,name="adminfeedbackreply"),
    path("adminfeedbackdelete/<int:id>/",views.adminfeedbackdelete,name="adminfeedbackdelete"),
    path("teacherfeedbackview",views.teacherfeedbackview,name="teacherfeedbackview")

]
