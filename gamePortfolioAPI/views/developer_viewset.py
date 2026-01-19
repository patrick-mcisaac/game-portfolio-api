from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status, serializers
from rest_framework.decorators import action
from gamePortfolioAPI.models import Developer


class DeveloperView(ViewSet):
    """
    View sets for developer model
    """

    @action(detail=False, methods=["get"])
    def get_details(self, request):
        username = request.query_params.get("username")

        if username is not None:
            developer = Developer.objects.filter(username=username)
            ser = DeveloperSerializer(developer, many=True)
            return Response(ser.data, status=status.HTTP_200_OK)
        return Response(None, status=status.HTTP_400_BAD_REQUEST)


class DeveloperSerializer(serializers.ModelSerializer):
    """
    Serializer for Developer Model
    """

    class Meta:
        model = Developer
        fields = ("first_name", "last_name", "username", "logo", "about")
