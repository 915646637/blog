from celery import Celery

# 为celery使用django配置文件进行设置
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings.dev")

# 创建celery应用
celery_app = Celery('blog', broker='redis://127.0.0.1:6379/15')

# 导入celery配置
# app.config_from_object('celery_tasks.config')

# 自动注册celery任务
celery_app.autodiscover_tasks(
    ['celery_tasks.static_detail'])
