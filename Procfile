web: gunicorn prj_ga_chartjs.wsgi --log-file=gunicorn.log - 
celery -A prj_ga_chartjs worker -l info --logfile=celery.worker.log
celery -A prj_ga_chartjs beat -l info --logfile=celery.beat.log
