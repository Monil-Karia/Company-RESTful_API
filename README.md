# Company-RESTful_API
This Django REST API project showcases the implementation of a scalable and modular API backend for managing companies and employees, providing CRUD operations and a custom endpoint for retrieving employees of a specific company. It also provides endpoints for managing companies and employees.

## Table of Contents

- [Installation](#Installation)
- [Usage](#Usage)
- [API Endpoints](#API-Endpoints)
- [Contributing](#Contributing)
- [License](#License)

## Installation

1. Clone the repository:
    
    ```
    git clone https://github.com/Monil-Karia/Company-RESTful_API.git
    ```
    
2. Navigate to the project directory:
    
    ```
    cd your-repository
    ```
    
3. Install the required dependencies:
    
    ```
    pip install -r requirements.txt
    ```
    
4. Apply the database migrations:
    
    ```
    python manage.py migrate
    ```
    

## **Usage**

1. Start the development server:
    
    ```
    python manage.py runserver
    ```
    
2. Access the API endpoints locally at **`http://localhost:8000/`**.
3.  **Don't Forget to Make your own superuser.** 

## **API-Endpoints**

- **GET /companies**: Retrieve a list of all companies.
- **POST /companies**: Create a new company.
- **GET /companies/{companyID}**: Retrieve details of a specific company.
- **PUT /companies/{companyID}**: Update details of a specific company.
- **DELETE /companies/{companyID}**: Delete a specific company.
- **GET /companies/{companyID}/employees**: Retrieve employees of a specific company.
- **GET /employees**: Retrieve a list of all employees.
- **POST /employees**: Create a new employee.
- **GET /employees/{employeeID}**: Retrieve details of a specific employee.
- **PUT /employees/{employeeID}**: Update details of a specific employee.
- **DELETE /employees/{employeeID}**: Delete a specific employee.

## **Contributing**

Contributions are welcome! If you find any issues or have suggestions for improvements, please create an issue or submit a pull request.

1. Fork the repository.
2. Create your feature branch:
    
    ```
    git checkout -b feature/your-features
    ```
    
3. Commit your changes:
    
    ```
    git commit -m 'Add your feature'
    
    ```
    
4. Push to the branch:
    
    ```
    git push origin feature/your-feature
    ```
    
5. Open a pull request.

## **License**

This project is licensed under the **[MIT License]((https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt))**.

Feel free to modify and enhance the README file as per your project's requirements.
