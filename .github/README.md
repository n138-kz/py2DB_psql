# [py2DB_psql](https://github.com/n138-kz/py2DB_psql)

## Refs

- [![](https://www.google.com/s2/favicons?size=64&domain=https://github.com)py2DB_psql](https://github.com/n138-kz/py2DB_psql/)
- [![](https://www.google.com/s2/favicons?size=64&domain=https://qiita.com)Pythonから各種DBへ接続する方法](https://qiita.com/overflowfl/items/5abdf49322942276fb2c#2-3postgresql)
- [![](https://www.google.com/s2/favicons?size=64&domain=https://qiita.com)psycopg2 でよくやる操作まとめ](https://qiita.com/hoto17296/items/0ca1569d6fa54c7c4732#%E5%AE%9F%E8%A1%8C%E7%B5%90%E6%9E%9C%E3%82%92%E8%BE%9E%E6%9B%B8%E5%BD%A2%E5%BC%8F%E3%81%A7%E5%8F%96%E5%BE%97%E3%81%99%E3%82%8B)
- [![](https://www.google.com/s2/favicons?size=64&domain=https://github.com)isjp](https://github.com/n138-kz/isjp/)

## Sample

```sh
pip install -r requirements.txt
```

```python
>>> import psycopg2

# Connect to an existing database
>>> conn = psycopg2.connect("dbname=test user=postgres")

# Open a cursor to perform database operations
>>> cur = conn.cursor()

# Execute a command: this creates a new table
>>> cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

# Pass data to fill a query placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)
>>> cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",
...      (100, "abc'def"))

# Query the database and obtain data as Python objects
>>> cur.execute("SELECT * FROM test;")
>>> cur.fetchone()
(1, 100, "abc'def")

# Make the changes to the database persistent
>>> conn.commit()

# Close communication with the database
>>> cur.close()
>>> conn.close()

```

```python
import psycopg2
from psycopg2.extras import DictCursor

with psycopg2.connect('postgresql://{}:{}@{}:{}/{}'.format(
    'postgres',
    'postgres',
    'localhost',
    '5432',
    'postgres',
)) as conn:
    with conn.cursor(cursor_factory=DictCursor) as cur:
    cur.execute('SELECT count(uuid) as count from isjp where request like %s ', ('%.%',))
    print(json.dumps(cur.fetchall()))

```

## License

[Copyright (c) 2025 Yuu Komiya (n138), Under MIT License](LICENSE)  
