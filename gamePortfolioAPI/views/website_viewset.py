from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gamePortfolioAPI.models import Website, WebsiteImage


class WebsiteViews(ViewSet):
    """Viewset for Websites"""

    def list(self, request):
        """
        List all the websites
        """
        websites = Website.objects.all().prefetch_related()
        ser = WebsiteSerializer(websites, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)


class WebsiteImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = WebsiteImage
        fields = ("id", "image")


class WebsiteSerializer(serializers.ModelSerializer):

    images = WebsiteImageSerializer(many=True)

    class Meta:
        model = Website
        fields = ("id", "description", "learned", "link", "title", "images")
