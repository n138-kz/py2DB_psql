# [py2DB_psql](https://github.com/n138-kz/py2DB_psql)

## Refs

- [![](https://www.google.com/s2/favicons?size=64&domain=https://github.com)py2DB_psql](https://github.com/n138-kz/py2DB_psql/)
- [![](https://www.google.com/s2/favicons?size=64&domain=https://qiita.com)Pythonから各種DBへ接続する方法](https://qiita.com/overflowfl/items/5abdf49322942276fb2c#2-3postgresql)

## Sample

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

## License

[Copyright (c) 2025 Yuu Komiya (n138), Under MIT License](LICENSE)  
