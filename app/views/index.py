from django.views import generic


class IndexView(generic.TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result["title"] = "Recipe home"
        return result
