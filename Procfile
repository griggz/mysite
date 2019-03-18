release: python manage.py migrate
web: gunicorn config.wsgi:application
log.Fatal(http.ListenAndServe(":" + os.Getenv("PORT"), router))
