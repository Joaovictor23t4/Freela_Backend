from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.project.views import ProjectView, FinishedProjectAPIView

router = DefaultRouter()
router.register(r"Projetos", ProjectView, basename="Projetos")

urlpatterns = [
    path("", include(router.urls)),
    path("finalizar/",  FinishedProjectAPIView.as_view(), name="Finished")
]