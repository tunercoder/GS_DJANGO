from django.shortcuts import HttpResponse

class MyMiddleware1:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Initialization for MyMiddleware1")

    def __call__(self, request):
        print("This is before view MyMiddleware1")
        response = self.get_response(request)
        print("This is after view MyMiddleware1")
        return response



class MyMiddleware2:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Initialization for MyMiddleware2")

    def __call__(self, request):
        print("This is before view MyMiddleware2")
        # response = self.get_response(request)
        response =HttpResponse('Nikal lo beech me se hi')
        print("This is after view MyMiddleware2")
        return response

class MyMiddlewar3:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Initialization for MyMiddlewar3")

    def __call__(self, request):
        print("This is before view MyMiddlewar3")
        response = self.get_response(request)
        print("This is after view MyMiddlewar3")
        return response