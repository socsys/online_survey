import os
import gunicorn

pythonpath = "/app"

bind = ["0.0.0.0:8002"]
workers = 3
timeout = 100000

proc_name = 'survey-service-gunicorn'
loglevel = 'info'
logfile = '/var/log/online_survey/gunicorn.log'
accesslog = '/var/log/online_survey/access.log'


asgi_application = "online_survey.asgi.application"

gunicorn.SERVER_SOFTWARE = 'online_survey_server'

STR_TO_BOOL = {
    'True': True,
    'False': False
}

DEBUG = STR_TO_BOOL.get(os.getenv('DEBUG'), False)
