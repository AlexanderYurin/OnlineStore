import redis
from django.conf import settings
from users.utils import get_session_key


class CacheMixin:
	ban_time = 10

	@staticmethod
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

	@staticmethod
	def get_cache_key(request):
		# Получение уникального ключа для кеширования
		return get_session_key(request)

	def get_cache(self, request):
		# Получение объекта кеша
		cache_key = self.get_cache_key(request)
		return self.get_redis_connection().get(cache_key)

	def set_cache(self, request, value, timeout=None):
		# Установка значения в кеш
		cache_key = self.get_cache_key(request)
		self.get_redis_connection().set(cache_key, value, ex=timeout)

	def get_cache_timeout(self, request):
		# Получение времени жизни кеша
		cache_key = self.get_cache_key(request)
		return self.get_redis_connection().ttl(cache_key)
