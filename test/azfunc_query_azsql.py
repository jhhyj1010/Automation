#!/usr/bin/env python3

import sys
import base64
import requests
from sqlalchemy import func
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
import pdb;pdb.set_trace()
ret = session.query(Repo).filter_by(name=repo).one_or_none()
#user = session.query(User).filter_by(email='sophia1.zhang@intel.com', enabled='True').one_or_none()
users = session.query(User).filter_by(email='chirag.singhal@intel.com').all()
uids = session.query(User.id).filter_by(email='chirag.singhal@intel.com').all()
### Get the latest result of a user
subquery = session.query(User.id).filter_by(email='chirag.singhal@intel.com').subquery()
latest_id = session.query(func.max(subquery.c.id)).scalar()
new_user = session.query(User).filter_by(id=session.query(func.max(subquery.c.id)).scalar()).one_or_none()
print(new_user.id, new_user.name, new_user.email)
group_query = session.query(User).filter_by(id=session.query(func.max(session.query(User.id).filter_by(email='chirag.singhal@intel.com').subquery().c.id)).scalar()).one_or_none()
###################################
print(users)
print(ret)
print('Jesson', group_query)
#engine = create_engine("mssql+pyodbc://sa:Intel123456@10.114.120.137:1433/inventory?driver=ODBC+Driver+17+for+SQL+Server&encrypt=yes&TrustServerCertificate=yes&MARS_Connection=Yes", pool_timeout=3000,  pool_pre_ping=True, pool_size=20000, max_overflow=30000)
conn = engine.connect()
conn.execute("update dbo.repo set iapm_id='1010101010' where name='applications.services.1source.inventory-data-sync-service'")
cursor = conn.execute("select iapm_id from dbo.repo where name='applications.services.1source.inventory-data-sync-service'")
row = cursor.fetchall()
print(row)
conn.close()
'''
owners_list = []
if hasattr(ret, 'id'):
    r1 = session.query(RepoOwner).filter_by(repo_id=ret.id).all()
    for i in r1:
        owners_list.append(i.email)
'''
#print(f"\nowners for repo {repo} are:\n{owners_list}\n")

