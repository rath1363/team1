# User Acceptance Tests

The following user acceptance tests will test the signup, login, and logout capabilities of a user who wants to create an account on the application and use that account to plan their weekend in Miami. In general, a user should be able to create an account, access that account and the functionality of the app through that account, and be able to leave their account and log out of the app at any time.

### 1. Validate Signup Functionality
Use case name
    Verify signup with username, email, and password.
Description
    Test the "Weekend in Miami - Signup" page and user experience
Pre-conditions
    User is able to navigate to the "/signup" URL. User will input a valid username, email, and password and be provided with the requirements for each of those fields in the sgnup form.
Test steps
    1. User can visit the signup page at "/signup"
    2. Provide valid user name (no special characters)
    3. Provide valid email (validated with regex)
    4. Provide valid password (1 each of uppercase, lowercase, number, and special character)
    5. Click Signup button
Expected Result
    User should be able to signup with valid credentials and should be stopped from signup if their credentials are invalid. Once signd up successfully, a user should automatically be logged in and redirected to the trip planner steps in the application.
Actual Result
    -
Status (Pass/Fail)
    -
Notes
    N/A
Post-conditions
    The user's inforation is stored in the database securely, with their password hashed (using bcrypt) before being stored in the DB. The user is notified that their signup was successful and that they are able to start planning their trip.

### 2. Validate Login Functionalty
Use case name
    Verify login with valid user name and password
Description
    Test the "Weekend in Miami - Login" page and user experience
Pre-conditions
    User has valid username and password. A valid username is any string made up of
    alphanumeric letters and avoids special symbols. A valid password is at least 
    8 characters long, includes at least one uppercase and lowercase letter, one 
    number, and one special character.
Test steps
    1. Navigate to login page at "/login"
    2. Provide valid user name (no special characters)
    3. Provide valid password (1 each of uppercase, lowercase, number, and special character)
    4. Click login button
Expected result
    User should be able to login, they should see a confirmation/success message, and be redirected to the trip planner steps in the application.
Actual result
    -
Status (Pass/Fail)
    -
Notes
    N/A
Post-conditions
    User credentials are validated with the database securely and, if they provide the correct login information, are successfully signed into their account. The session details are logged in database and allow the user to access certain restricted areas of the application. After logging in, the user should see some small UI changes (links to newly available pages like a profile, a button to Logout) indicating they are now logged in.

### 3. Validate Logout Functionalty
Use case name
    Verify logout when user clicks the "Logout" button in the navigation bar.
Description
    Test the "Weekend in Miami" logout functionality and user experience
Pre-conditions
    User has a valid, active session on the database and is able to see the "Logout" button in the navigation bar while on any page in the application.
Test steps
    1. Click logout button.
    2. User should be shown a confirmation message that they have logged out and be redirected to the homepage (or any other appropriate page for an unverified user)
    3. A logged out user should not be able to visit certain pages reserved for signed in users.
Expected result
    User should be able to logout, they should see a confirmation/success message, and be redirected to a public page in the application.
Actual result
    -
Status (Pass/Fail)
    -
Notes
    N/A
Post-conditions
    User's session is found in the database and deleted, effectively logging them out from the application and restricting their access to protected resources.