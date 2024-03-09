import redis
from django.conf import settings


def get_redis_connection() -> redis.StrictRedis:
	"""
    Получает и возвращает подключение к серверу Redis, используя настройки из Django settings.
    :return: Объект подключения к Redis.
    """
	return redis.StrictRedis(
		host=settings.REDIS_HOST,
		port=settings.REDIS_PORT,
		db=settings.REDIS_DB
	)



