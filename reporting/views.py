from django.shortcuts import render

# Create your views here.

from django.conf import settings


def index(request):
    data = settings.DATABASES

    res = {}

    for conn_name, conn_data in data.items():
        tmp = {}
        for param_name, param_val in conn_data.items():
            if param_name in ('NAME', 'USER', 'PASSWORD', "HOST", 'PORT'):
                tmp[param_name] = param_val
        res[conn_name] = tmp

    data = res

    return render(request, 'reporting/index.html', {'data': data})
