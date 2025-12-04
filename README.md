## Form Challenge for Worky

This project automates the filling out of the contact form at:

https://hangers-crisbusa.web.app/

Using:
- Python
- Selenium WebDriver
- Pytest
- Allure Reports

#### Installation
pip install -r requirements.txt

#### Run tests
pytest --alluredir=report/

#### Generate Allure report
allure serve report/

### View Allure report

1. Unzip allure-results.zip
2. Open a terminal in the unzipped folder
3. Run --> allure serve allure-results