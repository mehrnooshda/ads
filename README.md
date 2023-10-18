# Advertisement Posting and Commenting System

## Table of Contents
- [Business Specification](#business-specification)
- [Technical Specification](#technical-specification)
- [Setup](#setup)
  - [PostgreSQL Setup](#postgresql-setup)
- [Usage](#usage)
  - [Authentication](#authentication)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [OpenAPI Specification](#openapi-specification)
- [Contributing](#contributing)
- [License](#license)

---

## Business Specification

The Advertisement Posting and Commenting System is designed to enable users to post Ads and comment on other people's Ads. Here are the key business specifications:

1. **User Authentication**: Users are required to be authenticated to perform actions like adding Ads and comments.
2. **User Registration**: Users can register with a unique email as their username and password.
3. **Commenting Limit**: Each user can comment on an Ad just once.
4. **Public Access**: Users can view Ads and their related comments without being logged in to the system.
5. **Ad Management**: Users have the ability to delete and edit their own Ads.

## Technical Specification

The technical specifications for this project are as follows:

1. **RESTful API**: The system is implemented as a RESTful API using one of the popular Python web frameworks such as Django, Flask, or FastAPI, with no requirement for a UI.
2. **Database**: PostgreSQL is used as the database to store user data, Ads, and comments.
3. **ORM (Object-Relational Mapping)**: An ORM is employed to interact with the database.
4. **Testing**: Unit tests are written to ensure the reliability of the APIs.
5. **OpenAPI Specification**: The API endpoints are documented using the OpenAPI Specification.
6. **README**: A comprehensive README file is provided for setting up and running the project.

### PostgreSQL Setup

To set up PostgreSQL, follow these steps:

1. Open your PostgreSQL terminal:

   ```bash
   sudo -u postgres psql
   ```

2. Create a user named "mehrnooch" with a password (replace 'miloo123456' with your preferred password):

   ```sql
   CREATE USER mehrnooch WITH PASSWORD 'miloo123456';
   ```

3. Create a database named "urlhasher" with "mehrnooch" as the owner and encoding set to 'UTF8':

   ```sql
   CREATE DATABASE urlhasher WITH OWNER mehrnooch ENCODING 'UTF8';
   ```
### Setup Virtualenv
Use the contents of example.env and copy that into a file named .env in the route directory of the project and replace 
it with your own specifications if needed. 

To use the API, follow these guidelines:

### Authentication

1. After calling the login API, retrieve the token from the response.
2. Put the token in the `Authorization` header of APIs that require authorization.

## API Endpoints

The API endpoints are documented using the OpenAPI Specification. Refer to the API documentation for details on available endpoints, request formats, and responses.

## Testing

To run the unit tests for the project, use the following command:

```bash
python manage.py test
```

Make sure all tests pass successfully.

## OpenAPI Specification

The OpenAPI Specification documentation provides a structured and comprehensive reference for the project's API endpoints. It's crucial for understanding the structure and functionality of the API.

## Contributing

Contributions from the open-source community are welcome. To contribute to this project, please follow the provided guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and ensure they pass the existing tests.
4. Document any new endpoints or features in the OpenAPI Specification.
5. Create a pull request with a clear description of the changes.

## License

This project is licensed under the [License Name] License. Please refer to the [LICENSE.md](LICENSE.md) file for details.