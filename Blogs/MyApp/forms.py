from django import forms
from .models import BlogDetails,UserInfo

class BlogDetailsForm(forms.ModelForm):
    # user = forms.ModelChoiceField(queryset=UserInfo.objects.get(username=request.session["uname"]))
    class Meta:
        model = BlogDetails
        fields = '__all__'
