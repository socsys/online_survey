from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


from user.models import UserProfile


class CsrfExemptMixin(object):
    """
    Exempt CSRF for DRF API views.
    """
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(CsrfExemptMixin, cls).as_view(**initkwargs)
        return csrf_exempt(view)


class CreateUserView(CsrfExemptMixin, APIView):
    def post(self, request):
        user_nickname = request.data.get('user_nickname')
        if UserProfile.objects.filter(nickname=user_nickname).exists():
            return Response({"message": "User with this nickname already exists."}, status=status.HTTP_400_BAD_REQUEST)

        user = UserProfile.objects.create_user(nickname=user_nickname)

        return Response({"message": "User created successfully.", "user_id": user.id}, status=status.HTTP_201_CREATED)
