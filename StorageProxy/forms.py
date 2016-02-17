from django import forms


class UploadForm(forms.Form):
    key = forms.CharField(
        label='Key',
        min_length=1,
        max_length=1000,
    )
    comment = forms.CharField(
        label='Comment',
        widget=forms.Textarea,
        required=False,
    )
    file = forms.FileField(
        label='File',
        allow_empty_file=False,
    )