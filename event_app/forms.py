from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from event_app.models import Login, teacher, student, club, event, notification, Feedback, joinrequest, join


class customform(UserCreationForm):
    username=forms.CharField()
    password1 = forms.CharField(label="password",widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password",widget=forms.PasswordInput)
    class Meta:
        model=Login
        fields=("username","password1","password2")

class Teacherform(forms.ModelForm):
    class Meta:
        model=teacher
        fields='__all__'
        exclude=('name1',)

class Studentform(forms.ModelForm):
    class Meta:
        model=student
        fields='__all__'
        exclude=('name2',)

class Clubform(forms.ModelForm):
    class Meta:
        model=club
        fields='__all__'

class DateInput(forms.DateInput):
    input_type = 'date'
class TimeInput(forms.TimeInput):
    input_type = 'time'

class Eventform(forms.ModelForm):
    event_date = forms.DateField(widget=DateInput)
    start_time= forms.TimeField(widget=TimeInput)
    end_time= forms.TimeField(widget=TimeInput)
    class Meta:
        model=event
        fields='__all__'
        exclude=('club1',)

class Notificationform(forms.ModelForm):
    date= forms.DateField(widget=DateInput)
    class Meta:
        model=notification
        fields='__all__'

class Feedbackform(forms.ModelForm):
    class Meta:
        model=Feedback
        fields="__all__"
        exclude=('reply','user')

class Adminfeedbackform(forms.ModelForm):
      class Meta:
        model=Feedback
        fields="__all__"

class Joinrequestform(forms.ModelForm):
    start_date = forms.DateField(widget=DateInput)
    end_date = forms.DateField(widget=DateInput)
    class Meta:
        model=joinrequest
        fields="__all__"

class Join(forms.ModelForm):
    class Meta:
        model=join
        fields="__all__"