## Project Name : Cosy Craft Club

* [**Project Brief**](#Project-Brief)
My project is a forum for ammature artists to display their artwork, encourage one another and share craft tips.

# **TABLE OF Contents**

* [**User Experience** ](#User-experience)
* [**User Stories**](#User-Stories)
* [**Wireframes** ](#Wireframes)
* [**Surface-plan**](#Surface-plan)
* [**Features** ](#Features)
* [**Frameworks and libraries**](#Framewores-and-Liberies)
* [ **Testing**](#Testing)
* [ **Deployment**](#Deployment)
* [**Credits** ](#Credits)
* [**Acknowledgements** ](#Acknowledgements)

# User-Experience 
Project Outcomes:

To build a full stack project using Django.
To impliment the CRUD functionalities so that users can create accounts, read descriptions, update and delete artwork posts or comments.
To create a custom model for uploading and commenting on artwork.

# User-Stories:
I want to see a gallery of images so that I can be inspired to paint. 
I want to be able to create an account so that I can upload my artwork to share with others.
As the administrator, I want to be able to log in and manage users and posts so that only artwork has been uploaded.

# Features 


# Structure-Plan:


# Design-and-Color-Scheme


# Future developments 


# Testing-and-Results 
Strategy:
Once my website is finished I will attempt to create an art account to test the Crud functionalities. I will also seen to my peers so that they can reveiw it and create accounts too. 
I will be testing things such as navigation of the webpage and the gallery views during production. 
The results of my testing is detailed below. 

Results:

Errors in production:
I had not created a custom model, so I had to change the fields in the modules.py file after originally following the walkthrough. To do this I first went back to my plan and re-read what fields I needed to create a custom model art forum rather than a blog. The fields needed were title, image, description, author, created on and status. Now that I changed the model, I kept running into migration errors because the migration files had changed. Before attempting the migration again the terminal line pointed to typing errors in the code which I fixed.
After researching followed the steps on (webpage) to delete the previous migration files, and then run migrations again.  To do this I typed $ find . -path "*/migrations/*.py" -not -name "__init__.py" -delete into the terminal line. This deleted all the migration files except the init__.py file. After this I was able to run migrations again and it worked. 

As well as the model fields I changed the url paths as the app names had changed. Whilst I was doing this my website ran into server errors. To attempt solving this bug I first checked that all my models, views and url codes were spelt correctly. I also retraced all my steps in changing the model fields, but everything seemed to be correct. After some time I asked for support from alumni. They realized that under the first url path I had wrote my app name ‘artwork’ rather than leaving the syntax blank. Once I removed this my code worked and my deployed website was displaying correctly again.

Another issue that I ran into was displaying my images on the gallery page. To try and resolve this I watched a tutorial video. I had to install pillow so that the imagaes could be stored somewhere. I also had to add a media root to the settings.py file. After doing both of these things it was still showing a 404 error. I left this for a while and moved froward with the project. The course materials showed that I needed a static folder for my images to go into. After following these steps to create a static folder and moving the image files into it my webpage then displayed the images. 

Another issue that I found was trying to create more template pages. I was struggling to get the pages to display and I realised that the problem was in the views.py file. To solve it I watched this video (https://www.youtube.com/watch?v=1jcjuV2StxQ), re wrote the file and it worked. 
Whilst doing this however, I ran into merge issues. To solve this I looked at the individual merge conflicts and chose which branch I needed to keep.

# Deployment 

# Credits 

To add the media root:
https://medium.com/geekculture/uploading-and-managing-django-images-and-files-afcd26526864

To display images:
https://support.hostinger.com/en/articles/1583313-how-to-fix-images-not-being-displayed-on-a-website

https://www.youtube.com/watch?v=JQ5MR-09msw

https://www.w3schools.com/django/django_add_image.php/django_add_image_global.php

Migrations:
https://docs.djangoproject.com/en/5.0/topics/migrations/

https://.com/tutorial/2016/07/26/how-to-reset-migrations.html

Navigation:
https://stackoverflow.com/questions/71692890/how-to-go-from-one-page-to-another-in-django#:~:text=You%20need%20to%20make%20changes,should%20be%20accessed%20with%20name.&text=From%20django%2Ddoc%2C%20you%20can,function%20in%20urls.py%20file.

To create the models fields:
https://docs.djangoproject.com/en/5.0/topics/db/models/

https://stackoverflow.com/questions/64543923/django-post-form-and-post-list-on-the-same-page

https://stackoverflow.com/questions/47362122/django-modulenotfounderror

Other:
https://www.youtube.com/watch?v=ygzGr51dbsY

Video to add other pages:
https://www.youtube.com/watch?v=1jcjuV2StxQ 

Other websites:

https://hub.packtpub.com/multiple-templates-django/ 

https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Home_page 

https://www.w3schools.com/django/django_add_image.php/django_add_image_global.php

https://medium.com/i18n-and-l10n-resources-for-developers/the-difference-between-and-trans-in-django-templates-e1605a710b6f

https://learndjango.com/tutorials/django-login-and-logout-tutorial 

https://docs.djangoproject.com/en/5.0/ref/urls/

https://stackoverflow.com/questions/39935578/invalid-block-tag-endblock-did-you-forget-to-register-or-load-this-tag 

https://stackoverflow.com/questions/35054230/custom-tag-not-loaded-in-template 

https://medium.com/@sowaibaarshad/connecting-css-files-with-html-in-django-5dfb1d7039#:~:text=You%20can%20create%20the%20static,a%20subfolder%20if%20you%20prefer.&text=Once%20you%20have%20your%20static,to%20the%20static%20folder%20itself.

for the login page:

https://github.com/Code-Institute-Solutions/blog/blob/main/11_authorisation/login.html 



# Acknowleadements 

