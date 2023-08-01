from rest_framework import generics
from .models import Policy
from .serializers import PolicySerializer

# views for normal CRUD operations 

class PolicyListCreateAPIView(generics.ListCreateAPIView):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer

class PolicyRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer

# views for commnets 

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer

@api_view(['POST'])
def add_comment(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_comments_for_policy(request, policy_id):
    comments = Comment.objects.filter(policy_id=policy_id)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)
