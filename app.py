from apistar import Include, Route
from apistar.frameworks.wsgi import WSGIApp as App
from apistar.handlers import docs_urls, static_urls
from apistar import typesystem


def welcome(name=None):
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}

class IntProp(typesystem.Integer):
    minimum = 1
    maximum = 5

class EnumProp(typesystem.Enum):
    enum = ['one', 'two', 'three']

class RetType(typesystem.Object):
    properties = {
        'strprop': typesystem.string(max_length=100),
        'intprop': IntProp,
        'enumprop': EnumProp,
    }

def api1(intprop: IntProp, enumprop: EnumProp) -> RetType:
    return RetType(strprop='abc', intprop=intprop, enumprop=enumprop)

routes = [
    Route('/', 'GET', welcome),
    Route('/api1', 'GET', api1),
    Include('/docs', docs_urls),
    Include('/static', static_urls)
]

app = App(routes=routes)


if __name__ == '__main__':
    app.main()
