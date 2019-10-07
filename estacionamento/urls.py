from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(r'', include('website.urls')),
    path(r'sistema/', include('core.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),         

]
