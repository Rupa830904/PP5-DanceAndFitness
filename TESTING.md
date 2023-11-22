# Testing

Back to [README.MD](README.md)<br>

## Table of contents
* [User Story and Feature Testing](#user-story-and-feature-testing)
* [Automated View Testing](#automated-view-testing)
* [Browser Testing](#browser-testing)
* [Code Validation](#code-validation)
* [Bugs](#bugs)

## User Story and Feature Testing
All the user stories were tested manually comprehensively, including all the representative features, and were documented below with a summary of the steps made for demonstrating the validation of the tests: <br>

### EPIC - AUTHENTICATION
#### As a user I must be able to register to the danceandfitness* so that I can buy packages
* **Acceptance Criteria:** All auth function is implementes to provide new user to register.
* **Summary:**<br>
    - There is a Register page that provides a form with email, username and password for the user to fill in;<br>
    - When the user submits the form he is redirected to a page that informs him that he needs to verify his email to finalize the signup process;<br>
    - An info alert is displayed with the message "Confirmation e-mail sent to..." that suggests the user needs to verify his email.<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass 

#### As a user I want to be able to confirm my account with an email so that I can authenticate my registration.
* **Acceptance Criteria:** User gets an email with confirmation link while registering.
* **Summary:**<br>
    - An email is sent to the user when he tries to register on the page;<br>
    - The email includes a link that will redirect him to a page from the shop website where he can confirm the email by clicking on a button.<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass


#### As a user I want to be able to log out at any time
* **Acceptance Criteria:** User is prompted with logout confirmation button and upon clicking that user is logged out.
* **Summary:**    
    - There is a Logout modal that can be triggered when clicking on the hyperlink in the navbar. The modal is implemented as part of a defensive programming;<br> 
    - The logout modal asks the user again if he wishes to log out of the current account;<br> 
    - A success alert is displayed with the message "Logged out" that confirms to the user that he has been successfully logged out.<br><br> 
    
    *By testing all these features, it can be affirmed that the user story is accomplished.*<br>
* **Outcome:** Pass

### EPIC - PRODUCTS
#### As an user I can view the product catalogue so that I can choose the right product
* **Acceptance Criteria:** A buuton is enabled on the 'Home' page to direct to product page and view all products..
* **Summary:**<br> 
   - In the navigation menu there are separate links that redirect the user to the products' catalogue. These links are classified as: <em>All products</em><br>
    - Also there is a 'Explore Now' button in the home page which lands into All products page.

    *By testing this feature, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass

#### As a user I can sort packages so that I can choose packages
* **Acceptance Criteria:** Sort function implemented under drop down in Nav Bar..
* **Summary:**<br>
   - On the Nav Bar user sort the prducts as:, <em>By Category</em>, <em>By Price</em>;<br><em>
    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass

#### As a **user ** I can read the product details so that I can choose the package
* **Acceptance Criteria:** User is directed to product details page upon click on each packages/products.
* **Summary:**<br>
    - Every item listed on products' pages is clickable and it redirects to the selected product's details page;<br>
    - The details page includes the product's name, price, and a short description of the product;<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass

#### As a super user I can update the price and description of a package so that I can change the offer to make it more attractive
* **Acceptance Criteria:** Super user has 'Edit Package' link and Edit form open to update package.
* **Summary:**<br>
    - When a user is logged in as admin, the page for product details provides a link for updating package details like price and description in a form.<br>
    - The form has validation that prevents the user to update a product with invalid information;<br>
    - Any update is reflected in the product's details page;<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br><br> 
* **Outcome:** Pass

#### As an admin I can add new package so that I can add new offers for user
* **Acceptance Criteria:** An Add package form has been implemented for superuser.
* **Summary:**<br>
    - When a user is logged in as admin, the product catalogue page includes a link for <em>Add a new product</em>;<br>
    - When the link is clicked, it redirects to a form with fields for every detail of the product;<br>
    - After the form is submitted, the element is added to the products' list.<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass

#### As a user I can search a package in home page so that I can find a package easily
* **Acceptance Criteria:** A search bar is implemented in the home page to search for package.
* **Summary:**<br>
    - User has a seearch bar in home page where the user can search for a product name or any matching description in product details. ;<br>
    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass

#### As a user I can back to shopping from cart so that my cart is updated each time I update my shopping items
* **Acceptance Criteria:** A 'Keep Shopping' button is available for users to go back to shopping and cart info is saved in the session.
* **Summary:**<br>
    - On the <em>Product Details</em> page, for every product in the table there is a button 'KEEP SHOPPING' to continue shopping;<br>
   
    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass
### EPIC - RATING&REVIEWS
#### As a user I can read detailed reviews so that I know more about the product
* **Acceptance Criteria:** A button implented in product detail page to read detailed user reviews..
* **Summary:**<br>
    - on product details page, there is a button 'Show reviews';<br> 
    - Every review message is listed after clicking on that button.;<br>
    
    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass

#### As a user I can review and rate a product so that I can give feedback
* **Acceptance Criteria:** A user feedback form has been implemented and available to user after login for all products.
* **Summary:**<br> 
    - On the <em>Product details</em> page there is a section for "Write review" only visible for authenticated users.<br>
    - The form only contains inputs for product name, rating, and comment.<br>
    - There is no implementation for approval of the reviews for the purpose of full transparency;<br>
    - The response is immediate and the review appears as the on the list; <br><br>
    - The response is immediate and rating is changed as per the avg of all reviews <br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass 

#### As a user I can view total reviews and ratings of all packages so that I can choose the appropriate package.
* **Acceptance Criteria:** User can view reviews and ratings of all packages.
* **Summary:**<br> 
    - A user can view num of reviews on product details page of every product.<br>
    - The rating is displayed on the product's details page and for every element listed on the products' pages.<br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass

### EPIC - CART
#### As a user I can add items to cart so that I can checkput when I am ready
* **Acceptance Criteria:** User has an option to add items to cart and cart info is saved for user's session.
* **Summary:**<br>
    - There is a <em>ADD TO CART</em> button on product details page<br>
    - Shoppic cart is updated with the added product on click.<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass
#### As a user I can update items in cart so that I can change my shopping list
* **Acceptance Criteria:** User has a link to update item info in cart.
* **Summary:**<br>
   - On the <em>Shopping cart</em> page, for every product in the table there is a 'udpate link' visible only to users that are authenticated <br>
   - On click, it opens a box where user can update quantity and it is reflected on cart <br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass
#### As a user I should be notfied when a item is added/updated/removed from cart so that I get a confirmation message
* **Acceptance Criteria:** AUser gets a popup message for add/update/remove from cart.
* **Summary:**<br>
   - User gets a pop-up message for  actions like add/rmove item from cart.

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass
#### As a user I can remove item from cart so that I can remove item from my shopping list
* **Acceptance Criteria:**Use has a link to remove item from cart.
* **Summary:**<br>
   - On the <em>Shopping cart</em> page, for every product in the table there is a link for removing the product<br>
   - When the users click on the link, the product is removd from the cart;<br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass

### EPIC - CHECKOUT&PAYMENT
#### As a user I can pay with my credit card so that I can buy the packages
* **Acceptance Criteria:** user can provide the credit card details and pay for the bought packages.
* **Summary:**<br>
    - On the <em>Checkout</em> page there is a form section with fields for Credit Card payment authentication<br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass
#### As a user I can proceed to secure checkout so that I can buy the health packages
* **Acceptance Criteria:** Secure checkout option is enabled on shopping cart to proceed to checkout.
* **Summary:**<br>
    - On the <em>Checkout</em> page, there is a table with every product added to checkout;<br>
    - On the <em>Checkout</em> page, for every product in the table, the price per item is displayed;<br>
    - There is also an <em>Order Summary</em> section with full specifications about the total price.<br> <br>
    
    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass


### EPIC - USER MANAGEMENT
#### As a user I need to I should be able to save personal details so that my profile is saved for every purchases
* **Acceptance Criteria:** Profile app is created and user is offered the form to save personal details.
* **Summary:**<br>  
    - On the <em>Profile</em> page, there is a form with fields for personal details;<br>
    
    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass
#### As a user I can view my order history so that I know my previous purchases
* **Acceptance Criteria:** User can click on the previous order number and be directed to order details.
    - A logged in user On the <em>Profile</em> page, there is a table that includes a list of all the orders made by the authenticated user;<br>
    - Every order element displayed in the table contains link to see further details about the order.<br><br>
    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass
#### As a user I can see my order history under my profile so that I can see me previous order details
* **Acceptance Criteria:** User is presented with the link to all previous orders under 'My Profile.'
* **Summary:**<br> 
   - A logged in user On the <em>Profile</em> page, there is a table that includes a list of all the orders made by the authenticated user;<br>
   - Every order element displayed in the table contains link to see further details about the order.<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass
#### As a user I can submit the contact form so that I can get in touch with the service provide also subscribe to newsletters
* **Acceptance Criteria:** User contact from is implemented for submit by the user.
    - The CONTACT US page of the website provides us the form to conatct D&F for any questions or subscribe for newsletters.<br><br>

     *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass



### Aditional Manual Testing
#### Error Handling

* Ensure that **403 HTTP** errors display custom 403.html.
    - **Stress Test:** Input a route in the URL for accessing another user content
* Ensure that **404 HTTP** errors display the custom 404.html.
    - **Stress Test:** Input a random route in the URL that can't be found in the declared paths of the project
* Ensure that **500 HTTP** errors display the custom 500.html.
    - **Stress Test:** Set debug to false and try to access a path that has been breaked intentionally.


#### Interface Interaction

* Ensure all interactive elements respond appropriately:
    - **Desktop:**
        - All navbar elements correctly respond to hovering.
        - All buttons correctly respond to hovering.
        - All authentication links correctly respond to hovering
    - **Mobile:**
        - All navbar elements correctly respond to touch.
        - All buttons correctly respond to touch.
        - All authentication links correctly respond to touch


#### Links

* Ensure the external links to social media present in the footer open up in new tabs.

## Browser Testing
The website was tested on different browser to ensure all features work accordingly.
* Chrome
* Edge
* Firefox

## Code Validation
### HTML

The html code of the website was validated using [W3 Markup Validator](https://validator.w3.org/).<br>
At the time of deployment the validation have the following outcome:<br><br>

<img src="media/pp5_html_validation.png" width="60%"><br><br>

The following pages have been tested:
* Home
* Products
* Product details
* Cart
* Checkout
* Checkout Success
* User Profile
* Admin Orders
* Contact
* About
* Login/Register
* 403/404/500 custom pages

### CSS

The CSS code was validated using [W3 Jigsaw Validator](https://jigsaw.w3.org/css-validator/)<br>
At the time of deployment the validation for *base.css* has the following outcome:<br><br>

<img src="media/CSS-Validation_checkout.png" width="60%"><br><br>

<img src="media/CSS-Validation1.png" width="60%"><br><br>

### Javascript

The Javascript code was validated using using [JsHint](https://jshint.com/)<br>
At the time of deployment the validation for * *stripe_elements.js* have the following outcome:<br>
<details>
<summary>stripe_elements.js</summary>
<img src="media/stripe_element_jshint.png" width="40%"><br><br>
</details>

* The warnings listed are caused by the EventListeners added to elements in a loop.<br>
I tried to solve the issue but no successful method has been found, so I chose to ignore the warning as it is not affecting the way my code works in any way.

### Python
The python code was tested using [Code Institute python linter](https://pep8ci.herokuapp.com/) online validator.<br>
At the time of deployment the python code validation have the following outcomes:<br><br>

<details>
<summary>Main App</summary>
<img src="media/context_processor.png" width="70%"><br><br>

</details>
<details>
<summary>Bag App</summary>
<img src="media/bag_context.png" width="70%"><br><br>

</details>
<details>
<summary>Checkout App</summary>
<img src="media/checkout_app1.png" width="70%"><br><br>

</details>
<details>
<summary>Contact App</summary>
<img src="media/contact_app1.png" width="70%"><br><br>

</details>
<details>
<summary>Newsletter App</summary>
<img src="media/newsletter_app1.png" width="70%"><br><br>

</details>
<details>
<summary>Product Reviews App</summary>
<img src="media/review_app1.png" width="70%"><br><br>

</details>
<details>
<summary>Products App</summary>
<img src="media/products_app1.png" width="70%"><br><br>

</details>
<details>
<summary>Profiles App</summary>
<img src="media/profiles_app1.png" width="70%"><br><br>


</details>


### Accesibility 
The accesibility of the website was tested with [Wave](https://wave.webaim.org/)

**Wave results:**<br>
<details>
<summary>Home page</summary>
<img src="media/wave_home.png" width="30%"><br><br>
</details>
<details>
<summary>Products page</summary>
<img src="media/wave_products.png" width="30%"><br><br>
</details>
<details>
<summary>Login page</summary>
<img src="media/wave_signin.png" width="30%"><br><br>
</details>
<details>
<summary>Register page</summary>
<img src="media/wave_register.png" width="30%"><br><br>
</details>
<details>
<summary>About page</summary>
<img src="media/wave_about.png" width="30%"><br><br>
</details>
<details>
<summary>Contact page</summary>
The contact page result is showing one error about the map image missing alternative text. I tried to fix it but was unsuccessful.
<img src="media/wave_contact.png" width="30%"><br><br>
</details>
<details>
<summary>FAQs Page</summary>
<img src="media/wave_faqs.png" width="30%"><br><br>
</details>
<details>
<summary>Bag Page</summary>
<img src="media/wave_bag.png" width="30%"><br><br>
</details>
<details>
<summary>Admin Page</summary>
<img src="media/wave_admin_orders.png" width="30%"><br><br>
</details><br>




## BUGS
I encountered many challenges during the whole building process of this project. So much so, that I often forget to list them down here as a bug and just get my head stuck in solving them. But the ones listed below were the ones that really challenged my tenacity and patience.
### Solved
* **Update quantity in shopping cart page**
     When I added update cart feature in cart page I struggled a lot to update the quantity and reflect that in my cart session. 
     Solution:
     I took help from CI tutors to solve and understand the  update cart view and corrected the flow to update the cart session.

* **Stripe Element not working as expected**
     When I implemented stripe payments and try to check that everything works, I could only go as far as 'Secure Checkout' but it wouldn't bring me to success checkout page as expected.
     Solution:
     I took help from CI tutors to solve and understand how stripe works and required variables are added on config vars.

* **reviews not showing in a table**
    When I had implemented reviews button I had a challenge to display them in a table. 
    Solution:
    I took help from CI tutors to solve and understand how I can dsiplay in bootstrap table and also can iterate the value over the output.

Back to [README.MD](README.MD)<br>