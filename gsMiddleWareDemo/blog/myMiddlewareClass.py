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

    def process_view(request,*args, **kwargs):
        print('in process_view before view middle ware will execute this')
        return None
        # return HttpResponse("this is response from process view hook no further view will be called")



class MyMiddleware2:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Initialization for MyMiddleware2")

    def __call__(self, request):
        print("This is before view MyMiddleware2")
        response = self.get_response(request)
        # response =HttpResponse('Nikal lo beech me se hi') if returns then no further processing is done if none passed on to next
        print("This is after view MyMiddleware2")
        return response
    
    def process_exception(self,request,exception):
        msg=exception
        print('when exception happens in view this code will run')
        return None
        # return HttpResponse(msg)


class MyMiddlewar3:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Initialization for MyMiddlewar3")

    def __call__(self, request):
        print("This is before view MyMiddlewar3")
        response = self.get_response(request)
        print("This is after view MyMiddlewar3")
        return response

    def process_template_response(self,request,response):
        print("MyMiddlewar3 :: process_template_response ")
        response.context_data['name']='Delhi'
        return response
