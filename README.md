## Project Name : Cosy Craft Club

* [**Project Brief**](#Project-Brief)
My project is a forum for ammature artists to display their artwork, encourage one another and share craft tips.

# **TABLE OF Contents**

* [**User Experience** ](#User-experienceX)
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
To impliment the CRUD functionalities so that users can create, read, update and delete artwork.
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

Results:

Other errors:
I had not created custom models, so I had to change the fields in the models.py file after originally following the walkthrough model. To do this I first went back to my plan and re-read what fields I needed to create a custom model. The fields needed were title, image, description, author, created on and status. Now that I changed the model, I kept running into migration errors because the migration files had changed. Before attempting the migration again the terminal line pointed to typing errors in the code which I fixed.
After researching followed the steps on (webpage) to delete the previous migration files, and then run migrations again.  To do this I typed $ find . -path "*/migrations/*.py" -not -name "__init__.py" -delete into the terminal line. This deleted all the migration files except the init__.py file. After this I was able to run migrations again and it worked. 

Another issue that I ran into was displaying my images. 
To try and resolve this I watched a tutorial video. I had to install pillow so that the imagaes could be stored somewhere. I also had to add a media root to the settings.py file. After doing both of these things it was still showing a 404 error.

# Deployment 

# Credits 

To add the media root:
https://medium.com/geekculture/uploading-and-managing-django-images-and-files-afcd26526864

To display images:
https://support.hostinger.com/en/articles/1583313-how-to-fix-images-not-being-displayed-on-a-website

https://www.youtube.com/watch?v=JQ5MR-09msw

To reset migrations:
https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html

To create the models fields:
https://docs.djangoproject.com/en/5.0/topics/db/models/

https://stackoverflow.com/questions/64543923/django-post-form-and-post-list-on-the-same-page


# Acknowleadements 

