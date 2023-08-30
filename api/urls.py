from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.FruitsViewSetApiView)


urlpatterns = [
    path('function/', views.all_todos),
    path('function/<int:todo_id>', views.todo_detail_view),
    path('cbv/', views.FruitsListApiView.as_view()),
    path('cbv/<int:todo_id>', views.FruitsDetailApiView.as_view()),
    path('mixins/', views.FruitsListMixinApiView.as_view()),
    path('mixins/<pk>', views.FruitsDetailMixinApiView.as_view()),
    path('generics/', views.FruitsGenericApiView.as_view()),
    path('generics/<pk>', views.FruitsGenericDetailView.as_view()),
    path('viewsets/', include(router.urls)),
    # path('users/', views.UsersGenericApiView.as_view()),
]