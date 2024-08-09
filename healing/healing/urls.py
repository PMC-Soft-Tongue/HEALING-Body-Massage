from django.contrib import admin
from django.urls import include, path, reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
    path('comments/', include('comments.urls', namespace='comments')),
    path('admin/', admin.site.urls),
    path('auth/registration', CreateView.as_view(
        template_name='registration/registration_form.html',
        form_class=UserCreationForm,
        success_url=reverse_lazy('pages:homepage')
    ),
         name='registration'
         ),
    path('auth/', include('django.contrib.auth.urls')),
    path('', include('pages.urls', namespace='pages')),
]
