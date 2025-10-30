@echo off
echo Running pytest + allure demo...
pytest --clean-alluredir --alluredir=./result
allure serve ./result
pause