from collections import OrderedDict

from django import forms

from app.models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ("title", "summary", "content", "image")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        title = forms.CharField(max_length=200, required=True)
        summary = forms.CharField(max_length=200, required=True)
        content = forms.CharField(
            max_length=200, required=True, widget=forms.Textarea
        )
        image = forms.ImageField()
        self.fields = OrderedDict(
            {"title": title, "summary": summary, "content": content, "image": image}
        )

    def clean_title(self):
        result = self.cleaned_data["title"]
        if any([c in result for c in '<>"']):
            self.add_error("title", "Forbidden char")
        return result

    def clean(self):
        title = self.cleaned_data["title"]
        summary = self.cleaned_data["summary"]
        if title == summary:
            self.add_error("title", "Same as summary")
            self.add_error("summary", "Same as title")
            self.add_error(None, "Do something clever")
        return self.cleaned_data


