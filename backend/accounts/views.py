from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from accounts.models import TelegramUser


class TelegramUserRegisterView(APIView):

    def post(self, request):
        telegram_id = request.data.get("telegram_id")
        full_name = request.data.get("full_name")

        if not telegram_id:
            return Response(
                {"error": "telegram_id is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user, created = TelegramUser.objects.get_or_create(
            telegram_id=telegram_id,
            defaults={"full_name": full_name}
        )

        if not created and full_name and user.full_name != full_name:
            user.full_name = full_name
            user.save(update_fields=["full_name"])

        return Response(
            {
                "telegram_id": user.telegram_id,
                "full_name": user.full_name,
                "created": created,
            }
        )
