import os

from django.conf import settings
from django.template import loader

from celery_tasks.main import celery_app
from main.models import Article


@celery_app.task
def generate_static_detail_html(article_id):
    article = Article.objects.get(id=article_id)
    title = article.en_title
    content = article.content
    category = article.category.name
    create_time = article.create_time
    view_counts = article.view_counts
    author = article.author.username
    html_content = {
        "content": content,
        "author": author,
        "title": title,
        "category": category,
        "create_time": create_time,
        "view_counts": view_counts
    }
    template = loader.get_template("deteil.html")
    html_text = template.render(html_content)
    file_path = os.path.join(settings.GENERATED_STATIC_HTML_FILES_DIR,
                             'article/' + str(category) + "/" + str(article.id) + ".html")
    with open(file_path, 'w') as f:
        f.write(html_text)

