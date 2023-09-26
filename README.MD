#### Запустить приложение:

docker-compose up --build

 docker-compose exec web python manage.py migrate

    создает админа с кредами - login: admin, password: adminpassword

    так же создает экземпляры моделей City, Category, Advert
