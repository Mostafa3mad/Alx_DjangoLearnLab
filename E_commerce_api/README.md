# 🛒 **E-Commerce Project Documentation**

---

## 1. 🎯 **Project Overview**
This Django-based E-Commerce project aims to provide an online shopping platform with features such as user registration, login, product management, cart management, product search functionality, and user profile management with order tracking and checkout.

---

### ✅ **Features Implemented So Far:**
- **User Authentication:** Registration, login with JWT tokens, and session-based authentication.
- **Product Management:** CRUD operations for managing products.
- **Shopping Cart:** Ability to add, update, and remove products from the shopping cart.
- **Search Products:** Search for products by name or category.
- **User Profile Management:** Ability for users to update profile information and change passwords.
- **Order Management:** Basic structure for checkout and order creation.

---

## 2. 🛠️ **Technologies Used**
- **Django:** Backend framework to handle data models, views, and routing.
- **Django REST Framework (DRF):** For building API endpoints.
- **SimpleJWT:** For JWT token-based authentication to secure endpoints.
- **SQLite (default):** Database for storing users, products, and cart data.
- **Session Authentication:** To allow logged-in users to interact with the API seamlessly.

---

## 3. 🚀 **Features Implemented**

---

### 🎟️ **User Management**
✅ **User Registration:**  
- **Endpoint:** `POST /api/register/`  
- **Functionality:** Allows new users to register by providing username, email, and password.  

✅ **User Login:**  
- **Endpoint:** `POST /api/login/`  
- **Functionality:** Users log in and receive a JWT token for authorization on subsequent requests.  

✅ **JWT Authentication:**  
- **Endpoints:**  
    - `POST /api/token/` for login.
    - `POST /api/token/refresh/` for refreshing tokens.  

✅ **Session Authentication (New):**  
- **Endpoints:**  
    - `POST /api/login/` (Session-based login)  
    - `GET /api/logout/` (Logout with session)  

✅ **User Profile Management:**  
- **Endpoint:** `GET /api/profile/`  
- **Functionality:** Allows authenticated users to view their profile information.  

✅ **Update Profile:**  
- **Endpoint:** `PUT /api/profile/`  
- **Functionality:** Allows users to update their profile information (first name, last name, and email).  

✅ **Change Password:**  
- **Endpoint:** `POST /api/profile/change-password/`  
- **Functionality:** Allows authenticated users to change their password securely.  

---

### 📦 **Product Management**
✅ **Add Product:**  
- **Endpoint:** `POST /api/product/add/`  
- **Functionality:** Admins or authenticated users can add new products to the store.  

✅ **Product CRUD Operations:**  
- `GET /api/products/`: List all products.  
- `POST /api/products/`: Add a new product.  
- `PUT /api/products/{id}/`: Update an existing product.  
- `DELETE /api/products/{id}/`: Delete a product.  

---

### 🛒 **Shopping Cart Management**
✅ **Add to Cart:**  
- **Endpoint:** `POST /api/cart/add/`  
- **Functionality:** Authenticated users can add products to their shopping cart.  

✅ **Update Cart Items (New):**  
- **Endpoint:** `POST /api/cart/add/`  
- **Functionality:** If a product already exists in the cart, the quantity is updated dynamically.  

✅ **Remove from Cart:**  
- **Endpoint:** `POST /api/cart/remove/`  
- **Functionality:** Authenticated users can remove products from their shopping cart.  

✅ **Cart Total Calculation (New):**  
- **Functionality:** Cart items are dynamically updated, and the total price is calculated during checkout.  

---

### 🔎 **Product Search**
✅ **Search by Name or Category:**  
- **Endpoint:** `GET /api/search?name={name}` or `GET /api/search?category={category}`  
- **Functionality:** Users can search products by name or category.

---

## 4. 📚 **API Endpoints Summary**

### 🧑‍💻 **User Management:**
- `POST /api/register/` ➡️ Register a new user.
- `POST /api/login/` ➡️ Login with JWT token.
- `POST /api/token/` ➡️ Obtain JWT token.
- `POST /api/token/refresh/` ➡️ Refresh JWT token.
- `GET /api/profile/` ➡️ View user profile.
- `PUT /api/profile/` ➡️ Update profile.
- `POST /api/profile/change-password/` ➡️ Change password.

### 🛍️ **Product Management:**
- `POST /api/product/add/` ➡️ Add a new product.
- `GET /api/products/` ➡️ List all products.
- `PUT /api/products/{id}/` ➡️ Update a product.
- `DELETE /api/products/{id}/` ➡️ Delete a product.

### 🛒 **Shopping Cart:**
- `POST /api/cart/add/` ➡️ Add a product to the cart.
- `POST /api/cart/remove/` ➡️ Remove a product from the cart.

### 🔎 **Search:**
- `GET /api/search?name={name}` ➡️ Search products by name.
- `GET /api/search?category={category}` ➡️ Search products by category.

---

## 5. ⚡ **Challenges Faced**

---

### 🔐 **1. JWT and Session Authentication Integration**
**Problem:**  
Initially, integrating JWT authentication and ensuring that only authenticated users could modify products was challenging.  

**Solution:**  
- I used the `SimpleJWT` package to handle JWT tokens.  
- Added `SessionAuthentication` to support session-based interactions during development and admin management.  

---

### 🛒 **2. Cart Management**
**Problem:**  
Managing the cart dynamically and ensuring that quantity updates are handled properly was confusing.  

**Solution:**  
- I used a `ManyToMany` relationship between `Cart` and `Product` with a `through` model (`CartItem`).  
- Updated the cart to allow quantity modification dynamically when adding existing items.  

---

### 🔎 **3. Search Optimization**
**Problem:**  
Implementing search by both name and category simultaneously required dynamic query filtering.  

**Solution:**  
- Leveraged Django’s `Q` objects to perform flexible and dynamic querying.  

---

## 6. ⏩ **Pending Tasks and Next Steps**

---

### 👤 **1. User Profile Management Enhancements**
- ✅ Update profile functionality added.
- ✅ Change password functionality added.
- ⚡ Pending: Add order history and past purchases.

---

### 📦 **2. Order Management (Checkout Process)**
- Pending: Add functionality for users to complete purchases, process payments, and track order status.
- Pending: Add order confirmation email functionality.

---

### 🔍 **3. Product Validation**
- Pending: Add product validation (e.g., ensuring that prices are positive, and stock quantities are not negative).

---

### 🛒 **4. Cart Checkout and Order Placement**
- Pending: Implement the process of checking out from the cart, calculating the total, and confirming the order.

---

### 💳 **5. Payment Gateway Integration**
- Pending: Add support for integrating a payment gateway (e.g., Stripe or PayPal) to complete transactions.

---

## 7. 🎉 **Conclusion**
The project is progressing well with the core features implemented, including user authentication, product management, cart functionalities, and profile management. Moving forward, the focus will be on enhancing the checkout process, adding order management, and integrating payment gateways to ensure a seamless user experience.

---

### 📢 **Future Enhancements:**
- Implement **Email Notifications** for order confirmation and account changes.
- Add **Multi-Language Support** to enhance user experience globally.
- Introduce **Wishlist Feature** for saving favorite items.

✅ **This document will be updated regularly as new features are added and issues are resolved.**
