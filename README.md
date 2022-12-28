# CodeBeLog
CodeBeLog webapplication for blogging.

#### Built with
- Python
- Django
- Html
- CSS

#### Setup & Run
```bash
.\venv\Scripts\activate
cd codebelog
python manage.py runserver

http://127.0.0.1:8000/

- run those command
[Create your own virtual env]


- activate virtual env

- install dependency
pip install -r requirements.txt
cd codebelog
python manage.py makemigrations
python manage.py migrate

- run server
python manage.py runserver

- hit url
http://127.0.0.1:8000/
```

#### Install dummy data
```bash
- create/export db backup
python manage.py dumpdata > db_backup.json


- import dummy data
python manage.py loaddata db_backup.json
```

#### Features Done
- Basic setup and core `Hello World!` app
- Blog post `CRUD` operations
- User core `signup login logout` using name, email, password & confirm password
- Post Created by user
- User Profile View
- Pagination
- Search articles by title or subtitle
- Blog view count
- Login signup page error and success messages flash
- Search by category 
- User dashboard 
- User Post CRUD
- Comment by user and 
- Comment approve by admin
- Like by user and show message if not logged in for comment and likes


#### Features
Articles, Pages, Categories, Tags(Add, Delete, Edit), etc.
Articles and pages support Markdown and highlighting.
Articles support full-text search.
Complete comment feature, include posting reply comment and email notification. Markdown supporting.
Sidebar feature: new articles, most readings, tags, etc.
OAuth Login supported, including Google, GitHub, Facebook, Weibo, QQ.
Memcache supported, with cache auto refresh.
Simple SEO Features, notify Google and Baidu when there was a new article or other things.
Simple picture bed feature integrated.
django-compressor integrated, auto-compressed css, js.
Website exception email notification. When there is an unhandle exception, system will send an email notification.
Wechat official account feature integrated. Now, you can use wechat official account to manage your VPS.

#### Resources
- [Core Template](https://github.com/sumitgirwal/CodeBeLog-Template)
- [Virutal Env Doc](https://virtualenv.pypa.io/en/latest/installation.html)
- [Django Docs](https://docs.djangoproject.com/en/4.1/intro/tutorial01/)
- [ManyToMany Field](https://stackoverflow.com/questions/28057512/django-form-with-many-to-many-relationship-does-not-save)

- [DB Backups](https://coderwall.com/p/mvsoyg/django-dumpdata-and-loaddata)
- [UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte](https://stackoverflow.com/questions/17843630/python-can-dumpdata-cannot-loaddata-back-unicodedecodeerror)
    Just install notepad++,open file, change encoding to UTF-8 save and run the loaddata commads
- [Django Fontawesome](https://fontawesome.com/docs/web/use-with/python-django)