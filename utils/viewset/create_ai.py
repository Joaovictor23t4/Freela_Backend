from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from utils.mixins.create_ads import CreateAdsModelMixin

class AdsModelViewSet(CreateAdsModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.UpdateModelMixin,
                      GenericViewSet):
    pass