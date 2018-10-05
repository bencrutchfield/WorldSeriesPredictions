import multiprocessing
worker_class = 'gthread'
workers = multiprocessing.cpu_count()
threads = 25
pidfile = 'gunicorn_pid.txt'