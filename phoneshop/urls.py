from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/', include(('store.urls', 'store'), namespace='store_unique')),
    path('', include('store.urls')),
]