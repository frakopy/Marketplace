# Marketplace Web App
This is a README file for a marketplace web application built using Django, JavaScript, HTML, CSS, and Bootstrap. The application allows users to register, authenticate via username and password, and also provides Google Authentication for login. Users can post new products, search for products by name and category, communicate with sellers and clients through chat messages, and access a basic dashboard for managing their own products.

## Technologies Used
* Django: Django is a high-level Python web framework that provides a clean and efficient way to build web applications.
* JavaScript: JavaScript is a programming language commonly used for web development to add interactivity and dynamic features to web pages.
* HTML: HTML (Hypertext Markup Language) is the standard markup language for creating web pages and applications.
* CSS: CSS (Cascading Style Sheets) is used to style the visual presentation of HTML documents.
* Bootstrap: Bootstrap is a popular CSS framework that provides pre-built components and styles for creating responsive web designs.
  
## Features
* User Authentication: Users can create an account, log in using their username and password, and also use Google Authentication for easy login.

* Product Posting: Registered users can post new products for sale, including details such as title, description, price, and category.

* Product Search: Users can search for products using the name of the product or by selecting a category from the provided section.

* Chat Messaging: The application allows communication between sellers and clients through chat messages. Users can exchange messages to discuss product details, negotiate prices, and arrange transactions.

* Dashboard: The web app provides a basic dashboard for users to manage their own products. Users can view, edit, and delete their posted products. They have the following capabilities:

* View a list of their own products.
1. Edit the details (title, description, price, category) of their own products.
2. Delete their own products from the marketplace.
   
## Setup Instructions    
1. Clone the repository to your local machine.

2. Install Python (if not already installed) and set up a virtual environment.

3. Activate the virtual environment and install the required dependencies by running the following command:   

`pip install -r requirements.txt`

4. Create the following enviroment variables in a .env file
   `SECRET_KEY="your-secret-key"`  
   `DEBUG="True or False"`  
   `DB_NAME="Your-db-name"`  

5. Set up the database by applying migrations:    

`python manage.py migrate`

6. Create a superuser account to access the admin dashboard:    

`python manage.py createsuperuser`

7. Start the development server:    

`python manage.py runserver`  

8. Access the web application by visiting http://localhost:8000 in your web browser.

## Usage
1. Open the web application in your browser.
2. Register a new account or log in using your existing credentials.
3. Use the provided options to post new products, search for products, and communicate with other users through chat messages.
4. Access the dashboard to manage your own posted products.

## Contributions
Contributions to the marketplace web app are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## Contact
If you have any questions or need further assistance, please contact Frakopy at frako789@gmail.com

Enjoy using the marketplace web app!
