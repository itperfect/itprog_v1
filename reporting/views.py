from django.shortcuts import render
import io
from base64 import b64decode
from pickle import loads
import pandas as pd

from django_pandas.io import read_frame

# Create your views here.

# from django.conf import settings
from django.db import connections, models
from .models import SitesOnServers, GrandProfitAbilityReport


def index(request):
    # data = settings.DATABASES
    res = {}
    cn = ''
    m_obj = connections.databases
    conn_dict = m_obj.keys()

    for conn_name in conn_dict:
        db_conn = connections[conn_name]
        try:
            c = db_conn.cursor()
            print(f'Connection to database {db_conn} is OK')
            c.execute('select count(*) from auth_permission')
            d = c.fetchone()
            print(d)
            cn = 'OK'
        except Exception as e:
            print(f'Connection to database {db_conn} is ERROR')
            cn = 'ERROR'
        finally:
            res[db_conn] = cn


    all_sites = list(SitesOnServers.objects.values().order_by('-id'))

    # all_reports = list(GrandProfitAbilityReport.objects.all())
    all_reports = []

    return render(request, 'reporting/index.html', {'data': res, 'models': conn_dict, 'sites': all_sites, 'reports': all_reports})


def grandprofit(request):

    data_item = {}
    result = []

    data_item_df = {}
    result_df = []

    reports = GrandProfitAbilityReport.objects.filter(id__range=[31253, 31268], type=1)
    for report in reports:
        data_item['id'] = report.id
        data_item['created'] = report.created
        data_item['created_for'] = report.created_for
        data_item['type'] = report.type
        data_item['from_server'] = report.from_server
        data_item['from_id'] = report.from_id
        data_item['data'] = report.data.to_html()

        result.append(data_item)

        # pd_dataframe_item = loads(b64decode(data_item['data'].encode()))
        #
        # data_item_df = read_frame(pd_dataframe_item)
        #
        # result_df.append(data_item_df)

        data_item = {}

    return render(request, 'reporting/reports1.html', {'data': result})

