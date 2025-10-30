import allure

@allure.feature("用户模块")
@allure.story("获取用户信息")
def test_userinfo(client, login_token):
    headers = {"Authorization": f"Bearer {login_token}"}
    res = client.get("/get", headers=headers)
    allure.attach(str(res.json()), "响应内容", allure.attachment_type.JSON)
    assert res.status_code == 200
    assert "headers" in res.json()