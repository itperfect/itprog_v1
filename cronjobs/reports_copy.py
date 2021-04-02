import os
import sys
from pathlib import Path
import configparser

from itproger.settings import DATABASES
from pymysql import connect, cursors

if __name__ == '__main__':
    BASE_DIR = Path(__file__).resolve().parent

    tables = {'IN': 'reporting_grandprofitabilityreport', 'OUT': 'reporting_grandprofitabilityreport'}

    for conn, conn_data in DATABASES.items():
        result = None
        if conn_data["ENGINE"] == 'django.db.backends.mysql':
            print(f'{conn} ; {conn_data}')
            try:
                connection_live = connect(host=conn_data["HOST"], user=conn_data["USER"], database=conn_data['NAME'],
                                          password=conn_data["PASSWORD"], port=int(conn_data["PORT"]),
                                          cursorclass=cursors.DictCursor)
            except Exception as e:
                print(f"EXCEPTION got: {e}")
            else:
                path_loc = str(BASE_DIR) + "/" + conn
                if os.path.isdir(path_loc):
                    print(f"Path {path_loc} exists;")
                else:
                    os.makedirs(path_loc)

                with connection_live.cursor() as cursor:
                    cursor.execute(f"SELECT MIN(id) as 'min_val', MAX(id) as 'max_val' from {tables['IN']}")
                    result = cursor.fetchone()
                    print(result)
                    print()

                    if os.path.isfile(path_loc + "/values.cnf") is False:

                        if result['min_val'] is None:
                            result['min_val'] = 0
                        if result['max_val'] is None:
                            result['max_val'] = 0


                        os.mknod(f'{path_loc}/values.cnf')
                        config = configparser.ConfigParser()
                        config['SETTINGS'] = {}
                        config.set('SETTINGS', 'SRC_MIN_VAL', str(result["min_val"]))
                        config.set('SETTINGS', 'SRC_MAX_VAL', str(result["max_val"]))
                        config.set('SETTINGS', 'DST_MIN_VAL', str(0))
                        config.set('SETTINGS', 'DST_MAX_VAL', str(0))
                        with open(path_loc + "/values.cnf", "w") as conf_file:
                            config.write(conf_file)

                    # config = configparser.ConfigParser()
                    # config.read(path_loc + "/values.cnf")







