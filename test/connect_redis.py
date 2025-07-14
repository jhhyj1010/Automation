#!/usr/bin/env python

import redis

def connect_to_redis_cache(hostname, port, password):
    try:
        client = redis.Redis(
            host=hostname,
            port=port,
            username=user,
            password=password,
            ssl=False
        )
        # Test the connection
        client.ping()
        print("Connected to Redis")
        return client
    except Exception as e:
        print(f"Failed to connect to Redis: {e}")
        return None

# Usage
hostname = '10.139.152.5'
port = 10000  # Default port for SSL
user = 'default'
import pdb;pdb.set_trace()
redis_client = connect_to_redis_cache(hostname, port, password)


