# Empproject
 Employee Management System




Developed and Implemented API Endpoints Using Django Rest Framework (DRF)

Designed and Created API Endpoints: Implemented a RESTful API endpoint for creating employee records using Django Rest Framework (DRF) and APIView. The endpoint supports both HTML form rendering and JSON data handling for creating new employee entries.

Integrated Custom User Model: Utilized Django’s custom Employee model, which extends AbstractBaseUser and PermissionsMixin, to manage employee data, including fields such as email, first_name, last_name, job_title, department, and more.

Form and Serializer Handling: Employed Django’s EmployeeCreationForm for HTML form rendering and handling form submissions. Transitioned to using DRF serializers for API requests to ensure compatibility with JSON data formats and improve data validation and processing.

Implemented Token Authentication: Applied token-based authentication to secure API endpoints, ensuring that only authenticated users can access and manipulate employee data.

Error Handling and Validation: Developed comprehensive error handling to manage validation errors and ensure robust feedback for users when required fields are missing or invalid data is provided.

Permissions and Security: Configured API endpoint permissions to restrict access to authenticated users only, enhancing the security of sensitive employee information.
