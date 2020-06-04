from django.urls import path
from . import views

urlpatterns = [

]

urlpatterns = [
    path('', views.index, name='index'), path('measures/', views.MeasureListView.as_view(), name='measures'), path('measure/<int:pk>', views.MeasureDetailView.as_view(), name='measure-detail'),
]