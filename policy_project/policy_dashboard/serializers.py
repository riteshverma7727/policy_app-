from rest_framework import serializers
from .models import Policy
from .models import Comment
# Serializers for Policy 
class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = '__all__'

# Serializers for Comments
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
