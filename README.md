# Peacefulmind.art

This e-commerce platform that was designed and built to scale an already existing business. This business is the selling of handmade craft jewelry 
which has been running on Instagram using DMs to complete the sell. The intention is to automate most of the processes and allow the store owner to reach a bigger number of clients
and allow them to make their payments securely and hassel free via Stripe's payment system. With this platform up and running, the store owner only needs to monitor the orders and
courier them itself. The platform requests the client to create an account in order to save their details and previous orders in order to make future purchases more efficient and easy for the client.
Besides the already crafted jewelry, the client has the option to make a custom order through the platform. The client just needs to fill a form and include their requirements
for a custom made craft jewel.

Besides the business itself, on this platform there's a sub-platform called "Community" that has the goal of helping other small business to exposes themselves and hopefully reach
out to a bigger number of clients. This idea came from the very essence of "sharing is caring" that rules the store owner's life.

A live demo of website can be found [here](https://peacefulmind-art.herokuapp.com/).

## UX

The main users of this platform are everyone with a desire to purchase a piece of jewelry which won't be found anywhere else, there's no more exlusive than this.

The navigation is very user friendly, starting with and index page that has all the links displayed and easy to see. On the top bar, on the right, there are the account, community and shopping bag icons and just bellow are the links that divide the entire stock into categories. This makes it easier for the client to search for exactly what it wants.

The footer allows the client to learn more about the store owner by reading a small biography and checking his intagram page. The custom order link is also in this area.

<img src="static/readme_screenshots/Index.jpg" alt="Index Screenshot">

### User Stories

- As an anonymous user, I want to be able to browse through the whole jewelry stock or browse over just one specific category.
- As an anonymous user, I want to be able to browse through the community in order to check what other business are being marketed.
- As an anonymous user, I want to be able to create my own account and become a registered client.
- As an anonymous user and a registered client, I want to know more about the owner of this store by reading about him and checking social media.
- As an anonymous user and a registered client, I want to be able to submit a custom jewel request. As an anonymous user I want to be able to make this request and possibily receive
a quote before having to commit to registering.
- As a registered client, I want to easily add a desired product to my shopping bag.
- As a registered client, I want to be able to delete a product from the shopping bag.
- As a registered client, I want to be able to save my personal details to use them on my next purchase. Besides this I want to be able to update these details.
- As a registered client, I want to be able to check my previous orders.
- As a registered client, I want to be able to submit a community card in order to share my own or someone else's business.
- As the store owner, I want to be able to manage my products by adding new products, editing or deleting existing ones.
- As the store owner, I want to be able to manage the community cards by deleting the ones I find not relevant.

### Strategy

The goal of this project is to give a chance of this small business to reach out to a bigger number of possible clients. In a world filled woth chain business where everything is the standard causing that everyone has the same clothes, promoting small and medium businesses should be a priority. Enterpreneurs that use their creativity to make the world an exciting
and diverse place should be praise and supported. 

### Scope

This platform was built with the goal of promoting this small and individual business.

### Wireframes

* Index

<img src="static/wireframes/index.jpg" alt="Index Wireframe">

* Products List

<img src="static/wireframes/products.jpg" alt="Products Wireframe">

* Product Details

<img src="static/wireframes/product_details.jpg" alt="Product Details Wireframe">

* Profile Page

<img src="static/wireframes/profile.jpg" alt="Profile Page Wireframe">

* Community Page

<img src="static/wireframes/community.png" alt="Community Page Wireframe">

* Shopping Bag Page

<img src="static/wireframes/bag.jpg" alt="Shopping Bag Wireframe">

### Surface

The palette of colors chosen was based on the craftsman's personality.

## DATA

### Databases

Sqlite3 was used during development. For deployment, data tables and data was migrated to a PostgreSQL database.

### Data models

#### Products app

##### Product Model

| **Field**   | **Type**       | **Notes**                   |
|:----------- |:-------------- |:----------------------------|
| category    | ForeignKey     | Category                    |
| sku         | CharField      | Jewel's internal code       |
| name        | CharField      | Jewel's name                |
| description | Textfield      | Jewel's description         |
| material    | CharField      | Materials used              |
| price       | DecimalField   | Jewel's Price               |
| image       | ImageField     | Jewel's image               |

##### Category Model

| **Field**     | **Type**       | **Notes**                   |
|:------------- |:-------------- |:----------------------------|
| name          | CharField      | Category's name             |
| friendly_name | CharField      | Category's friendly name    |

#### Profile app

##### User Profile Model

| **Field**        | **Type**       | **Notes**                   |
|:---------------- |:-------------- |:----------------------------|
| user             | CharField      | User's nickname             |
| phone number     | CharField      | User's Phone Number                |
| street_address1  | CharField      | User's Address                     |
| street_address2  | CharField      | User's Address                     |
| town or city     | CharField      | User's Town or City                |
| postcode         | CharField      | User's Postcode                    |
| county           | ImageField     | User's County                      |
| country          | CountryField   | User's Country                     |

#### Checkout app

##### Order Model

| **Field**        | **Type**       | **Notes**              |
|:---------------- |:-------------- |:-----------------------|
| order_number     | CharField      | Order's Name           |
| user_profile     | ForeignKey     | User's Nickname        |
| full_name        | CharField      | User's Full Name       |
| email            | EmailField     | User's email address   |
| phone_number     | CharField      | User's Phone Number    |
| country          | CountryField   | User's Country         |
| postcode         | CharField      | User's Postcode        |
| street_address1  | CharField      | User's Address         |
| street_address2  | CharField      | User's Address         |
| county           | CharField      | User's County          |
| date             | DateTimeField  | Order's Date           |
| delivery_cost    | DecimalField   | Order's Delivery Cost  |
| order_total      | DecimalField   | Order's Product Cost   |
| grand_total      | DecimalField   | Order's Grande Total   |
| original_bag     | TextField      | Order's Original Bag   |
| stripe_pid       | CharField      | Stripe ID              |

#### Community app

##### Community Card Model

| **Field**        | **Type**      | **Notes**                             |
|:---------------- |:------------- |:--------------------------------------|
| card_number      | AutoField     | Card Number (See note below)          |
| name             | CharField     | Card Name                             |
| website          | URLField      | Business' Website                     |
| description      | TextField     | Small description about the business  |
| email            | CharField     | Business' email                       |
| date             | DateTimeField | Date card was created                 |

Note: This field was created to be used as an argument for the deletion view but then became useless when decided to use the element's ID for it.
The reason why it wasn't deleted was because it was creating some conflicts in the database so I just left this field in.

#### Custom Orders app

##### Custom Order Model

| **Field**        | **Type**      | **Notes**                                |
|:---------------- |:------------- |:-----------------------------------------|
| name             | CharField     | User's Name                              |
| email            | CharField     | User's email                             |
| street_address1  | CharField     | User's Address                           |
| street_address2  | CharField     | User's Address                           |
| town_or_city     | CharField     | User's County                            |
| postcode         | CharField     | User's Postcode                          |
| county           | CharField     | User's County                            |
| country          | CountryField  | User's Country                           |
| date             | DateTimeField | Custom Order's date                      |
| color            | CharField     | Jewel's color                            |
| material         | CharField     | Materials used                           |
| jewel_type       | CharField     | Jewel's Type                             |
| notes            | TextField     | Adittional notes about the custom order  |


### Schema

The database is divided into 3 main components:

- Products
- Community Cards
- Custom Orders

The Products components include 4 databases: User Profile, Products, Category and Order. These 4 databases are the backbone of this whole platform since it provides all the data necessary to display the jewels being sold and then assists with the checkout process and other related processes. In order to purchase anything the user needs to have a registered profile which is stored in User Profile Model. The Products and Category models are related to each other since every product is required to have a category. Community Cards and Custom Orders are separate models which are complementary to the platform. The Community Cards Model is where the business details are stored from the users that want to advertise it while the Custom Orders Model is where the user can submit a request for a custom made jewel for the owner then to see.

Bellow is the graphical representation of my database schema:<br>

<img src="static/schema.jpg" alt="Database Schema"><br>

## Existing Features

<ins>Feature 1<ins><br>
- As an anonymous user, I want to be able to browse through the whole jewelry stock or browse over just one specific category.

<img src="static/screenshots/feature1.jpg" alt="Navigation Bar"><br>

<ins>Feature 2<ins><br>
- As an anonymous user, I want to be able to browse through the community in order to check what other business are being marketed.

<img src="static/screenshots/feature2.jpg" alt="Community Cards"><br>

<ins>Feature 3<ins><br>
- As an anonymous user, I want to be able to create my own account and become a registered client.

<img src="static/screenshots/feature3.jpg" alt="Registration"><br>

<ins>Feature 4<ins><br>
- As an anonymous user and a registered client, I want to know more about the owner of this store by reading about him and checking social media.

<img src="static/screenshots/feature4.jpg" alt="About the owner links"><br>

<ins>Feature 5<ins><br>
- As an anonymous user and a registered client, I want to be able to submit a custom jewel request. As an anonymous user I want to be able to make this request and possibily receive
a quote before having to commit to registering.

<img src="static/screenshots/feature5.jpg" alt="Custom Order link"><br>
<img src="static/screenshots/feature5a.jpg" alt="Custom Order Form"><br>

<ins>Feature 6<ins><br>
- As a registered client, I want to easily add a desired product to my shopping bag.

<img src="static/screenshots/feature 6.jpg" alt="Add to bag button"><br>

<ins>Feature 7<ins><br>
- As a registered client, I want to be able to delete a product from the shopping bag.

<img src="static/screenshots/feature7.jpg" alt="Delete from bag button"><br>

<ins>Feature 8<ins><br>
- As a registered client, I want to be able to save my personal details to use them on my next purchase. Besides this I want to be able to update these details.

<img src="static/screenshots/feature8.jpg" alt="Profile Data"><br>

<ins>Feature 9<ins><br>
- As a registered client, I want to be able to check my previous orders.

<img src="static/screenshots/feature9.jpg" alt="Order History"><br>

<ins>Feature 10<ins><br>
- As a registered client, I want to be able to submit a community card in order to share my own or someone else's business.

<img src="static/screenshots/feature10.jpg" alt="Create a Card Link"><br>
<img src="static/screenshots/feature10a.jpg" alt="Create a Card Form"><br>

<ins>Feature 11<ins><br>
- As the store owner, I want to be able to manage my products by adding new products, editing or deleting existing ones.

<img src="static/screenshots/feature11.jpg" alt="Manage Products Link"><br>
<img src="static/screenshots/feature11a.jpg" alt="Create New Product Form"><br>

<ins>Feature 12<ins><br>
- As the store owner, I want to be able to manage the community cards by deleting the ones I find not relevant.

<img src="static/screenshots/feature12.jpg" alt="Delete Community Card Button"><br>

### Features Left to Implement

The payment flow is still in test so no actual payment is submitted, for this platform to go live this must go live too.
Login with social media is also a feature that would help the platform to get more users to register.

### Known Bugs

Below is a list of bugs/things that are not working correctly that were detected. These weren't corrected due to lack of time from the developer's side so they are flagged here.

The Sort dropdown in the product pages is not working. The option are correctly displayed in the dropdown but does nothing when one of them is selected.\
The purchases are being recorded in duplicate, this can be seen when checking a registered user's profile.

# Technologies Used

- Programming Languages
    - HTML
    - CSS
    - JavaScript
    - Python
- [Django](https://www.djangoproject.com/)
- [Google Fonts](https://fonts.google.com/)
    - Amatic font style was used
- [Font Awesome](https://fontawesome.com/)
- [Stripe](https://stripe.com/en-nl)
- [sqlite3](https://www.sqlite.org/index.html)
- [Postgres](https://www.postgresql.org/)
- [Heroku](https://www.heroku.com)

# Testing

All the tests done to this website can be found in [testing.md](testing.md).

## Heroku

1.  The first thing was to create a requirements.txt and a Procfile as below:

```
pip3 freeze --local > requirements.txt
echo web: python app.py > Procfile
```

2.  Once these files were sucessfuly created I navigated to Heroku and logged into my account.
    On the top right side of the screen click on "New" and created a new app.
  
<img src="static/screenshots/heroku/second_step.JPG" alt="Heroku Deployment - Creating a new app">  

3.  Then I had to chose a name for my app, I decided on "peacefulmind-art".
  
<img src="static/screenshots/heroku/third_step.JPG" alt="Heroku Deployment - Naming the app"> 

4.  After creating the app in Heroku installed and imported dj_database_url into the project's settings file and then add the POSTGRES database connection as the default database when in production mode alongside the sqlite database when in development. At this point psycopg2 was also installed. Once these were installed I ran pip3 freeze in order to update requirements.txt

<img src="static/screenshots/heroku/forth_step.jpg" alt="Database Setup"> 

5.  ACreayed a new superuser by running:

```
python3 manage.py createsuperuser
```

For review purposes here's the credential of this superuser

```
username: superuser
password: superuser
```

6.  With the superuser created installed gunicorn before creating a Procfile.

```
pip3 install gunicorn
```

7.  Temporarily disabled COLLECTSTATIC in the Heroku CLI by setting it to -1.

8.  Set up the ALLOWED_HOTS in setting.py in order to allow Heroku's hostname.

9. Set up config variable SECRET_KEY.

10. Set up automatic deployments in Heroku by connecting to the Lionize github repo.

<img src="static/screenshots/heroku/tenth_step.jpg" alt="Setup automatic deployments"> 

11. Enable automatic deploys by selecting the master branch.

<img src="static/screenshots/heroku/eleventh_step.jpg" alt="Enable automatic deployments"> 

## AWS

1.  Created my own AWS account.

2.  In the AWS Management Console searched for S3.

3.  In the S3 Management Console click on "Create bucket" to create a new bucket. Inserted the bucket's name "peacefulmind-art" and selected the closeste region for me. Gave public access, as below:

<img src="static/screenshots/aws/create_bucket_aws.jpg" alt="Create Bucket Screenshot"> 

4.  Once the new bucket was created, navigated to the properties tab of the bucket and scrolled down to "Static website hosting", click "Edit", and then selected "Enable" under the "Static website hosting" option. My default values for "Index document" and "Error document - optional" were index.html and error.html, as below:

<img src="static/screenshots/aws/properties.jpg" alt="Properties Navbar"> 
<img src="static/screenshots/aws/static_hosting.jpg" alt="Static Website Hosting"> 
<img src="static/screenshots/aws/static_website_hosting.jpg" alt="Static Website Hosting"> 

5.  On the bucket's permissions tab, add a CORS configuration, as below:

<img src="static/screenshots/aws/permissions.jpg" alt="Permissions Navbar"> 
<img src="static/screenshots/aws/CORS.jpg" alt="CORS"> 

6.  On the bucket's policy tab, clicked on "policy generator" and created a new policy which will then be added to the bucket.

7.  After saving the bucket policy, scrolled to the "Access control list (ACL)" tab and checked the list of objects box under the "Everyone (public access)" header.

### AWS Identity and Access Management Configuration

1.  In the IAM dashboard under "Security, Identity, & Compliance" navigated to the "User Groups" tab and created a new group.


<img src="static/screenshots/aws/users_groups.jpg" alt="Create a new user group"> 

2.  Under the policies tab, clicked on the JSON tab and then clicked on "Import managed policy".

3.  Select the S3FullAccess policy and click import.

<img src="static/screenshots/aws/policies.jpg" alt="Import AmazonS3FullAccess policies"> 

4.  Edited the imported JSON code in order to allow full access to the app's bucket and its' associated files, using its bucket's arn.

5.  Filled in the name and policy's description before creating the policy.

6.  Back in the "User groups" page clicked on the "manage-peacefulmind-art" group. Navigated to "permissions" and clicked the dropdown menu "Add permission" and selected "Attach Policies". Then click to check the policy that was just created and then click to "Add permissions".

<img src="static/screenshots/aws/permissions_policies.jpg" alt="Permissions Policies"> 

7.  Created a user to add to the group with programmatic access, for this project I named it "ms4-peacefulmind-art-staticfiles-user".

<img src="static/screenshots/aws/add_user.jpg" alt="Add User"> 

8.  Downloaded the CSV file with the new user's access key and secret access key in order to add them to Django to authenticate this user.

9.  Installed boto3 & django-storages, froze them into requirements.txt and then added 'storages' to the installed apps list in settings.py

10. Added the following AWS config variables to the settings.py file for use only if the USE_AWS var is found in os.environ:

```
AWS_STORAGE_BUCKET_NAME = 'peacefulmind-art'
AWS_S3_REGION_NAME = 'eu-central-1'
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_KEY')
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

# Static and media files
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATICFILES_LOCATION = 'static'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
MEDIAFILES_LOCATION = 'media'

# Override static and media URLs in productions
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```

11. Added the Access Keys as well as the USE_AWS=TRue to the Heroku config vars.

12. Committed these changes and pushed to github which then deployed it in Heroku due to because of automatic deployments, and the build collected all the Static files and placed them in the S3 bucket and Heroku served them successfully.

13. Created a new folder in the S3 bucket called Media and set permissions to grant public-read access as below:

<img src="static/screenshots/aws/acl.jpg" alt="Access Control List"> 

14. Last step was to just upload all the in-app images into that folder.

## Stripe

1.  Created a Stripe account and set it up in order to test payments.

2.  Added the STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY as config variables in Heroku.

3.  Created a new Production Webhook Endpoint in the Stripe Dashboard by clicking on the "Developers" and then "Webhooks" and finally "Add endpoint". Then added the application's heroku url + checkout/wh/ to "receive all events".

4.  Finally added the webhook's signing secret to the Heroku config variables.

## Emails

1.  In the application's associated Gmail account set up 2-step verification.

2.  Generated a new app password and added it to the application's config variables in Heroku alongside with a EMAIL_HOST_USER variable that stores the associated email.

3.  Then in settings.py use the following settings to connect the application to send emails via Gmail:

```
if "DEVELOPMENT" in os.environ:
    DEFAULT_FROM_EMAIL = 'peacefulmind-art@gmail.com'
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
    DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')
```



