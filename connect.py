import os
import json
import traceback

def config_default():
    config = {}
    config |= json.loads('''{
        "internal": {
            "databases": [
                {
                    "host": "localhost",
                    "port": "5432",
                    "schema": "postgresql",
                    "user": "postgres",
                    "password": "postgres",
                    "database": "postgres",
                    "tableprefix": ""
                }
            ]
        }
    }''')
    return config # Type: Dict

def config_load(config_file='.secret/config.json'):
    config = config_default()

    if(os.path.isfile(config_file)):
        with open(config_file,encoding='UTF-8') as f:
            config = config | json.load(f)
    else:
        print('No such file or directory: '+config_file)

    return config

if __name__ == '__main__':
    config = config_load()
    
    import psycopg2
    from psycopg2.extras import DictCursor
    with psycopg2.connect('{}://{}:{}@{}:{}/{}'.format(
        config['internal']['databases'][0]['schema'],
        config['internal']['databases'][0]['user'],
        config['internal']['databases'][0]['password'],
        config['internal']['databases'][0]['host'],
        config['internal']['databases'][0]['port'],
        config['internal']['databases'][0]['database'],
    )) as conn:
        with conn.cursor(cursor_factory=DictCursor) as cur:
            cur.execute('SELECT count(uuid) as count from isjp where request like %s ', ('%.%',))
            print(json.dumps(cur.fetchall()))
