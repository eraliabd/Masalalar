# Django loyihani PostgreSql bazaga ulash va xavfsizlikni taminlash

  pip install environs  -  paket o'rnatiladi.
  pip install psycopg2  -  postgresql uchun o'rnatiladi.

  # settings.py fayl ichiga quyidagilarni qo'shamiz.
  import os
  import environs

  env = environs.Env()
  env.read_env()  # agar .env fayl mavjud bo'lsa uni o'qish uchun

  INSTALLED_APPS = [
    ...
    'environs',
    ...
  ]

  DATABASES = {
      'default': {
          'ENGINE': os.environ.get("ENGINE"),
          'NAME': os.environ.get("NAME"),
          'USER': os.environ.get("USER"),
          'PASSWORD': os.environ.get("PASSWORD"),
          'HOST': os.environ.get("HOST"),
          'PORT': os.environ.get("PORT"),
      }
  } # hohlasangiz bunda 'NAME': env("NAME"), sifatida ishlatsa ham bo'ladi.

  # Loyiha ichida .env nomli fayl ochiladi va ichiga quyidagilar yoziladi.  

  export ENGINE=django.db.backends.postgresql_psycopg2
  export NAME=database
  export USER=username
  export PASSWORD=password
  export HOST=127.0.0.1
  export PORT=5432
