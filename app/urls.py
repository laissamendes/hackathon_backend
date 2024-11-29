from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter
from uploader.router import router as uploader_router
from core.views import UserViewSet, TurmaViewSet, AlunoViewSet, OcorrenciaViewSet, ProfessorViewSet, DisciplinaViewSet, TrimestreViewSet, ConselhoClasseViewSet, PreConselhoViewSet, AlunoTemDisciplinaViewSet

router = DefaultRouter()

router.register(r"usuarios", UserViewSet, basename="usuarios")
router.register(r"turmas", TurmaViewSet, basename="turma")
router.register(r"alunos", AlunoViewSet, basename="aluno")
router.register(r"ocorrencias", OcorrenciaViewSet, basename="ocorrencias")
router.register(r"professores", ProfessorViewSet, basename="professor")
router.register(r"disciplinas", DisciplinaViewSet, basename="disciplina")
router.register(r"trimestres", TrimestreViewSet, basename="trimestre")
router.register(r"conselho-classe", ConselhoClasseViewSet, basename="conselho-classe")
router.register(r"pre-conselho", PreConselhoViewSet, basename="pre-conselho")
router.register(r"aluno-tem-disciplina", AlunoTemDisciplinaViewSet, basename="aluno-tem-disciplina")

urlpatterns = [
    path("admin/", admin.site.urls),
    # OpenAPI 3
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    # API
    path("api/", include(router.urls)),
    path("api/media/", include(uploader_router.urls)),
]
urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)

