from typing import List

from django.shortcuts import get_object_or_404
from ninja import ModelSchema, Router, Schema

from apps.project.models import Project

project_router = Router(
    tags=["Projet"],
    auth=None,
)


class ProjectRequest(ModelSchema):
    class Meta:
        model = Project
        fields = ["number", "name", "description"]


class ProjectResponse(ModelSchema):
    class Meta:
        model = Project
        fields = ["id", "number", "name", "description", "created_at", "updated_at"]


class SuccessResponse(Schema):
    message: str


class ErrorResponse(Schema):
    message: str


@project_router.post(
    "/add",
    summary="Ajouter un nouveau projet",
    response={200: SuccessResponse, 500: ErrorResponse},
)
def add_project(request, payload: ProjectRequest):
    """
    Ajoute un nouveau projet dans la base de données.
    """
    try:
        Project.objects.create(**payload.dict())
        return SuccessResponse(message="Projet créé avec succès")
    except Exception as e:
        return ErrorResponse(message=str(e))


@project_router.get(
    "/all",
    summary="Récupérer tous les projets",
    response=List[ProjectResponse],
)
def get_projects(request):
    """
    Récupère l'ensemble des projets enregistrés dans la base de données.
    """
    return list(Project.objects.all())


@project_router.get(
    "/{project_number}",
    summary="Récupérer un projet par son numéro",
    response={200: ProjectResponse},
)
def get_project(request, project_number: str):
    """
    Récupère un projet par son numéro de devis ou son numéro de projet.
    TODO : utiliser un schéma en paramètre.
    """
    project = get_object_or_404(Project, number=project_number)
    return project


@project_router.put(
    "/{project_number}",
    summary="Mettre à jour un projet",
    response={200: SuccessResponse, 404: ErrorResponse},
)
def update_project(request, project_number: str, payload: ProjectRequest):
    """
    Met à jour un projet existant dans la base de données.
    """
    project = get_object_or_404(Project, number=project_number)
    for attr, value in payload.dict(exclude_unset=True).items():
        setattr(project, attr, value)
    project.save()
    return SuccessResponse(message="Projet mis à jour avec succès")


@project_router.delete(
    "/{project_number}",
    summary="Supprimer un projet",
    response={200: SuccessResponse, 404: ErrorResponse},
)
def delete_project(request, project_number: str):
    """
    Supprime un projet existant dans la base de données.
    """
    project = get_object_or_404(Project, number=project_number)
    project.delete()
    return SuccessResponse(message="Projet supprimé avec succès")
