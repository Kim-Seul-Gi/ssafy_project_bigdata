from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from api.models import Profile, Subscription_manager
from rest_framework.response import Response
from api.serializers import SubscriptionSerializer
import datetime
@api_view(['POST'])
def create(request):
    if request.method == 'POST':

    # Subscription_manager 이라는 모델에 생성을 해야 한다.
        username = request.data.get('user')
        user = User.objects.get(username=username)
        profile = Profile.objects.get(user=user)

        check_subscription_request = Subscription_manager.objects.filter(Profile=profile, approval=False)
        if check_subscription_request:
            message = {'message':'이미 구독 신청을 한 상태입니다.'}
            return Response(data=message, status=status.HTTP_200_OK)
        else:
            subscription_request = Subscription_manager.objects.create(
                Profile=profile,
                request=request.data.get('request'),
                approval=False,
            )
            return Response(status=status.HTTP_200_OK)

@api_view(['GET','POST'])
def manager(request):
    if request.method == 'GET':
        subscriptions = Subscription_manager.objects.filter(approval=False)
        serializer = SubscriptionSerializer(subscriptions, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        subscription = request.data.get('subscription')
        profile = Profile.objects.get(pk=subscription['Profile'])

        # 1. Profile 변경 (처음 신청했을 때, 만료 이후 재신청했을 때, 연장신청했을 때 모두 여기에 해당한다.)

        if profile.subscription.strftime("%Y%m%d") > datetime.datetime.now().strftime("%Y%m%d"):
            # 이것이 바로 연장
            profile.subscription = profile.subscription + datetime.timedelta(days=subscription['request'])
            profile.save()
        else:
            # 이것은 처음 신청, 또는 만료 이후 다시 신청
            profile.approval = True
            profile.subscription = datetime.datetime.now() + datetime.timedelta(days=subscription['request'])
            profile.save()

        # 2. Subscription_manager 에서 해당 객체 승인 되었다고 변경
        subscription_instance = Subscription_manager.objects.get(pk=subscription['id'])
        subscription_instance.approval = True
        subscription_instance.save()

        return Response(status=status.HTTP_200_OK)
