from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('api-auth/', include('rest_framework.urls',
         namespace='rest_framework')),
    path('editor/', include('django_summernote.urls')),

]

urlpatterns += i18n_patterns(
    path('', include('apps.company.urls')),
    path('', include('apps.users.urls')),
    path('blog/', include('apps.posts.urls')),
)

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
