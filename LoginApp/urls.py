from django.contrib import admin
from django.urls import path,include
from dologin import views 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.Loginview, name='index'),
    path('signup/',views.Signupview, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    path('secretpage/',views.secret , name='secret'),
    path('Classview/',views.Classview.as_view(),name='classview'),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
