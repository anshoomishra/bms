from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.schemas import SchemaGenerator
from rest_framework.views import APIView
from rest_framework_swagger import renderers
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='DBS - Bakery System')


class SwaggerSchemaView(APIView):
    permission_classes = [AllowAny]
    renderer_classes = [
        # renderers.OpenAPIRenderer,
        renderers.SwaggerUIRenderer
    ]

    def get(self, request):
        generator = SchemaGenerator()
        schema = generator.get_schema(request=request)

        return Response(schema)

