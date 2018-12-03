
from celery_tasks.main import celery_app


@celery_app.task
def generate_static_detail_html(article_id):
    pass