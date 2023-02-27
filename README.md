# DRF_Image_API

# Goals of this project:

Using Django REST Framework, write an API that allows any user to upload an image in PNG or JPG format.
# added 'custom_renderers.py' so DRF could handle '.jpg' and '.png' files, also 'ImageSerializer' in 'serializers.py'

You are allowed to use any libraries or base projects / cookie cutters you want (but using DRF is a hard requirement).
# used Pillow (to handle images) and DRF 

Skip the registration part, assume users are created via the admin panel. 

Requirements:
it should be possible to easily run the project. docker-compose is a plus
# to be implemented in a future

users should be able to upload images via HTTP request

users should be able to list their images
#done, but not by DRF UI, DRF UI to be implemented in a future

there are three bultin account tiers: Basic, Premium and Enterprise:
#added 'permissions.py' file with 'Basic', 'Premium', 'Enterprise', and 'Admin' permission classes, not implemented yet - focused on other aspects of the project.

  users that have "Basic" plan after uploading an image get: 
    a link to a thumbnail that's 200px in height
  users that have "Premium" plan get:
    a link to a thumbnail that's 200px in height
    a link to a thumbnail that's 400px in height
    a link to the originally uploaded image
  users that have "Enterprise" plan get
    a link to a thumbnail that's 200px in height
    a link to a thumbnail that's 400px in height
    a link to the originally uploaded image
  ability to fetch a link to the (binary) image that expires after a number of seconds (user can specify any number between 300 and 30000)

apart from the builtin tiers, admins should be able to create arbitrary tiers with the following things configurable:
  arbitrary thumbnail sizes
  presence of the link to the originally uploaded file
  ability to generate expiring links
  admin UI should be done via django-admin
  there should be no custom user UI (just browsable API from Django Rest Framework)

remember about:
  tests
  validation
  performance considerations (assume there can be a lot of images and the API is frequently accessed)
#to be implemented in future!
  
 
