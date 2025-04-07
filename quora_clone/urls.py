from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

handler404  = 'apps.core.views.error_404_view'
handler500  = 'apps.core.views.error_500_view'