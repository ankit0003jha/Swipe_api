# Swipe_api
 Django restfull api which helps user to signup with the help of otp.

## How to run this application on your system.

1) First clone this project.
2) Make a virtual enviroment on your system.
3) Take requirements.txt file which i provided in the uppermost dir in this respository.
4) Then run: pip install -r requirements.txt in your shell.
5) Go to setting.py file and change the database information key. ( You can use default database or start with mysql/postgresql)
6) Go to terminal and run python manage.py make migrations and python manage.py migrate.
7) Go to manage.py file dir and run python manage.py runserver.
8) Want to access django admin panel createsuper and login into it.


## POSTMAN APi collection

1) http://127.0.0.1:8000/Register/<phone>/
2) http://127.0.0.1:8000/Login/<phone>/
3) http://127.0.0.1:8000/like/<int:id>
4) http://127.0.0.1:8000/dislike/<int:id>
5) http://127.0.0.1:8000/History
6) http://127.0.0.1:8000/liked-me
7) http://127.0.0.1:8000/whom-i-liked 
