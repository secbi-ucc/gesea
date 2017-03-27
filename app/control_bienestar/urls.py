from django.conf.urls import include, url
from django.contrib import admin



urlpatterns = [

    url(r'^$', include('core.urls')),
    url(r'^admin/', admin.site.urls),

    # Django-Select2
    url(r'^select2/', include('django_select2.urls')),

]
