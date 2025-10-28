# ⚙️ Allure Configuration
Project includes Allure configuration file `allure.properties`:

allure.results.directory=allure-results
allure.report.directory=allure-report
allure.report.title=Cars API Tests Report


To generate and view report:
```bash
pytest --alluredir=allure-results
allure serve allure-results