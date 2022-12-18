from django import forms
from .models import Articles

class ArticlesForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = Articles

        # specify fields to be used
        fields = [
            "name",
            "stock",
            "price",
            "image_url"
        ]