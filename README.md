# django-rest-framework-custom-exceptions
Why do we use it?
If we are not using rest_frameworks exceptions, 
then we will recieve a HTML page as a raised exception.
Instead of that what we want is a exception as a response.
rest_frameworks exceptions are used to map exceptions to response.
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
You can change ValidationError with ParseError, which will lead to a response like this.
```
{
    "detail": "Malformed request.",
    "status_code": 400,
    "myCustomInfo": "Read docs about posting carefully!"
}
```
EDIT: The previous output was a list response of a ValidationError, other errors gives dict response.
Hence, it is better if we convert this list response to a dict response. The code can be changed in custom_exception_handler.
```
dict_response = Response({})
		dict_response.data['detail'] = response.data[0]
		dict_response.data['status_code'] = response.status_code
		dict_response.data['myCustomInfo'] = "Read docs about posting carefully!"
		return dict_response
```
Expected output:
```
{
    "detail": "Invalid input.",
    "status_code": 400,
    "myCustomInfo": "Read docs about posting carefully!"
}
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
