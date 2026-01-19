from rest_framework import status, serializers
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from gamePortfolioAPI.models import Contact


class ContactViews(ViewSet):

    @action(methods=["get"], detail=False)
    def get_dev_contact(self, request):
        dev = request.query_params.get("dev", None)
        name = request.query_params.get("name", None)
        if dev is not None and name is not None:
            try:
                # get contact where the related developer username is the param
                contact = Contact.objects.get(developer__username=dev, name=name)
                ser = ContactSerializer(contact, many=False)
                return Response(ser.data, status=status.HTTP_200_OK)
            except Contact.DoesNotExist as ex:
                return Response({"ERROR": str(ex)})


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ("id", "name", "link")
