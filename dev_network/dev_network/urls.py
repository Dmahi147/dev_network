"""dev_network URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path(
        'dev/',
        include('pages.urls', namespace='pages')
    ),
    path(
        'dev/accounts/',
        include('accounts.urls', namespace='accounts')
    ),
    path(
        'dev/posts/',
        include('posts.urls', namespace='posts')
    ),
    path(
        'dev/posts/',
        include('likes.urls', namespace='likes')
    ),
    path(
        'dev/posts/',
        include('unlikes.urls', namespace='unlikes')
    ),
    path(
        'dev/posts/',
        include('comments.urls', namespace='comments')
    ),
    path(
        'dev/profiles/',
        include('profiles.urls', namespace='profiles')
    ),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
