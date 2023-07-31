from django import forms


class CommentForm(forms.Form):
    name_comment = forms.CharField(max_length=25)
    email_comment = forms.EmailField(required=False)
    comment = forms.CharField(max_length=1024, required=True)
