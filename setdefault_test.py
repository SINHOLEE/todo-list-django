## set_attribute 와 class namespace 공부

dic = {"a":1, "view": 2}

# temp = {"v":"zzz"}
# dic.setdefault("view", 123)
# dic.update(temp)
# print(dic)



class A:
    # class attribute
    __a = 1
    extra_context = None    
    
    # instance attribute
    def __init__(self, value):
        self.some_value = value
        # self.a = 11


    def get_context_data(self, *args, **kwargs):
        print(kwargs)
        print(type(args))
        kwargs.setdefault('view', self)

        if self.extra_context is not None:
            kwargs.update(self.extra_context)
        return kwargs

a_instance = A("instance attribute")

print(A.__a)
# print(a_instance.get_context_data(123, 4, a=1, b=2))
# print(a_instance.get_context_data()['view'].__dict__)  # 인스턴스에서 클래스 어트리뷰트에 접근이 가능하다. 하지만 이렇게 접근하는 방식은 위험하다.
# print("===============================")
# setattr(A, '__a', "asd")
# print(a_instance.__a)
# print(a_instance.__dict__)
# print(A.__a)
# print("===============================")
# a_instance.a = 2 # a_instance name space에 a라는 인스턴스 어트리뷰트를 설정하라는 명령
# print(a_instance.a)
# print(a_instance.__dict__)
# print(A.__a)
# print("===============================")
# setattr(a_instance, 'a', 3)
# print(a_instance.a)
# print(a_instance.__dict__)
# print(A.__a)
# # print(a_instance["some_value"])
# # print(a_instance.get_context_data()['view']['a'])

# a_list = [1,2,3,]
# print(type(a_list))