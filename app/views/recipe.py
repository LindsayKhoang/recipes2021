from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages

from app.forms.recipe import RecipeForm
from app.models import Recipe


class RecipeListView(generic.ListView):
    model = Recipe

    def get_context_data(self, *, object_list=None, **kwargs):
        result = super().get_context_data(**kwargs)
        result["title"] = "Recipe list"
        return result

    template_name = "recipe_list.html"


class RecipeByIngredientListView(generic.ListView):
    template_name = "recipe_list.html"

    def get_queryset(self):
        return Recipe.objects.filter(
            Q(
                ingredients__ingredient__name_singular__icontains=self.kwargs[
                    "ingredient"
                ]
            )
            | Q(
                ingredients__ingredient__name_plural__icontains=self.kwargs[
                    "ingredient"
                ]
            )
        )

    def get_context_data(self, *, object_list=None, **kwargs):
        result = super().get_context_data(**kwargs)
        result["title"] = "Recipe list"
        return result


class RecipeDetailView(generic.DetailView):
    model = Recipe
    template_name = "recipe_detail.html"


class RecipeCreateView(LoginRequiredMixin, generic.FormView):
    form_class = RecipeForm
    template_name = "recipe_form.html"

    def get_success_url(self):
        return reverse_lazy("recipe_list")

    def form_valid(self, form):
        title = form.cleaned_data["title"]
        content = form.cleaned_data["content"]
        summary = form.cleaned_data["summary"]
        Recipe.objects.create(title=title, content=content, summary=summary)
        return super().form_valid(form)


class RecipeUpdateView(LoginRequiredMixin, generic.UpdateView):
    success_url = reverse_lazy("recipe_list")
    model = Recipe
    form_class = RecipeForm
    template_name = "recipe_form.html"


class RecipeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Recipe
    template_name = "recipe_delete.html"

    def get_success_url(self):
        messages.success(self.request, "Deletion successful")
        return reverse_lazy("recipe_list")
