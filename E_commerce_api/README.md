# **E-Commerce Project Documentation**

## **1. Project Overview**
This Django-based E-Commerce project aims to provide an online shopping platform with features such as user registration, login, product management, cart management, and product search functionality.

### **Features Implemented So Far:**
- **User Authentication**: Registration and login with JWT tokens.
- **Product Management**: CRUD operations for managing products.
- **Shopping Cart**: Ability to add and remove products from the shopping cart.
- **Search Products**: Search for products by name or category.

---

## **2. Technologies Used**
- **Django**: Backend framework to handle data models, views, and routing.
- **Django REST Framework (DRF)**: For building API endpoints.
- **SimpleJWT**: For JWT token-based authentication to secure endpoints.
- **SQLite (default)**: Database for storing users, products, and cart data.

---

## **3. Features Implemented**

### **User Management**
- **User Registration**: 
  - **Endpoint**: `POST /api/register/`
  - **Functionality**: Allows new users to register by providing `username`, `email`, and `password`.
  - **Status**: ✅ Implemented.
  
- **User Login**:
  - **Endpoint**: `POST /api/login/`
  - **Functionality**: Users log in and receive a JWT token for authorization on subsequent requests.
  - **Status**: ✅ Implemented.
  
- **JWT Authentication**:
  - **Endpoints**: `POST /api/token/` for login, `POST /api/token/refresh/` for refreshing tokens.
  - **Status**: ✅ Implemented.

### **Product Management**
- **Add Product**:
  - **Endpoint**: `POST /api/product/add/`
  - **Functionality**: Admins or authenticated users can add new products to the store.
  - **Status**: ✅ Implemented.
  
- **Product CRUD Operations**:
  - **GET /products/**: List all products.
  - **POST /products/**: Add a new product.
  - **PUT /products/{id}/**: Update an existing product.
  - **DELETE /products/{id}/**: Delete a product.
  - **Status**: ✅ Implemented (Basic functionality).

### **Shopping Cart Management**
- **Add to Cart**:
  - **Endpoint**: `POST /api/cart/add/`
  - **Functionality**: Authenticated users can add products to their shopping cart.
  - **Status**: ✅ Implemented.

- **Remove from Cart**:
  - **Endpoint**: `POST /api/cart/remove/`
  - **Functionality**: Authenticated users can remove products from their shopping cart.
  - **Status**: ✅ Implemented.

### **Product Search**
- **Search by Name or Category**:
  - **Endpoint**: `GET /search?name={name}` or `GET /search?category={category}`
  - **Functionality**: Users can search products by name or category.
  - **Status**: ✅ Implemented.

---

## **4. API Endpoints Summary**

Here is a list of the API endpoints implemented so far:

- **User Management**:
  - `POST /api/register/`: Register a new user.
  - `POST /api/login/`: Login with JWT token.
  - `POST /api/token/refresh/`: Refresh JWT token.

- **Product Management**:
  - `POST /api/product/add/`: Add a new product to the store.
  - `GET /products/`: List all products.
  - `PUT /products/{id}/`: Update an existing product.
  - `DELETE /products/{id}/`: Delete a product.

- **Shopping Cart**:
  - `POST /api/cart/add/`: Add a product to the cart.
  - `POST /api/cart/remove/`: Remove a product from the cart.

- **Search**:
  - `GET /search?name={name}`: Search products by name.
  - `GET /search?category={category}`: Search products by category.

---

## **5. Challenges Faced**

### **1. JWT Authentication Integration**
   - **Problem**: Initially, I struggled with integrating JWT authentication and ensuring that only authenticated users could add, update, or delete products.
   - **Solution**: I used the `SimpleJWT` package to handle token-based authentication and managed to set it up correctly. I applied `IsAuthenticatedOrReadOnly` permission in the views to restrict access to certain actions.

### **2. Cart Management**
   - **Problem**: Managing the cart efficiently and ensuring users can add/remove products dynamically created some confusion, especially when dealing with cart items.
   - **Solution**: I used a `ManyToMany` relationship between `Cart` and `Product`, using a through model `CartItem` to store quantities for each product.

### **3. Search Functionality**
   - **Problem**: Implementing search by both name and category at the same time required dynamic query filtering.
   - **Solution**: I leveraged Django's `Q` objects for flexible querying based on optional `name` and `category` parameters.

---

## **6. Pending Tasks and Next Steps**

### **1. User Profile Management**
   - **Pending**: Implement the ability for users to update their profiles, change passwords, and view order history.
   
### **2. Order Management (Checkout Process)**
   - **Pending**: Add functionality for users to complete purchases, process payments, and track order status.

### **3. Product Validation**
   - **Pending**: Add product validation (e.g., ensuring that prices are positive, stock quantities are not negative).

### **4. Cart Checkout**
   - **Pending**: Implement the process of checking out from the cart, calculating the total, and confirming the order.

### **5. Payment Gateway Integration**
   - **Pending**: Add support for integrating a payment gateway (e.g., Stripe or PayPal) to complete transactions.

---

## **7. Conclusion**

The project is progressing well with the core features implemented, including user authentication, product management, and cart functionalities. Moving forward, the focus will be on improving the user experience with the addition of order management, payment gateways, and profile management.

This document will be updated regularly as new features are added and issues are resolved.

