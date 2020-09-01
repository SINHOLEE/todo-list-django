class A:
    def __init__(self):
        self.a = 123
    
    
    def dummy_dispatch(self, request):
        handler =  getattr(self, 'post', self.test_method)
        return handler(request)
    
    def test_method(self, request):
        return "t_m"
    
    def post(self, request):
        return "post" + request
a_instance = A()

print(a_instance.a)

print(a_instance.dummy_dispatch("ccc"))