from django.urls import include, path
from payments import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # add this line
    path('payments/', include('payments.urls'))
]