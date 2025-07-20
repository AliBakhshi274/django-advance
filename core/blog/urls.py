from django.urls import path
from .views import indexView, IndexView
# from django.views.generic import TemplateView

urlpatterns = [
    path('fbv-index/', indexView, name='fbv-index'),
    # path('cbv-index/', TemplateView.as_view(template_name="index.html", extra_context={'name': 'Django Advance'}), name='cbv-index'),  
    path('cbv-index/', IndexView.as_view(), name='cbv-index')
]