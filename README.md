# CodeBeLog
CodeBeLog web application for blogging.

#### Built with
- Python 
- Django 
- Html
- CSS

![home page](https://user-images.githubusercontent.com/64283478/210176840-96be9f4f-494c-4fca-be54-ac05902fada3.png)


#### Installation & Setup
- Install virtual env
```bash
python -m pip install --user virtualenv
python -m venv venv
```
- Activate virtual env
```bash
.\venv\Scripts\activate
```
- Install packages
```bash
pip install -r requirements.txt
```

- Goto project folder
```bash
cd codebelog
```

- Database migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

- Run application
```bash
python manage.py runserver
```
- Hit url in browser 
```bash
http://127.0.0.1:8000/
```

#### Quick Cmd
```bash

.\venv\Scripts\activate
cd codebelog
python manage.py runserver

http://127.0.0.1:8000/

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

```

#### Install dummy data
```bash
- create/export db backup
python manage.py dumpdata > db_backup.json


- import dummy data
python manage.py loaddata db_backup.json
```

#### Features
Basic setup and core `Hello World!` app <br/>
Blog post `crud` operations <br/>
User core `signup login logout` using the name, email, password & confirm password <br/>
Post created by user User profile view <br/>
Post pagination on home page <br/>
Search articles by `title` or `subtitle` or `category` or by `username` <br/>
Blog post `view count` <br/>
Login signup page error and success messages flash <br/>
User dashboard and `view stats` <br/>
Comment by user and `comment` approved by admin <br/>
Like by the user and show a message if not logged in for comment and `likes` <br/>
User `name edit` and upload `profile photo` <br/>
Blog post editor using `TinyMCE` <br/>


#### Coming Soon
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
- [Django Fontawesome - Icon](https://fontawesome.com/docs/web/use-with/python-django)
- [Modal Popup](https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_modal)
- [TinyMCE](https://pypi.org/project/django-tinymce/)
