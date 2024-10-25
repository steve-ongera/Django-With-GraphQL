from django.urls import path
from graphene_django.views import GraphQLView
from api.schema import schema
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('graphQL/', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]