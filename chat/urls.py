from django.urls import path, include

urlpatterns = [
    path('chat/', include('core.urls')),
]
