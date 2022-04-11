
## Python Libs
- fastapi
- fastapi_jwt_auth
- sqlalchemy

## ROUTES TO IMPLEMENT
| METHOD | ROUTE | FUNCTIONALITY |ACCESS|
| ------- | ----- | ------------- | ------------- |
| *POST* | ```/auth/signup/``` | _Register new user_| _All users_|
| *POST* | ```/auth/login/``` | _Login user_|_All users_|
| *GET* | ```/docs/``` | _View API documentation_|_All users_|
| *GET* | ```/orders/orders/``` | _List all orders made_|_Superuser_|
| *GET* | ```/orders/orders/{order_id}/``` | _Retrieve an order_|_Superuser_|
| *POST* | ```/orders/order/``` | _Place an order_|_Current user_|
| *GET* | ```/orders/user/orders/``` | _Get user's orders_|_Current user_|
| *GET* | ```/orders/user/order/{order_id}/``` | _Get user's specific order_|_Current user_|
| *PUT* | ```/orders/order/update/{order_id}/``` | _Update an order_|_Current user_|
| *PATCH* | ```/orders/order/update/{order_id}/``` | _Update order status_|_Superuser_|
| *DELETE* | ```/orders/order/delete/{order_id}/``` | _Delete/Remove an order_ |_Current user_|

