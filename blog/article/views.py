from flask import (
    Blueprint,
    render_template,
)
from werkzeug.exceptions import NotFound

article = Blueprint('article', __name__, url_prefix='/articles', static_folder='../static', )

ARTICLES = [
    {
        'id': 1,
        'title': 'some title #1',
        'text': 'some text',
        'author': {
            'name': 'Alice',
            'id': 1,
        },
    },
    {
        'id': 2,
        'title': 'some title #2',
        'text': 'some text',
        'author': {
            'name': 'Jon',
            'id': 2,
        },
    }
]


@article.route('/')
def article_list():
    return render_template(
        'articles/list.html',
        articles=ARTICLES,
    )


@article.route('/<pk>')
def get_article(pk):
    try:
        pk = eval(pk)
        article_title = pk.get('title')
        article_text = pk.get('text')
        article_author_name = pk.get('author').get('name')
        article_author_id = pk.get('author').get('id')
    except KeyError:
        raise NotFound(f'Article {article_title} not found')
    return render_template(
        'articles/details.html',
        #article_id=article_id,
        article_title=article_title,
        article_text=article_text,
        article_author_name=article_author_name,
        article_author_id=article_author_id,
    )
