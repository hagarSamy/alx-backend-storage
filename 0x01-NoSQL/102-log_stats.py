#!/usr/bin/env python3
""" a Python script that provides some stats about Nginx logs stored in MongoDB
adding the top 10 of the most present IPs in the collection nginx of the database logs
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    num_of_docs = nginx_collection.count_documents({})
    print(f'{num_of_docs} logs')
    print('Methods:')

    get_logs = nginx_collection.count_documents({"method": "GET"})
    print(f'\tmethod GET: {get_logs}')

    POST_logs = nginx_collection.count_documents({"method": "POST"})
    print(f'\tmethod POST: {POST_logs}')

    PUT_logs = nginx_collection.count_documents({"method": "PUT"})
    print(f'\tmethod PUT: {PUT_logs}')

    PATCH_logs = nginx_collection.count_documents({"method": "PATCH"})
    print(f'\tmethod PATCH: {PATCH_logs}')

    DELETE_logs = nginx_collection.count_documents({"method": "DELETE"})
    print(f'\tmethod DELETE: {DELETE_logs}')

    status_checks = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print(f'{status_checks} status check')

    aggr_collection = nginx_collection.aggregate([
        {"$group": {
            "_id": "$ip",
            "ip_count": {"$sum": 1}  # increment the counter by 1 for each ip occurance
        }},
        {"$sort": {"ip_count": -1}},  # Sort by ip_count in descending order
        {"$limit": 10}  # Limit to top 10 documents
    ])
    print("IPs:")
    for log in aggr_collection:
        print(f"\t{log['_id']}: {log['ip_count']}")
