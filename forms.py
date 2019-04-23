from django import forms
from .models import Registration,LeaveApplication,Complaint
from django.contrib.auth import(authenticate,get_user_model)
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):

    class Meta:
        model = Registration
        fields = ('name', 'mobile','email', 'address','city', 'state','course', 'year','srn', 'gname','gaddress', 'gmobile','password',)


class LeaveApplicationForm(forms.ModelForm):

    class Meta:
        model = LeaveApplication
        fields = ('name', 'block','room_no', 'whereto','stu_mob_no', 'parent_name','par_mob_no', 'leaving_date','arriving_date')
   

class ComplaintForm(forms.ModelForm):

    class Meta:
        model = Complaint
        fields = ('name', 'mobile_no','email_id', 'block','room_no','subject', 'complaint')









User = get_user_model()
class UserLoginForm(forms.Form):
    password1=0
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    def clean(self,*args,**kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if(Registration.objects.filter(name=username).count()>0):
           password1=Registration.objects.get(name=username).password
           #user1=Registration.objects.get(name=username)
           
        else:
           raise forms.ValidationError('This user does not exist')  
        if username and password:
            user= password==password1
            if password1 and not user:
                raise forms.ValidationError('Incorrect Password')
        return super(UserLoginForm,self).clean(*args,**kwargs)






