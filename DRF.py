"""
Django REST Framework (DRF) is a powerful toolkit that enables developers to build and customize web APIs using the Django web framework. It is an open-source project that provides a set of reusable components for building RESTful web APIs.

DRF builds on top of Django and provides additional features and tools that make it easier to develop web APIs, such as serialization, authentication, and content negotiation. With DRF, developers can quickly build robust APIs that follow best practices for RESTful design.

Some key features of DRF include:

Serialization: DRF provides a powerful serialization engine that can convert complex data structures such as Django models into simple data formats like JSON or XML.

Authentication and permissions: DRF includes built-in support for authentication and permissions, enabling developers to control access to API endpoints based on user authentication and authorization.

Views: DRF provides a set of generic views that can be used to handle common use cases, such as retrieving lists of objects, creating, updating, or deleting objects.

API documentation: DRF includes a built-in web-based interface for API documentation that can be automatically generated from the API code.

Testing: DRF provides a set of tools for testing web APIs, including a test client and a test framework for testing the correctness of API endpoints.

Overall, DRF is a comprehensive toolkit that streamlines the development of web APIs using Django, allowing developers to focus on building high-quality APIs that are easy to use and maintain. It is widely used in production environments and is recommended by the Django community for building RESTful APIs.
"""

"""
RESTful web APIs are a type of web API that follows the principles of Representational State Transfer (REST) architecture. REST is a set of architectural principles that provide a standard way of designing web services that can be easily accessed and manipulated by clients over the internet.

In a RESTful web API, the server exposes a set of resources, each of which is identified by a unique URI (Uniform Resource Identifier). These resources can be manipulated by clients using a set of standard HTTP methods, such as GET, POST, PUT, PATCH, and DELETE. The HTTP methods are used to perform operations on the resources, such as retrieving, creating, updating, or deleting resources.

One of the key principles of RESTful web APIs is that they are stateless, meaning that the server does not maintain any client state between requests. Instead, each request is self-contained and includes all the information necessary for the server to process the request and return a response.

Another important principle of RESTful web APIs is that they are resource-oriented, meaning that they focus on the resources that the API exposes, rather than the actions that can be performed on those resources. This makes RESTful APIs more flexible and easier to understand than traditional RPC (Remote Procedure Call) style APIs.

RESTful web APIs also make use of standard formats for representing data, such as JSON (JavaScript Object Notation) or XML (eXtensible Markup Language). This makes it easier for clients to consume the API and reduces the amount of code that needs to be written to handle the data.

Overall, RESTful web APIs provide a standard and flexible way of building web services that can be easily accessed and consumed by clients over the internet. They are widely used in modern web development and are recommended for building APIs that are easy to use, scalable, and maintainable.
"""

# Steps:
# 1. Create folder with name for the project 
# 2. Create virtual environment $python3 -m venv drf-env
# 3. Activate virtual environment $source drf-env/bin/activate
# install Django $pip install django
# 5. install DRF $pip install djangorestframework
# 6. on settings.py add app: 'rest_framework', 
# 7. Create new folder on route directory of the project call it api. Create ___init__.py file and views.py file
