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
hit url: 
```

#### Install dummy database
```bash
python manage.py makemigrations
python manage.py migrate

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
- [Django Docs](https://docs.djangoproject.com/en/4.1/intro/tutorial01/)
