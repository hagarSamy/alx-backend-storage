#!/usr/bin/env python3
""" 
a Python function that changes
all topics of a school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    '''Update the topics of a school document where the name matches.

    :param mongo_collection: The MongoDB collection to update. pymongo 
    :param name: The name of the school document to update.
    :param topics: The list of topics to set in the document'''
    mongo_collection.update_one(
        {"name": name},
        { "$set": {"topics": topics}}
    )
