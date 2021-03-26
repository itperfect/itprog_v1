from django.shortcuts import render

# Create your views here.

# from django.conf import settings
from django.db import connections


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

    return render(request, 'reporting/index.html', {'data': res, 'models': conn_dict})
