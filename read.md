# Bakery Management System

---
> Bakery Management System basically has been implemented by using Django 
> and Django Rest Framework. It contains some end points to provide the service of
> creating Bakery Items,Updating them, deleting them as per set permissions
> Postman has been used as a client to call designed API

# Features

---

### Bakery ADMIN has the capability to:

1. Add Ingredients to bakery like Milk, Eggs etc
2. Create BakeryItem from a list of ingredients like Cupcake, Cake, Muffin etc
3. Get the detail of BakeryItem (ingredients with quantity percentage, cost price, selling price etc)
4. Manage inventory

### CUSTOMER has the capability to:

1. Register and Login
2. Get a list of available products
3. Place an Order and get the bill
4. See order history

# Installation Guide

---


>   py -m venv myenv

>   myenv/script/activate

>   pip install -r requirement.txt

>   py manage.py runserver


# Authentication and Authorization

We have Designed this system to register a fresh user and create a Token for him/her.
If you do not have Token right now you can use login api call to get access of token.
Once you get Token you can move on to get access of data from back end. We have taken care the accurate permission are set while creation of Token in
system.

You can set that token in postman client using authorization as oauth2.0 and provide your token right there.


### Authentication

1. Registration

````
End point - http://localhost:8000/accounts/register/ 
POST 
request body

{
  "username":"user_two",
  "first_name": "Anshu",
  "last_name": "Mishra",
  "email": "anshoomish.in@gmail.com",
  "password":"Anshoo12@#",
  "address":{
    "street_address":"adrress_one",
    "city":"Kanpur",
    "phone":"900989900",
  } 
}

Response - 

{"message":"login successful.","token":"69d1d158818dae29e73f7f34fcd9e1fe052e6da6"}

````
2. Login
```
End Point - http://localhost:8000/accounts/login/ 
GET Request 
Body 

{
  "username":"user_two",
  "password":"Anshoo12@#"
}

Response - 

{
    "message": "login successful.",
    "token": "69d1d158818dae29e73f7f34fcd9e1fe052e6da6"
}

```
# Back End Api calls

---

1. Bakery Item Creation - Only Admin can do this

We are passing here bakery item with name*, profit,ingredients* Where ingredients contain 
cost price and number of unit required to build the bakery Item. So we have calculated
selling price and cost price of Bakery Item as per profit set and total cost of each ingredient.

````
End Point - http://localhost:8000/bakery/manage-bakery/
POST
Token

Req Body 

{
  "name": "CupCake",
  "profit": 15,
  "ingredients": [
    {
      
      "name": "eggs",
      "quantity": 2,
      "cost_price": 5
    },
    {
      
      "name": "bread",
      "quantity": 3,
      "cost_price": 5
    },
    {
      
      "name": "Milk",
      "quantity": 5,
      "cost_price": 15
    }
  ]
}

````
2. List of All Available Items Valid for Both Admin and Customer

```
End Point - http://localhost:8000/bakery/available-products/
GET 
TOKEN

Response 

[
    {
        "id": 9,
        "ingredients": [
            {
                "id": 9,
                "name": "eggs",
                "quantity": 2,
                "cost_price": 5.0
            },
            {
                "id": 10,
                "name": "bread",
                "quantity": 3,
                "cost_price": 5.0
            }
        ],
        "name": "Cake",
        "created_at": "2022-12-03T16:20:14.244880Z",
        "modified_at": "2022-12-03T16:20:14.221677Z",
        "expiry_date": "2023-12-03T16:20:14.221677Z",
        "selling_price": 26.25,
        "is_available": true,
        "discount": 0.0,
        "cost_price": 25.0,
        "profit": 5.0
    },
    {
        "id": 10,
        "ingredients": [
            {
                "id": 11,
                "name": "eggs",
                "quantity": 2,
                "cost_price": 5.0
            },
            {
                "id": 12,
                "name": "bread",
                "quantity": 3,
                "cost_price": 5.0
            },
            {
                "id": 13,
                "name": "Milk",
                "quantity": 5,
                "cost_price": 15.0
            }
        ],
        "name": "CupCake",
        "created_at": "2022-12-03T16:26:40.652895Z",
        "modified_at": "2022-12-03T16:26:40.595577Z",
        "expiry_date": "2023-12-03T16:26:40.595577Z",
        "selling_price": 115.0,
        "is_available": true,
        "discount": 0.0,
        "cost_price": 100.0,
        "profit": 15.0
    },
    {
        "id": 11,
        "ingredients": [
            {
                "id": 14,
                "name": "eggs",
                "quantity": 2,
                "cost_price": 5.0
            },
            {
                "id": 15,
                "name": "bread",
                "quantity": 3,
                "cost_price": 5.0
            },
            {
                "id": 16,
                "name": "Milk",
                "quantity": 5,
                "cost_price": 15.0
            }
        ],
        "name": "CupCake",
        "created_at": "2022-12-03T16:29:58.464236Z",
        "modified_at": "2022-12-03T16:29:58.445868Z",
        "expiry_date": "2023-12-03T16:29:58.445868Z",
        "selling_price": 115.0,
        "is_available": true,
        "discount": 0.0,
        "cost_price": 100.0,
        "profit": 15.0
    }
]

```