#!/usr/bin/env python3.8

from cryptography.fernet import Fernet
from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient, KeyVaultSecret
from azure.keyvault.keys import KeyClient
from azure.identity import DefaultAzureCredential
#import pdb;pdb.set_trace()


tenant_id='46c98d88-e344-4ed4-8496-4ed7712e255d'
client_id='d53efd2f-3d51-4b59-b3b7-2169941a43d6'
client_secret='o1ebuaO:DImdrZhkUa[]QCQq_Fs5bp01'
url='https://scm-invkv-prodwestus.vault.azure.net'
credential = ClientSecretCredential(tenant_id=tenant_id, client_id=client_id, client_secret=client_secret)
key_cred = DefaultAzureCredential()
kv_client = SecretClient(vault_url=url, credential=credential)
key_client = KeyClient(vault_url=url, credential=credential)

for key in key_client.list_properties_of_keys():
    print(key.name)

