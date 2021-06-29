# Peacefulmind.art

This e-commerce platform was was designed and built in order to scale an already existing business. This business is the selling of handmade craft jewelry 
which has been running on Instagram using DMs to complete the sell. The intention is to automate most of the processes and allow the store owner to reach a bigger number of clients
and allow them to make their payments securely and hassle free via Stripe's payment system. With this platform up and running, the store owner only needs to monitor the orders and
post them itself. The platform requests the client to create an account in order to save their details and previous orders so make future purchases more efficient and easy for the client.
Besides the already crafted jewelry, the client has the option to make a custom order also through the platform. The client just needs to fill a form and include their requirements
for a custom made craft jewel.

Besides the business itself, on this platform there's a sub-platform called "Community" that has the goal of helping other small business to exposes themselves and hopefully reach
out to a bigger number of clients. This idea came from the very essence of "sharing is caring" that rules the store owner's life.

A live demo of website can be found [here](###########################).

## UX

THe main users of this platform is everyone who desires to purchase a piece of jewelry which won't be found anywhere else, there's no more exlusive than this.

The navigation is very user friendly, starting with and index page that has all the links displayed and easy to see. On the top bar, on the right, there are the account, community and shopping bag icons
abnd just bellow are the links that divide the entire stock into categories in order to make ir easier for the client to search for exactly what it wants.

The footer allows the client to learn more about the store owner by reading a small biography and checking his intagram page. The custom order link is also in this area.

<img src="static/readme_screenshots/Index.jpg" alt="Index Screenshot">

### User Stories

- As an anonymous user, I want to be able to browse through the whole jewelry stock or browse over just one specific category.
- As an anonymous user, I want to be able to search through the whole jewelry stock.
- As an anonymous user, I want to be able to browse through the community in order to check what other business are being marketed.
- As an anonymous user, I want to be able to create my own account and become a registered client.
- As an anonymous user and a registered client, I want to know more about the owner of this store by reading about him and checking social media.
- As an anonymous user and a registered client, I want to be able to submit a custom jewel request. As an anonymous user I want to be able to make this request and possibily receive
a quote before having to commit to registering.
- As a registered client, I want to easily add a desired product to my shopping bag.
- As a registered client, I want to be able to delete a product from the shopping bag.
- As a registered client, I want to be able to pay for my purchases in a easy way.
- As a registered client, I want to be able to save my personal details to use them on my next purchase. Besides this I want to be able to update these details.
- As a registered client, I want to be able to check my previous orders.
- As a registered client, I want to be able to submit a community card in order to share my own or someone else's business.
- As the store owner, I want to be able to manage my products by adding new products, editing or deleting existing ones.
- As the store owner, I want to be able to manage the community cards by deleting the ones I find not relevant.

### Strategy

The goal of this project is to give a chance of this small business to reach out to a bigger number of possible clients. In a world where chain business where everything is standard is the 
norm, causing that everyone has the same clothes everywhere, promoting small and medium businesses should be a priority. Enterpreneurs that use their creativity to make the world an exciting
and diverse place should be praise and supported. 

### Strategy

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


