# django-rest-framework-custom-exceptions
Step. 1
Install virtualenv on your local machine.

Step. 2
In the project directory run following commands
```
mkdir env
cd env
virtualenv .
source bin/activate
cd ..
```
Step. 3
Install all the requirements.
```
pip3 install -r requirements.txt
```

Step. 4
Install the postman and use the following url for posting data
```
localhost:8000/users/
```
specify the input data and type is json
```
{
	"first_name": "ddd",
	"last_name": "fff",
	"email": "som@gmail.com"
}
```
Above data has no username, thus it should returns 400 bad request.
Expected output:
```
[
    "Invalid input."
]
```
# Logic behind this
Reference link 1 - https://github.com/encode/django-rest-framework/blob/master/rest_framework/exceptions.py
Reference link 2 - https://www.django-rest-framework.org/api-guide/exceptions/
1. In views.py of quickstart, in place of ValidationError we can use any exception that are specified in reference link 1.
eg. ParseError, AuthenticationFailed etc.

2. Django uses inbuilt exception_handler, to use custom exception handler as we did, we have to add this into settings.py
```
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'quickstart.utils.custom_exception_handler',
}
```
This will override the defual EXCEPTION_HANDLER which rest_framework uses.

3. In quickstart/utils.py we have to add a custom_exception_handler function which overrides the methods.
Read the comments in that file to understand more of it.
