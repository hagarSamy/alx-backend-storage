#!/usr/bin/env python3
""" a Python script that provides some stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    num_of_docs = nginx_collection.count_documents({})
    print(f'{num_of_docs} logs')
    print('Methods:')

    get_logs = nginx_collection.count_documents({"method": "GET"})
    print(f'\t method GET: {get_logs}')

    POST_logs = nginx_collection.count_documents({"method": "POST"})
    print(f'\t method POST: {POST_logs}')

    PUT_logs = nginx_collection.count_documents({"method": "PUT"})
    print(f'\t method PUT: {PUT_logs}')

    PATCH_logs = nginx_collection.count_documents({"method": "PATCH"})
    print(f'\t method PATCH: {PATCH_logs}')

    DELETE_logs = nginx_collection.count_documents({"method": "DELETE"})
    print(f'\t method DELETE: {DELETE_logs}')

    status_checks = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print(f'{status_checks} status check')
