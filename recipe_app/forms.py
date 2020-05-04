from django import forms
from recipe_app.models import Author


class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
            'name'
        ]
    bio = forms.CharField(widget=forms.TextArea)


class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=30)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(widget=forms.TextArea)
    time_required = forms.CharField(max_length=30)
    instructions = forms.CharField(widget=forms.TextArea)
