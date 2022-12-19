from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('character/', include("character.urls")),
    path('', include("index.urls")),
    path('monster/', include("monster.urls")),
    path('rte/', include("rte.urls")),
    path('encounter/', include("encounter.urls"))
]
