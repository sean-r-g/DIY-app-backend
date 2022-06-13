from django_urls import path
from . import views

urlpatterns = [
    path('/guides', views.GuideList.as_view(), name='guide_list'),
    path('/guides/<int:pk>', views.GuideDetail.as_view(), name='guide_detail')
]