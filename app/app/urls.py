from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers


from users import views


router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    # Add Log in Button in rest_framework page
    path("api-auth/", include("rest_framework.urls")),
    path("snippets/", include("snippets.urls")),
]

urlpatterns += router.urls