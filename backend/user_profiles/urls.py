from django.urls import path, include
from .views import GetUSerProfileView,  UpadateUserProfileView
urlpatterns = [
    path('user', GetUSerProfileView.as_view()),
    path('update', UpadateUserProfileView.as_view()),
    # path('api-auth/', include('rest_framework.urls'))
]