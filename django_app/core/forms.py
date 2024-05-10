


from django import forms

ONE_GB = 1e+9

class UploadForm(forms.Form):
    title = forms.CharField(max_length=20)
    file = forms.FileField(
        max_length=ONE_GB,
        allow_empty_file=False
        # TODO: add multiple checks to make filter files
    )

