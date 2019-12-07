from django import forms
from .models import Report
#, Image

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('title', 'author', 'bank_name', 'started_date', 'invest', 'withdrew',
        'gain_loss', 'face_value', 'cover', 'venue', 'officer', 'text')

""" class ImageForm(forms.ModelForm):
    class Meta:
        model= Image
        fields= ('name', 'imagefile') """