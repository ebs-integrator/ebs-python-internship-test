from django.contrib.auth.models import User
from drf_util.decorators import serialize_decorator
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from apps.comments.models import Comment
from apps.comments.serializers import CommSerializer

# Create your views here.

class CommItemPost(GenericAPIView):
    serializer_class = CommSerializer
    permission_classes = (AllowAny,)

    @serialize_decorator(CommSerializer)
    def post(self, request):
        validated_data = request.serializer.validated_data

        comment = Comment.objects.create(
            **validated_data,
        )
        comment.save()

        return Response(CommSerializer(comment).data)