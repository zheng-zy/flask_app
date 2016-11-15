python manage.py shell

> User.generate_fake(100)
> Post.generate_fake(100)


初始化python manage.py db init
数据迁移，自动生成迁移代码python manage.py db migrate
更新数据库python manage.py db upgrade


python manage.py runserver


httpie测试命令
http --json --auth zhezhiyong@163.com:123 GET http://127.0.0.1:5000/api/v1.0/posts/
认证令牌
http --json --auth zhezhiyong@163.com:123 GET http://127.0.0.1:5000/api/v1.0/token