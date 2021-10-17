# -*- coding: utf-8 -*-
import os
import subprocess
from uuid import uuid4

from django.http.request import QueryDict
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, \
    permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions

from .forms import ApiForm
from .serializers import ManoloSerializer
from .api_responses import JSONResponse
from visitors.views import do_pagination, data_as_csv, do_sorting

schema_view = get_schema_view(
    openapi.Info(
        title="Manolo API",
        default_version='v1',
        description='Documentación del API de Manolo.rocks',
        contact=openapi.Contact(email='aniversarioperu1@gmail.com'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


@api_view(['GET'])
@permission_classes((AllowAny, ))
def search(request, query):
    """
    Lista resultados de búsqueda de palabra clave. Usa paginación y muestra
    hasta 20 resultados por página.
    Además muestra links para páginas previas y siguientes.

    # Puedes obtener los resultados en archivo TSV

    Este archivo contiene la información en campos separados por tabs
    (fácil de importar a MS Excel)

    Solo es necesario usar la dirección `search.tsv`:

    * <http://manolo.rocks/api/search.tsv/romulo/>
    ---
    type:
      query:
        required: true
        type: string
    parameters:
      - name: query
        description: nombre o palabra clave a busar, por ejemplo Romulo
        type: string
        paramType: path
        required: true
    """
    query_request = QueryDict('q={}'.format(query))
    form = ApiForm(query_request)
    all_items = form.search()

    # sort queryset
    all_items = do_sorting(request, all_items)

    pagination = PageNumberPagination()
    paginated_results = pagination.paginate_queryset(all_items, request)

    serializer = ManoloSerializer(paginated_results, many=True)

    data = {
        'count': pagination.page.paginator.count,
        'next': pagination.get_next_link(),
        'previous': pagination.get_previous_link(),
        'results': serializer.data,
    }
    return JSONResponse(data)


@api_view(['GET'])
@permission_classes((AllowAny, ))
def search_tsv(request, query):
    query_request = QueryDict('q={}'.format(query))
    form = ApiForm(query_request)
    all_items = form.search()

    # sort queryset
    all_items = do_sorting(request, all_items)
    # paginate queryset
    paginator, page = do_pagination(request, all_items)

    return data_as_csv(request, paginator)


@csrf_exempt
@api_view(['POST'])
@authentication_classes((BasicAuthentication,))
@permission_classes((IsAdminUser,))
def mef_captcha(request):
    """Accepts a CAPTCHA image from MEF and returns the text

    Usage:

    import requests
    from requests.auth import HTTPBasicAuth

    fin = open("images/image_10.jpg", "rb")
    files = {'file': fin}
    url = "https://manolo.rocks/api/mef_captcha/"

    auth = HTTPBasicAuth("user", "pass")
    res = requests.post(url, files=files, auth=auth)
    print(res.text)
    """
    if "file" in request.FILES:
        myfile = request.FILES["file"]
        text = ocr_image(myfile.read())
        return HttpResponse(text)
    return "hi there"


def ocr_image(file_content):
    filename = "/tmp/" + str(uuid4()) + ".jpg"

    with open(filename, "wb") as handle:
        handle.write(file_content)

    basename = filename.replace(".jpg", "").replace("/tmp/", "")

    # process
    black_white_image_filename = "/tmp/{}-1.jpg".format(basename)
    cmd = "convert {} -threshold 90% {}".format(filename, black_white_image_filename)
    subprocess.call(cmd, shell=True)

    cmd = "tesseract -psm 7 -c tessedit_char_whitelist=ABCDEFGHIJKLMNPQRSTUVWXYabcdefghijkmnpqrstuvwxy23456789 {} {}".format(
        black_white_image_filename, basename)
    subprocess.call(cmd, shell=True)
    with open("{}.txt".format(basename), "r") as handle:
        text = handle.read().strip().replace(" ", "")
    os.remove("{}.txt".format(basename))
    return text
