#!/usr/bin/env python3
"""
a Cache class to store an instance of the Redis client as a private variable
named _redis (using redis.Redis())
a store method that takes a data argument and returns a string.
The method generates a random key (e.g. using uuid),
stores the input data in Redis using the random key and return the key.
"""

import redis
import uuid
from typing import Union, Any


class Cache:
    '''store an instance of the Redis client'''
    def __init__(self):
        self._redis = redis.Redis(host="localhost", port=6379, db=0)
        # resetting the db
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''generate a random key
        store the input data in Redis
        using the random key and return the key.'''
        rand_key = str(uuid.uuid4())
        self._redis.set(rand_key, data)
        return rand_key

    def get(self, key: str, fn: callable) -> Union[str, int]:
        '''get data converted back to the desired format using the
        optional Callable'''
        data = self._redis.get(key)
        if fn:
            try:
                converted_data = fn(data)
                return converted_data
            except:
                return data
        return data

    def get_str(self, data: Any) -> str:
        '''convert data to string'''
        try:
            return str(data)
        except:
            return data
            
    def get_int(self, data) -> int:
        '''convert data to integer'''
        try:
            return int(data)
        except:
            return data
