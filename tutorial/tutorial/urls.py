from django.conf.urls import include, url
from django.contrib import admin
from quickstart import views
from django.conf import settings
#import debug_toolbar

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^users/$', views.UserList.as_view()),
	url(r'^users/(?P<pk>\d+)/$', views.UserDetail.as_view()),
	url(r'rest-auth/', include('rest_auth.urls')),
	url(r'^silk/', include('silk.urls', namespace='silk')),
	url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
	url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
	url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
	#url(r'__debug__/', include(debug_toolbar.urls))
	#url(r'rest-auth/registration/', include('rest_auth.registration.urls')),
]

# You can use these request to post and get
# curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X GET http://127.0.0.1:8000/users/
# curl -X POST  -H "Accept: Application/json" -H "Content-Type: application/json" http://127.0.0.1:8000/users/ -d '{"username": "xyz","first_name": "ddd","last_name": "fff","email": "som@gmail.com"}' | grep }| python3 -mjson.tool