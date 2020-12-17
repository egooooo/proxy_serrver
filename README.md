## Installation
Create virtualenv and activate:
```bash
virtualenv venv_proxy --python=python3.8
```
```bash
source venv_proxy/bin/activate
```
Requirements
```bash
pip install -r requirements.txt
```

## Run backend
```bash
python manage.py run
```

## Browser
* http://127.0.0.1:8888/

## Tests
```bash
python -m unittest tests.test_modify_links
```
```bash
python -m unittest tests.test_modify_content
```
