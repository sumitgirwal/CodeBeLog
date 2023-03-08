# CodeBeLog
CodeBeLog web application for blogging.
A blog web application built with Django and Bootstrap can be a powerful tool for sharing ideas and information with the world. 
Here are some key features that you may have included in your project:

User authentication: Your blog web application likely allows users to sign up and log in to the application to create, edit, and publish their own blog posts. You may have used Django's built-in authentication system to handle user registration and login.

Blog post creation and editing: Your application may allow users to create new blog posts and edit existing ones. You may have used Django's form handling and database models to create and store blog post content.

Blog post display: Your application likely displays blog posts to users in a visually appealing and user-friendly way. You may have used Bootstrap's CSS and JavaScript to style and add interactivity to your blog post pages.

Search functionality: Your application may allow users to search for blog posts based on keywords or tags, making it easier for them to find content that interests them.

Admin dashboard: As the owner or administrator of the blog web application, you likely have access to a backend dashboard where you can manage blog posts, user accounts, and other aspects of the application.

Overall, a blog web application built with Django and Bootstrap can be a powerful tool for sharing ideas and engaging with a community of readers. With the right features and design, your blog can become a valuable resource for people looking for information on a wide range of topics.

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
###### Blog Post Management:
A key feature of the blog application will be the ability to create, read, update, and delete blog posts. This will involve creating a blog post model with fields such as title, content, author, and date created, as well as views to handle these operations.

###### User Authentication:
Users will need to be able to sign up, log in, and log out of the application. We will implement user authentication features using the user's name, email, password, and confirmation of the password.

###### Post Creation and User Profiles:
Users should be able to create and view posts they have created, as well as view their own profile and details of their posts.

###### Pagination and Search:
To improve user experience, we will add pagination to the home page, limiting the number of posts per page. Additionally, users should be able to search for articles by title, subtitle, category, or username.

###### Blog Post Analytics:
To provide valuable insights, we will implement a feature that tracks the number of views each blog post receives.

###### Login and Signup Messages:
We will add error and success messages to the login and signup pages to inform the user of the outcome of their actions.

###### User Dashboard and Stats:
Users will have access to a dashboard where they can view their activity stats, such as the number of posts they have created and their overall post views.

###### Comment and Like System:
Users should be able to comment on posts, and admins will approve them before they are published. Users should also be able to like posts, with a message displayed if they are not logged in.

###### User Profile Customization:
Users should be able to edit their username and upload a profile photo. We will integrate the TinyMCE editor to allow users to create visually rich blog posts.


#### Coming Soon
Articles, Pages, Categories, Tags(Add, Delete, Edit), etc. <br/>
Articles and pages support Markdown and highlighting. <br/>
Articles support full-text search. <br/>
Complete comment feature, include posting reply comment and email notification. Markdown supporting. <br/>
Sidebar feature: new articles, most readings, tags, etc. <br/>
OAuth Login supported, including Google, GitHub, Facebook, Weibo, QQ. <br/>
Memcache supported, with cache auto refresh. <br/>
Simple SEO Features, notify Google and Baidu when there was a new article or other things. <br/>
Simple picture bed feature integrated. <br/>
django-compressor integrated, auto-compressed css, js. <br/>
Website exception email notification. When there is an unhandle exception, system will send an email notification. <br/> 
Wechat official account feature integrated. Now, you can use wechat official account to manage your VPS. <br/>

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
