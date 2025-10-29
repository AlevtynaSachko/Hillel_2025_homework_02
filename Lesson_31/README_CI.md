# CI/CD з Jenkins для Cars API

## Попередні вимоги
- Встановлений Jenkins (локально).
- Плагіни: **Email Extension Plugin**, **Allure Jenkins Plugin** (JUnit є вбудованим).
- Налаштований SMTP у *Manage Jenkins → System* для надсилання листів.

## Налаштування job
1. Створіть **Multibranch Pipeline** або **Pipeline**.
2. Якщо Pipeline: у полі *Pipeline script from SCM* вкажіть свій Git-репозиторій (де лежить `Jenkinsfile`).
3. Збережіть — перший білд підтягне залежності, підніме локальний Flask API й проганятиме тести.
4. Після кожного пуша (вебхук) або з періодичністю `H/30 * * * *` пайплайн стартує, а результати надійдуть на пошту **InsertYour@Mail.Here**.

## Артефакти та звіти
- `pytest-junit.xml` — у вкладці *Test Result*.
- `allure-results/` — у вкладці *Allure Report*.
- `test_search.log` та `app.log` — архівуються до білда.

## Локальний запуск без Jenkins
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
nohup python cars_app.py &
pytest -q --maxfail=1 --alluredir=allure-results --junitxml=pytest-junit.xml
