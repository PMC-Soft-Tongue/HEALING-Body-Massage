from django.urls import path
from pages.views import HomePage
from django.views.generic import TemplateView

app_name = 'pages'

urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('price_list/', TemplateView.as_view(template_name="pages/price_list.html"), name='price_list'),
    path('about_me/', TemplateView.as_view(template_name="pages/about_me.html"), name='about_me'),
    path('gift_card/', TemplateView.as_view(template_name="pages/gift_card.html"), name='gift_card'),
    path('questions/', TemplateView.as_view(template_name="pages/questions.html"), name='questions'),
]
