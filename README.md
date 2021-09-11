# Restaurant
Restaurant menu and order gestion web app. with this app, you can create daily menus, and customer can take a orders.the admin user can add food and gestion daily menu for customers.The customers can take a daily orders from menu options.

## Install
first you install the requariments:
```
pip install -r requirements.txt
```
following, you can create a first user using comand line
```
python manage.py create createsuperuser
```
with this user, you can get to *url: host/person/singup/* to create the first customer and administrator users. before that you can sign in in to *host/menu/*

### Links

Every link for this app have a login permission requaired and can have another to following permissions: *administrator_access* or *customer_access*.
The permission add automatilcly to user when his/her will created, depend for his/her rol selected in form. 

| URL | Short Description | Permission Need |
| ------------- | ------------- |---------------|
| host/person/singup/   | Create user | *administrator_access* |
| host/menu/   | Show today menu options | *only need login* |
| host/menu/order/   | Show all/your order | *only need login* |
| host/menu/order/create   | Create order | *customer_access* |
| host/menu/order/<int:pk>/delete/   | Delete/Calcel order | *only need login* |
| host/menu/food/create/   | Create Foot option | *administrator_access* |
| host/menu/create/   | Create Menu option | *administrator_access* |
| host/menu/<int:pk>/delete/   | Create Foot option | *administrator_access* |
| host/menu/food/list/   | List Foot options | *administrator_access* |
| host/menu/food/<int:pk>/delete/   | Delete Foot option | *administrator_access* |

## Test
Every model, vew and form for this project its tested with Django test. you can show in test folder in every app.
you can start to test everything with following comand.

```
python manage.py test
```


