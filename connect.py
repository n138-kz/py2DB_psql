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
    try:
        conn = psycopg2.connect('{}://{}:{}@{}:{}/{}'.format(
            config['internal']['databases'][0]['schema'],
            config['internal']['databases'][0]['user'],
            config['internal']['databases'][0]['password'],
            config['internal']['databases'][0]['host'],
            config['internal']['databases'][0]['port'],
            config['internal']['databases'][0]['database'],
        ))

        cur = conn.cursor()
    
        cur.execute('SELECT now(), EXTRACT(epoch FROM CURRENT_TIMESTAMP), trunc(EXTRACT(epoch FROM CURRENT_TIMESTAMP)), to_timestamp(trunc(EXTRACT(epoch FROM CURRENT_TIMESTAMP)));')
        print(cur.fetchall())
    except (psycopg2.ProgrammingError):
        print(traceback.format_exc())
    except (psycopg2.errors.InsufficientPrivilege):
        print(traceback.format_exc())
    
    conn.commit()
    
    cur.close()
    conn.close()

