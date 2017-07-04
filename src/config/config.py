from os import environ as env
from sys import argv
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

server = {
    'host': env.get('HOST') or 'localhost',
    'port': int(env.get('PORT')) if env.get('PORT') else 9080,
    'debug': bool(env.get('DEBUG')) if env.get('DEBUG') else False,
    'ssl': env.get('SSL') or None,
    'sock': env.get('SOCK') or None,
    'workers': int(env.get('WORKERS')) if env.get('WORKERS') else 1,
    'loop': env.get('LOOP') or None
}

db = {
    'host': env.get('DB_HOST'),
    'user': env.get('DB_USER'),
    'password': env.get('DB_PASSWORD'),
    'port': int(env.get('DB_PORT')),
    'database': env.get('DB_NAME')
}

if len(argv) == 5:
    server['host'] = argv[2]
    server['port'] = argv[4]
elif len(argv) > 3 < 4:
    server['host'] = argv[2] if argv[2] != '--port' else server['host']
    server['port'] = argv[3] if argv[3] != '--port' else server['port']
