import typing, json
from apistar import Include, Route
from apistar.frameworks.wsgi import WSGIApp as App
from apistar.handlers import docs_urls, static_urls
from apistar import typesystem
from youtube_client import Client

# dummy youtube data api response
f = open('dummy_response.json', 'r')
dummy_response = json.load(f)

class Query(typesystem.String):
    min_length = 1
    max_length = 250

class Order(typesystem.Enum):
    enum = ['date', 'rating', 'relevance', 'title', 'videoCount', 'viewCount']

def welcome(name=None):
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}

def search_video(query: Query, order_by: Order):
    if query is None:
        return 'query is empty!'
    else:
        # videos = Client().search(query, order_by)

        # return videos
        return dummy_response

routes = [
    Route('/', 'GET', welcome),
    Route('/search', 'GET', search_video),
    Include('/docs', docs_urls),
    Include('/static', static_urls)
]

app = App(routes=routes)


if __name__ == '__main__':
    app.main()
