# courses/forms.py
from django import forms
from .models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['slug', 'title', 'desc', 'image', 'is_free']
        widgets = {
            'slug': forms.TextInput(attrs={'placeholder': 'Enter a unique slug', 'unique': True}),
            'title': forms.TextInput(attrs={'placeholder': 'Course title'}),
            'desc': forms.Textarea(attrs={'placeholder': 'Course description'}),
            'image': forms.ClearableFileInput(attrs={'placeholder': 'Upload an image'}),
            'is_free': forms.CheckboxInput(),
        }