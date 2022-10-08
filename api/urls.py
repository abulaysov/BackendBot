from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter
from .views import *
from users.views import UserViewSet
router = SimpleRouter()

router.register('schedule', ScheduleViewSet)
router.register('events', EventDetailOrList)
router.register('telegram/user', TelegramUserViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('drf-auth/', include('rest_framework.urls')),
    path('number-week/<pk>/', NumberWeekAPI.as_view()),
    # path(r'auth/detail/', include('djoser.urls')),
    path(r'auth/', include('djoser.urls.authtoken')),
    path(r'list/group/', GroupApiView.as_view()),
    path('type-pair/', TypeListView.as_view()),
    path('get-pair/<int:week>/<int:day>/<int:number>/', ScheduleRetrieveOrDestroy.as_view()),
    # path('telegram/detail/user/', TelegramUserListOrUpdateOrCreate.as_view()),
    # path('telegram/detail/user/<int:telegrr>/', TelegramUserListOrUpdateOrCreate.as_view()),
    path('telegram/detail/group/', GroupUserCreateOrDeleteOrList.as_view()),
]
