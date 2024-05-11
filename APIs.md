
### APIs and Methods

**API Routes for Web Client:**

- `/api/users`
  - **GET:** Retrieves user information based on user ID.
  - **POST:** Creates a new user.

- `/api/carts`
  - **GET:** Retrieves the user's shopping cart items.
  - **POST:** Adds a product to the user's shopping cart.

- `/api/orders`
  - **GET:** Retrieves the user's order history.
  - **POST:** Places a new order for the user.

- `/api/products`
  - **GET:** Retrieves a list of available products for users to browse.
  - **POST:** Adds a new product to the database.

**API Endpoints for Other Clients:**

- **Class: User**
  - *Description:* Represents a user of the application.
  - *Methods:*
    - `getUserInfo(userId)`: Retrieves user information based on the provided user ID.
    - `createUser(userData)`: Creates a new user with the provided data.

- **Class: Order**
  - *Description:* Manages user orders and order history.
  - *Methods:*
    - `getUserOrders(userId)`: Retrieves the order history for a specific user.
    - `placeOrder(userId, orderData)`: Places a new order for the user with the provided order data.

**3rd Party APIs:**

- **Payment Gateway API**
  - *Description:* Integrates with a payment gateway service for processing payments.
  - *Endpoints:*
    - `POST /api/payment/process`: Initiates payment processing for an order.
    - `GET /api/payment/status/{transactionId}`: Retrieves the status of a payment transaction.

- **Google Maps API**
  - *Description:* Provides geolocation and mapping services.
  - *Endpoints:*
    - `GET /maps/api/geocode/json`: Retrieves geographic coordinates for a given address.
    - `GET /maps/api/directions/json`: Calculates directions and travel time between two locations.

- **Twilio API**
  - *Description:* Sends SMS notifications to users.
  - *Endpoints:*
    - `POST /api/twilio/sendSMS`: Sends an SMS message to a specified phone number.
    - `GET /api/twilio/messageStatus/{messageId}`: Retrieves the status of a sent SMS message.

