from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from .serializers import *
from rest_framework.authentication import TokenAuthentication
from users.models import CustomUser, TelegramUser, GroupUserTelegram
from rest_framework import mixins
from django.db.models import Q
from .models import Schedule
from rest_framework import status
from .filters import TelegramUsersFilter
from django_filters import rest_framework as filters


class ScheduleViewSet(mixins.CreateModelMixin,
                      viewsets.GenericViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


class NumberWeekAPI(generics.RetrieveUpdateAPIView):
    queryset = NumberWeek.objects.all()
    serializer_class = NumberWeekSerializer
    permission_classes = (permissions.IsAdminUser,)


class GroupApiView(APIView):
    def get(self, request):
        q = CustomUser.objects.filter(~Q(username='root')).values('username', 'group', 'verified')
        return Response(q)


class TypeListView(generics.ListAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class GetScheduleView(generics.RetrieveAPIView):
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all()

    def retrieve(self, request, *args, **kwargs):
        group = CustomUser.objects.filter(username=self.request.query_params.get('token')).first()
        instance = self.queryset.filter(group=group.pk,
                                        week=kwargs.get('week'),
                                        day=kwargs.get('day'),
                                        number_pair=kwargs.get('number')).first()

        if not bool(instance):
            return Response({})
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class TelegramUserListOrUpdateOrCreate(
    generics.CreateAPIView,
    generics.UpdateAPIView,
    generics.DestroyAPIView,
    generics.ListAPIView,
):
    queryset = TelegramUser.objects.all()
    serializer_class = TelegramUserSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TelegramUsersFilter


class GroupUserCreateOrDeleteOrList(generics.CreateAPIView,
                                    generics.DestroyAPIView,
                                    generics.ListAPIView):
    queryset = GroupUserTelegram.objects.all()
    serializer_class = GroupUserTelegramSerializer

    def destroy(self, request, *args, **kwargs):
        telegram_id = self.request.query_params.get('telegram_id')
        token = self.request.query_params.get('token')
        try:
            self.queryset.get(user__telegram_id=telegram_id, token=token).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except GroupUserTelegram.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get_queryset(self):
        telegram_id = self.request.query_params.get('telegram_id')
        return self.queryset.filter(user__telegram_id=telegram_id).values()


class ScheduleViewList(generics.ListAPIView):
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all()

    def list(self, request, *args, **kwargs):
        group = CustomUser.objects.filter(username=self.request.query_params.get('token')).first()
        if self.request.query_params.get('day'):
            instances = self.queryset.filter(group=group.pk,
                                             week=self.request.query_params.get('week'),
                                             day=self.request.query_params.get('day'))

        elif self.request.query_params.get('week'):
            instances = self.queryset.filter(group=group.pk,
                                             week=self.request.query_params.get('week'))

        else:
            instances = self.queryset.filter(group=group.pk)

        if not bool(instances):
            return Response({})
        serializer = self.serializer_class(instances, many=True)
        return Response(serializer.data)
