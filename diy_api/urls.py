
from django.urls import path
from . import views
from .views import MyTokenObtainPairView

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # added below
    path('', views.getUserRoutes),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterUser.as_view(), name='register'),

    path('guides', views.GuideList.as_view(), name='guide_list'),
    path('guides/<int:pk>', views.GuideDetail.as_view(), name='guide_detail')
]
