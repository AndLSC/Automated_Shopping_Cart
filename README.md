
# Automated Shopping Cart Process with Selenium

## Project Description

✏️ This project demonstrates an automated process for a shopping cart system using Selenium WebDriver. The project covers functional tests for login, adding items to the cart, modifying items in the cart, removing items from the cart, checking out, and logging out, ensuring that the shopping cart functionalities are robust and reliable.



## Table of Contents

- [Project Description](#project-description)

- [Installation](#installation)

- [Usage](#usage)

- [Features](#features)

- [Test Cases](#test-cases)

- [Project Structure](#project-structure)

- [Technologies Used](#technologies-used)

- [Contributing](#contributing)

- [Contact Information](#contact-information)



## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/AndLSC/Automated-shopping-cart.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Automated-shopping-cart
    ```
3. Create a virtual environment:
    ```bash
    python -m venv myenv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```bash
        myenv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source myenv/bin/activate
        ```
5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```



## Usage
To run the tests, execute the following command:
pytest --browser=chrome

or to run in Firefox execute the following command:
pytest --browser=firefox




## Features
- Automated login functionality
- Adding random products to the shopping cart
- Removing products from the shopping cart
- Updating products in the shopping cart
- Checkout process with input validation
- Automated logout functionality




## Test Cases

#### 1. Test Case: Login
Description: This test case verifies the login functionality of the application to ensure that users can successfully log in with 
valid credentials.

|Step  |Action                        |Expected Result                                                                  |
|------|------------------------------|---------------------------------------------------------------------------------|
| 1    | Open login page              | Login page is displayed                                                         |
| 2    | Enter username and password  | Username and password are entered                                               |
| 3    | Click login button           | User is redirected to the inventory page                                        |
| 4    | Validate URL                 | URL is "https://www.saucedemo.com/inventory.html"                               |

#### 2. Test Case: Login Failed
Description: This test case validates the login functionality by ensuring that the system displays an error message when invalid 
credentials are provided. 

| Step | Action                                         | Expected Result                                               |
|------|------------------------------------------------|---------------------------------------------------------------|
| 1    | Open login page                                | Login page is displayed                                       |
| 2    | Enter incorrect username and correct password  | Incorrect username and correct password are entered           |
| 3    | Click login button                             | An error message is displayed                                 |
| 4    | Enter correct username and incorrect password  | Correct username and incorrect password are entered           |
| 5    | Click login button                             | The same error message in displayed                           |


#### 3. Test Case: Logout
Description: This test case verifies the application's logout functionality to ensure that users can successfully log out of their accounts and confirm that the session is closed securely, 
and the user is properly logged out.

| Step | Action                    | Expected Result                                        | Pre-requisite             |
|------|---------------------------|--------------------------------------------------------|---------------------------|
| 1    |                           |                                                        | Login successful          |
| 2    | Click on logout menu      | Logout menu is displayed                               |                           |
| 3    | Click on logout button    | User is logged out and redirected to the login page    |                           |
| 4    | Validate URL              | The URL "https://www.saucedemo.com/" is displayed      |                           |


#### 4. Test Case: Add Item to the Cart
Description: This test case validates that users can add items successfully to the shopping cart.  

| Step | Action                    | Expected Result                                        | Pre-requisite             |
|------|---------------------------|--------------------------------------------------------|---------------------------|
| 1    |                           |                                                        | Login successful          |
| 2    | Open inventory page       | Inventory page is displayed                            |                           |
| 3    | Add random items to cart  | Selected items are added to the cart                   |                           |     
| 4    | Open cart page            | Cart page displays the added items                     |                           |
| 5    | Validate cart items       | Cart contains the correct number of items              |                           |
| 6    | Click on logout button    | Logout is executed                                     |                           |

#### 5. Test Case: Remove Items from the Cart
Description: This test case validates that users can remove items successfully from the shopping cart.  

| Step | Action                    | Expected Result                                        | Pre-requisite                             |
|------|---------------------------|--------------------------------------------------------|-------------------------------------------|
| 1    |                           |                                                        | Login successful                          |
| 2    |                           |                                                        | Items have already been added to the cart |
| 3    | Open cart page            | Cart page is displayed                                 |                                           |
| 4    | Remove items from cart    | Selected items are removed from the cart               |                                           |
| 5    | Validate cart             | Cart is empty                                          |                                           |  
      
#### 6. Test Case: Update Item in the Cart
Description: This test case verifies that users can update items successfully in the shopping cart.  

| Step | Action                       | Expected Result                                     | Pre-requisite                             |
|------|------------------------------|-----------------------------------------------------|-------------------------------------------|
| 1    |                              |                                                     | Login successful                          |
| 2    |                              |                                                     | Items have already been added to the cart |
| 3    |                              |                                                     | Cart page is displayed                    |
| 4    | Continuing to shopping       | Add new items to the cart                           |                                           |
| 5    | Validate updated items       | Cart reflects the updated items                     |                                           |

#### 7. Test Case: Proceed to Checkout
Description: This test case ensures that users can complete the checkout process.  

| Step | Action                       | Expected Result                                     | Pre-requisite                             |
|------|------------------------------|-----------------------------------------------------|-------------------------------------------|
| 1    |                              |                                                     | Cart page is displayed                    |
| 2    |                              |                                                     | Items have already been added to the cart |
| 3    | Click checkout               | Checkout page is displayed                          |                                           |
| 4    | Enter checkout information   | Information is entered                              |                                           |
| 5    | Click finish                 | Order completion page is displayed                  |                                           |
| 6    | Validate completion message  | Message "Thank you for your order!" is displayed    |                                           |   
| 7    | Come back home page          | Order completion page is displayed                  |                                           |
| 8    | Click on logout button       | Logout is executed                                  |                                           |




## Project Structure
The project is organized into the following directories and files:

#### Directory Descriptions

- **page_objects/**: Contains the page object model classes for the different pages of the application.
  - **base_page.py**: Contains the base class for all page objects, providing common methods and utilities.
  - **checkout_page.py**: Contains the page object for the checkout page.
  - **login_page.py**: Contains the page object for the login page.
  - **shopping_cart_page.py**: Contains the page object for the shopping cart page.

- **tests/**: Contains the test cases organized into functional subdirectories.
  - **functional/**: Contains functional test cases.
    - **authentication/**: Contains test cases related to authentication.
      - **test_login.py**: Contains test cases for the login functionality.
      - **test_logout.py**: Contains test cases for the logout functionality.
    - **shopping_cart/**: Contains test cases related to the shopping cart.
      - **test_add_items_to_cart.py**: Contains test cases for adding items to the shopping cart.
      - **test_remove_items_from_cart.py**: Contains test cases for removing items from the shopping cart.
      - **test_update_items_cart.py**: Contains test cases for updating items in the shopping cart.
    - **checkout/**: Contains test cases related to the checkout process.
      - **test_checkout_process.py**: Contains test cases for the complete checkout process.
- **conftest.py**: Contains shared fixtures and configuration for the tests.
- **reports/**: Directory for functional test reports.
-**pytest.ini**: Configures pytest settings and options, such as custom markers and command-line arguments, to control test behavior.
- **requirements.txt**: Contains the list of Python dependencies required for the project.




## Technologies Used

- Python
- Selenium WebDriver
- Pytest
- Webdriver Manager



## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.




## Contact Information

For any questions or inquiries, please get in touch with Andreina at andreinasoto77@gmail.com
