import pytest
from libs.api_client import ApiClient
from libs.db_client import MysqlClient

@pytest.fixture(scope='session')
def client():
    """初始化接口客户端"""
    return ApiClient()

@pytest.fixture(scope='session')
def login_token(client):
    """模拟登录，返回token"""
    payload = {"username": "user1", "password": "123456"}
    res = client.post("/post", data=payload)
    token = res.json().get("json", {}).get("username")
    return token

@pytest.fixture(scope='session')
def db_client():
    client = MysqlClient(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="123456",
        database="testdb"
    )
    return client

