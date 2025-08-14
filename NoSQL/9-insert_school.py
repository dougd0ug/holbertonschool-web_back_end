#!/usr/bin/env python3
"""
chnage all topics of a document
"""


def update_topics(mongo_collection, **kwargs):
    """
    change all topics
    """
    result = mongo_collection.insert_one(kwargs)
    insert_id = result.inserted_id
    return insert_id
