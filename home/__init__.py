# home/__init__.py
from learncelery.celery import app as celery_app


__all__ = ('celery_app',)
