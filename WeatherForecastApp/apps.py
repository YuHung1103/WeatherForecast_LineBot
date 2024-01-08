from django.apps import AppConfig
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger


class WeatherforecastappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'WeatherForecastApp'

    def ready(self):
        from .scheduler import send_reminder  # 注意這裡的相對引用路徑
