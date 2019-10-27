from echo.models import Meizis
from rest_framework import serializers

class MeiziSerializer(serializers.ModelSerializer):
    # ModelSerializer和Django中ModelForm功能相似
    # Serializer和Django中Form功能相似
    class Meta:
        model = Meizis
        # 和"__all__"等价
        fields = ('mid', 'title', 'picname', 'page_url', 'img_url')