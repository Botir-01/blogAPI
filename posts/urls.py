from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views
router = SimpleRouter()
router.register('users', views.UserViewSet, basename='users')
router.register('', views.PostViewSet, basename='posts')

urlpatterns = router.urls

# urlpatterns = [
#     path('users', views.UserList.as_view()),
#     path('users/<int:pk>/', views.UserDetail.as_view()),
#     path('<int:pk>/', views.PostDetail.as_view()),
#     path('', views.PostList.as_view()),
# ]
