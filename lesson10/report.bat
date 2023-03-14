echo Y| rmdir /s .\results
pytest --alluredir=.\results
move .\final-report\history .\results\
echo Y| rmdir /s .\final-report
allure generate results -o final-report && allure open final-report