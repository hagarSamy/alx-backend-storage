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
from typing import Union, Callable, Any
import functools


def count_calls(method: Callable) -> Callable:
    qualname = method.__qualname__

    @functools.wraps(method)  # This preserves the original method's metadata
    def wrapper(self, *args, **kwargs):
        self._redis.incr(qualname)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    '''a decorator to store the history of inputs
    and outputs for a particular function.'''
    qualname = method.__qualname__
    input_key = qualname + ":inputs"
    output_key = qualname + ":outputs"

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(output))
        return output
    return wrapper

def replay(self, method):
    '''display the history of calls of a particular function.'''
    qualname = method.__qualname__
    input_key = qualname + ":inputs"
    output_key = qualname + ":outputs"
    count = self.get(qualname).decode("utf-8")
    print(f"{qualname} was called {count} times:")

class Cache:
    '''store an instance of the Redis client'''
    def __init__(self):
        self._redis = redis.Redis()
        # resetting the db
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''generate a random key
        store the input data in Redis
        using the random key and return the key.'''
        rand_key = str(uuid.uuid4())
        self._redis.set(rand_key, data)
        return rand_key

    def get(self, key: str,
            fn: Callable = None) -> Union[str, bytes, int, float]:
        '''get data converted back to the desired format using the
        optional Callable'''
        data = self._redis.get(key)
        if fn:
            converted_data = fn(data)
            return converted_data
        return data

    def get_str(self, data: Any) -> str:
        '''convert data to string'''
        try:
            return str(data)
        except:
            return data

    def get_int(self, data: Any) -> int:
        '''convert data to integer'''
        try:
            return int(data)
        except:
            return data
