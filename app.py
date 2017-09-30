import typing, json
from apistar import Include, Route, annotate
from apistar.interfaces import Templates
from apistar.renderers import HTMLRenderer
from apistar.frameworks.wsgi import WSGIApp as App
from apistar.handlers import docs_urls, static_urls
from apistar import typesystem
from youtube_client import Client

# dummy youtube data api response
# f = open('dummy_response.json', 'r')
# dummy_response = json.load(f)

class Query(typesystem.String):
    min_length = 1
    max_length = 250

class Order(typesystem.Enum):
    enum = ['date', 'rating', 'relevance', 'title', 'videoCount', 'viewCount']

@annotate(renderers=[HTMLRenderer()])
def welcome(username: str, templates: Templates):
    index = templates.get_template('index.html')
    return index.render(username=username)

def search_video(query: Query, order_by: Order):
    if query is None:
        return {'message': 'query is empty!'}
    else:
        videos = Client().search(query, order_by)

        return videos
        # return dummy_response

routes = [
    Route('/', 'GET', welcome),
    Route('/search', 'GET', search_video),
    Include('/docs', docs_urls),
    Include('/static', static_urls)
]

settings = {
    'TEMPLATES': {
        'ROOT_DIR': 'templates',
        'PACKAGE_DIRS': ['apistar']
    },
    'STATICS': {
        'ROOT_DIR': 'static',       # Include the 'static/' directory.
        'PACKAGE_DIRS': ['apistar']  # Include the built-in apistar static files.
    }
}

app = App(routes=routes, settings=settings)


if __name__ == '__main__':
    app.main()
