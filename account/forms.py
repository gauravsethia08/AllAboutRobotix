from django import forms 
from .models import User

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profile_img']