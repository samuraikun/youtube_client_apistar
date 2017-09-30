import json
import pytest_mock
from apistar.test import TestClient
from app import app, welcome


def test_welcome():
    """
    Testing a view directly.
    """
    data = welcome()
    assert data == {'message': 'Welcome to API Star!'}


def test_http_request():
    """
    Testing a view, using the test client.
    """
    client = TestClient(app)
    response = client.get('http://localhost/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Welcome to API Star!'}

def test_search():
    client = TestClient(app)
    # TODO レスポンスをモック化したい
    response = client.get('http://localhost/search?query=hoge&order_by=date')
    result = [
        {
            "kind": "youtube#searchResult",
            "etag": "dummy",
            "id": {
                "kind": "youtube#video",
                "videoId": "dummy"
            },
            "snippet": {
                "publishedAt": "2017-09-30T00:00:00.000Z",
                "channelId": "dummy",
                "title": "dummy response",
                "channelTitle": "dummy",
                "description": "This is dummy data",
                "liveBroadcastContent": "none",
                "thumbnails": {
                    "default": {
                        "height": 90,
                        "url": "https://dummy.jpg",
                        "width": 120
                    },
                    "high": {
                        "height": 360,
                        "url": "https://dummy.jpg",
                        "width": 480
                    },
                    "medium": {
                        "height": 180,
                        "url": "https://dummy.jpg",
                        "width": 320
                    }
                }
            }
        }
    ]

    assert response.status_code == 200
    assert response.json() == result

def test_search_without_query():
    client = TestClient(app)
    response = client.get('http://localhost/search')

    assert response.json() == {'message': 'query is empty!'}
