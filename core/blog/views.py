from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Post

# Create your views here.
def indexView(request):
    """
    a function based view to show index page
    """
    return render(request=request, template_name="index.html", context={'name':"Django Advance"})

class IndexView(TemplateView):
    """
    a class based view to show index page
    """
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Django Advance'
        context['posts'] = Post.objects.all()[:3]
        return context