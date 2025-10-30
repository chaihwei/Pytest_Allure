import pytest
import allure
from pathlib import Path
from utils.yaml_util import load_yaml, get_project_root

@allure.feature("登录模块")
@allure.story("登录接口测试")
@pytest.mark.parametrize("case", load_yaml(Path(get_project_root() / "data" / "login_data.yaml")))
def test_login(case, client):
    with allure.step(f"执行测试用例：{case['case_name']}"):
        res = client.post(case["url"], data=case["data"])
        allure.attach(str(res.json()), "响应内容", allure.attachment_type.JSON)
        assert res.status_code == case["expected_status"]
