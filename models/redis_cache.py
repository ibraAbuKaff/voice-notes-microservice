import redis
from config import Config


class RedisCache:
    CACHE_SET_PREFIX = '_pilot_voice_notes'

    def __init__(self, identifier):
        self.redis_client = redis.StrictRedis(host=Config.get('REDIS_HOST'), port=Config.get('REDIS_PORT'),
                                              decode_responses=True)
        self.pool = RedisCache.get_set_name(identifier)

    def put(self, data):
        self.redis_client.sadd(self.pool, data)

    def get(self):
        return self.redis_client.smembers(self.pool)

    @staticmethod
    def get_set_name(identifier):
        return str(identifier) + RedisCache.CACHE_SET_PREFIX
