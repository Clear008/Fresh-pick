# Fresh-pick

Fresh-pick: Your go-to destination for fresh groceries, veggies, and fruits. Browse, shop, and enjoy hassle-free shopping with secure checkout and convenient delivery options.

## Table of Contents

- [Fresh-pick](#fresh-pick)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Architecture](#architecture)
    - [Components](#components)
  - [User Stories](#user-stories)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Backend Setup](#backend-setup)
    - [Frontend Setup (Planned)](#frontend-setup-planned)
  - [Usage](#usage)
  - [API Documentation](#api-documentation)
    - [/api/products](#apiproducts)
    - [/api/cart](#apicart)
    - [/api/orders](#apiorders)
  - [Models](#models)
  - [Third-Party APIs](#third-party-apis)
  - [License](#license)

## Features

- User authentication and management
- Product listing and categorization
- Shopping cart functionality
- Order processing
- Integration with payment gateway, Google Maps, and Twilio for SMS notifications

## Architecture

The architecture of Fresh-pick is designed to be modular and scalable. Below is a high-level diagram of the system:

![Architecture Diagram](link_to_architecture_diagram.png)

### Components

- **Frontend:** React (planned)
- **Backend:** Django, Django REST Framework
- **Database:** MySQL
- **Third-Party Services:**
  - Payment Gateway API
  - Google Maps API
  - Twilio API

## User Stories

1. **As a user, I want to create an account so that I can manage my shopping experience.**
    - Checklist:
        - [ ] Implement user registration
        - [ ] Implement user login
        - [ ] Implement user profile management

2. **As a user, I want to browse products so that I can find items to purchase.**
    - Checklist:
        - [ ] Create product listing page
        - [ ] Implement product search and filter
        - [ ] Display product details

3. **As a user, I want to add products to my cart so that I can purchase them later.**
    - Checklist:
        - [ ] Implement add to cart functionality
        - [ ] Display cart items
        - [ ] Update item quantities in the cart

4. **As a user, I want to place an order so that I can buy the items in my cart.**
    - Checklist:
        - [ ] Implement order placement
        - [ ] Integrate payment gateway
        - [ ] Send order confirmation via SMS

5. **As an admin, I want to manage product listings so that I can keep the inventory up-to-date.**
    - Checklist:
        - [ ] Implement product CRUD operations
        - [ ] Implement admin dashboard


## API Documentation

### /api/products

- **GET:** Retrieves a list of available products.
- **POST:** Adds a new product to the database.

### /api/cart

- **GET:** Retrieves the current user's cart items.
- **POST:** Adds a product to the user's cart.

### /api/orders

- **GET:** Retrieves the user's order history.
- **POST:** Places a new order for the user.

## Models

- **User:** Custom user model extending `AbstractUser`
- **Product:** Model for product details
- **Cart:** Model representing a user's shopping cart
- **CartItem:** Model for items in the cart
- **Order:** Model for user orders
- **OrderItem:** Model for items in an order

## Third-Party APIs

- **Payment Gateway API:**
  - `POST /api/payment/process`: Initiates payment processing for an order.
  - `GET /api/payment/status/{transactionId}`: Retrieves the status of a payment transaction.

- **Google Maps API:**
  - `GET /maps/api/geocode/json`: Retrieves geographic coordinates for a given address.
  - `GET /maps/api/directions/json`: Calculates directions and travel time between two locations.

- **Twilio API:**
  - `POST /api/twilio/sendSMS`: Sends an SMS message to a specified phone number.
  - `GET /api/twilio/messageStatus/{messageId}`: Retrieves the status of a sent SMS message.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
