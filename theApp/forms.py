from django import forms
from . import models


# This file controls all the forms in this web application by labelling them and
# even dictates the form of the html page. Here, I just defined the fields of the
# forms and relabelled them.

class appUploadForm(forms.ModelForm):
    class Meta:
        model = models.appUpload
        fields = ['title', 'image', 'file']
        labels = {
            'title': 'Title',
            'image': 'Cover image',
            'file': 'File',
        }
    

class bookUploadForm(forms.ModelForm):
    class Meta:
        model = models.bookUpload
        fields = ['title', 'image', 'file']
        labels = {
            'title': 'Title',
            'image': 'Cover Image',
            'file': 'File',
        }


class miscUploadForm(forms.ModelForm):
    class Meta:
        model = models.miscUpload
        fields = ['title', 'image', 'file']
        labels = {
            'title': 'Title',
            'image': 'Cover Image',
            'file': 'File',
        }


class moviesUploadForm(forms.ModelForm):
    class Meta:
        model = models.moviesUpload
        fields = ['title', 'image', 'file']
        labels = {
            'title': 'Title',
            'image': 'Cover Image',
            'file': 'File',
        }

class appRequestForm(forms.ModelForm):
    class Meta:
        model = models.apprequest
        fields = ['requestname']
        labels = {
            'requestname': 'Request Name',
        }


class bookRequestForm(forms.ModelForm):
    class Meta:
        model = models.bookrequest
        fields = ['requestname']
        labels = {
            'requestname': 'Request Name',
        }

class miscRequestForm(forms.ModelForm):
    class Meta:
        model = models.miscrequest
        fields = ['requestname']
        labels = {
            'requestname': 'Request Name',
        }

class moviesRequestForm(forms.ModelForm):
    class Meta:
        model = models.moviesrequest
        fields = ['requestname']
        labels = {
            'requestname': 'Request Name',
        }