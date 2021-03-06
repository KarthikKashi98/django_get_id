from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import *
from django.db.models import F
import time

from django.http import HttpResponseForbidden
from lock_tokens.exceptions import AlreadyLockedError, UnlockForbiddenError
from lock_tokens.sessions import check_for_session, lock_for_session, unlock_for_session


@api_view(['GET'])
def reset(request):
    Task.objects.filter(id=1).update(given_id= 1)
    api_urls = {
        'id': 'id is set to 1',

    }

    return Response(api_urls)


@api_view(['GET'])
def taskList(request):
    obj = Task.objects.get(id=1)
    while (1):
        try:

            lock_for_session(obj, request.session)
            print("i")

            Task.objects.filter(id=1).update(given_id=F("given_id") + 1)

            serializer = TaskSerializer(Task.objects.all(), many=True)
            print("ii")
            unlock_for_session(obj, request.session)

            return Response(serializer.data)
        except AlreadyLockedError:

            time.sleep(2)


