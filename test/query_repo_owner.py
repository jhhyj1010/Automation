#!/usr/bin/env python3

import sys
import base64
import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import urllib3
urllib3.disable_warnings()

repo = sys.argv[1]
print(f">>>>>> The input repo is {repo}\n")
#engine = create_engine("mssql+pyodbc://onesource:1SCM27a9b7ad56ab7a72a0d7SQL@1scm-sql-server-pre-westus.database.windows.net:1433/inventory?driver=ODBC+Driver+17+for+SQL+Server&encrypt=yes&TrustServerCertificate=yes&MARS_Connection=Yes", pool_timeout=3000, pool_pre_ping=True, pool_size=20000, max_overflow=30000)
engine = create_engine("mssql+pyodbc://onesource:1SCM27a9b7ad56ab7a72a0d7SQL@1scm-sql-server-group-prod.database.windows.net:1433/inventory?driver=ODBC+Driver+17+for+SQL+Server&encrypt=yes&TrustServerCertificate=yes&MARS_Connection=Yes", pool_timeout=3000, pool_pre_ping=True, pool_size=20000, max_overflow=30000)
Session = sessionmaker(engine)
session=Session()
INVENTORY_MODELS_URL = 'https://1source.intel.com/api/inventory/models'
request = requests.get(INVENTORY_MODELS_URL, verify=False)
models = base64.decodebytes(request.json()['data'].encode('utf8')).decode('utf8')
exec(models)
ret = session.query(Repo).filter_by(name=repo).one_or_none()
owners_list = []
if hasattr(ret, 'id'):
    r1 = session.query(RepoOwner).filter_by(repo_id=ret.id).all()
    for i in r1:
        owners_list.append(i.email)

print(f"\nowners for repo {repo} are:\n{owners_list}\n")
