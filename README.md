# FreshPick

![FreshPick Home](webapp/FreshPickApp/static/imgs/screenshot.png)

## Introduction

FreshPick is a web application designed to simplify the process of ordering fresh groceries for pickup at your local grocery store. Our platform allows users to browse and select from a wide range of fresh produce, ensuring a seamless and efficient shopping experience.

- **Deployed Site**: [FreshPick](https://fresh-pick.vercel.app/)
- **Final Project Blog Article**: [FreshPick Blog Post](https://medium.com/@yourusername/freshpick-webapp-overview)
- **Author(s) LinkedIn**:
  - Author 1 : [El Amraoui Khalil](https://www.linkedin.com/in/khalil-el-amraoui-5834a9216/)
  - Author 2 : [El Mouajjeh Soufiane](https://www.linkedin.com/in/soufiane-elmouajjeh-052929280/)
  - Author 3 : [Leknouch Wissal](https://linkedin.com/in/author2)

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/khalilelamraoui/Fresh-pick.git
    cd Fresh-Pick
    ```

2. Create a virtual environment:
    ```bash
    cd webapp
    python -m venv env
    source env/bin/activate   # On Windows, use `env\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    pip install django
    ```

4. Configure your MySQL database in `settings.py`:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'your_db_name',
            'USER': 'your_db_user',
            'PASSWORD': 'your_db_password',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    ```

5. Apply migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. Run the development server:
    ```bash
    python manage.py runserver
    ```

7. Open your browser and navigate to `http://127.0.0.1:8000/`.

## Usage

1. Register for an account or log in if you already have one.
2. Browse the available products.
3. Add desired products to your cart.
4. Proceed to checkout to place your order for pickup at the grocery store.

## Contributing

We welcome contributions to the FreshPick project. To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-name
    ```
3. Make your changes and commit them with descriptive messages:
    ```bash
    git commit -m "Description of the feature"
    ```
4. Push your changes to your forked repository:
    ```bash
    git push origin feature-name
    ```
5. Open a pull request with a detailed description of your changes.

## Related Projects

- [Fresh Pick Landing Page](https://github.com/Clear008/FreshPick)
- [Grocery Store Dataset](https://github.com/marcusklasson/GroceryStoreDataset)

## Licensing

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

![FreshPick Logo](webapp/FreshPickApp/static/imgs/freshpick.png)
