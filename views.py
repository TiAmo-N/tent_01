from django.http import HttpResponse


def index(request):
    """
    ������ҳ
    :param request:
    :return:
    """
    return HttpResponse("index")