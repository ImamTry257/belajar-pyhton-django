1. pyhton3 -m venv Env -> membuat virtual enviroment
    atau -> virtualenv env --no-site-packages
2. pip install --upgrade pip
3. pip install Django==3.2
4. source Env/bin/activate -> masuk ke virtual enviroment
5. deactivate -> keluar dari virtual enviroment
6. django-admin startproject namaproject -> create project django
7. python3 manage.py runserver -> aktifkan serve django framework
8. python3 manage.py startapp namaApp nya -> buat app

# for migrate db
python3 manage.py migrate
pyhton3 manage.py createsuperuser
-> url admin backoffice

install xampp
sudo apt-get install libmysqlclient-dev

install module mysql at django
pip install pymysql
add :
import pymysql

pymysql.install_as_MySQLdb()

# how ro run local xampp using terminal
cd /opt/lampp/bin
./mysql -u root

check status -> status
copy UNIX socket ke setting your project -> change localhost to /opt/lampp/var/mysql/mysql.sock


# how to migrate models to db
1. create model and fixing field
2. python3 manage.py makemigrations
3. pyhton3 manage.py migrate


# how to check data in DB
1. login to db using shell python -> pyhton3 manage.py shell
2. import your models -> from todo.models import Todo , Todo is your modelname
3. Todo.objects.all() -> getting all data


# how to register model to admin sistem
1. at models.py -> import your models -> from .models import Post
2. then -> admin.site.register(yourclassname) -> admin.site.register(Post) 
3. then -> access your website
