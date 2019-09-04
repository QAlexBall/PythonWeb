```shell
cd /app/static
git clone https://github.com/pandao/editor.md.git

export FLASK_ENV=development 
flask run

celery -A app.celery_worker worker -l info
```
