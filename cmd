python manage.py shell

> User.generate_fake(100)
> Post.generate_fake(100)


初始化python manage.py db init
数据迁移，自动生成迁移代码python manage.py db migrate
更新数据库python manage.py db upgrade


python manage.py runserver