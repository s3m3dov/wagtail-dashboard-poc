web: gunicorn prj_ga_chartjs.wsgi --log-file=gunicorn.log - 
worker: celery -A prj_ga_chartjs worker -l info --logfile=celery.worker.log
beat: celery -A prj_ga_chartjs beat -l info --logfile=celery.beat.log
