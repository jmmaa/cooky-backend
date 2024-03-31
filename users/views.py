import io

from django.core import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer


# @api_view(["POST"])
# @permission_classes([IsAuthenticated, IsAdminUser])
# def create_user(request):
#     serializer = UserSerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save()

#         return Response(status=status.HTTP_201_CREATED)

#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(["GET"])
# @permission_classes([IsAuthenticated])
# def get_users(request):
#     users = User.objects.all()  # for now it gets all users

#     json = serializers.serialize("json", users)
#     stream = io.BytesIO(json.encode())
#     data = JSONParser().parse(stream)

#     return Response(data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user(request):
    

    data = UserSerializer(request.user).data

    return Response(data, status=status.HTTP_200_OK)


# @api_view(["PUT"])
# @permission_classes([IsAuthenticated])
# def update_user(request):
#     if (id := request.GET.get("id")) is not None:
#         User.objects.filter(pk=id).update(**request.data)

#         user = User.objects.get(pk=id)
#         user.set_password(user.password)
#         user.save()

#         return Response(status=status.HTTP_202_ACCEPTED)

#     else:
#         return Response(
#             {"detail": "required id field"}, status=status.HTTP_400_BAD_REQUEST
#         )


# @api_view(["DELETE"])
# @permission_classes([IsAuthenticated])
# def delete_user(request):
#     data = request.GET

#     if (id := data.get("id")) is not None:
#         User.objects.filter(pk=id).delete()
#         return Response(status=status.HTTP_202_ACCEPTED)

#     else:
#         return Response(
#             {"detail": "required id field"},
#             status=status.HTTP_400_BAD_REQUEST,
#         )


# auth


@api_view(["POST"])
def signup(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        user.set_password(request.data["password"])
        user.save()

        token = Token.objects.create(user=user)

        return Response({"token": token.key}, status=status.HTTP_201_CREATED)

    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)

    if user is not None:
        try:
            token = Token.objects.get(user=user)

            return Response({"token": token.key}, status=status.HTTP_201_CREATED)

        except Token.DoesNotExist:
            new_token = Token.objects.create(user=user)

            return Response({"token": new_token.key}, status=status.HTTP_201_CREATED)

    else:
        return Response(
            {"detail": "wrong email or password!"}, status=status.HTTP_400_BAD_REQUEST
        )
