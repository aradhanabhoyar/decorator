#### build your own decorator ###
#def my_decorator(func):
#    def wrapper(*arg,**kargs):
#        print("Smart shooping trusted by million")
#        result = func(*arg,**kargs)
#        print("Thank you for visiting this site")
#        return result
#    return wrapper

#@my_decorator
#def Name(name):
#    print(f"Hello Wellcome to this site! {name}")

#Name("Aradhana")


## add two number ##
#def addition(twonumber):
#    def wrapper(a, b):
#        print("Adding the numbers...")
#        result = twonumber(a, b)
#        print(f"Addition of two number is : {result}")
#        return result
#    return wrapper

##short method ##
#@addition
#def add(a, b):
#    return a + b

#add(34,5)

#long method ##
#def add(a, b):
#    return a + b

#decorated_add = addition(add)

#decorated_add(10, 20)

#### add three numbers###
def add_three_no(func):
    def wrapper(a,b):
        print(f"Adding {a} and {b} by using original function")
        result = func(a,b)
        c = 12
        print(f"Now adding the third variable : {c}")
        total = result + c
        print(f"Addition of three number is : {total}")
        return total
    return wrapper

#short method##
#@add_three_no
#def add(a,b):
#    return a + b

#add(11,13)

##long method##
def add(a,b):
    return a + b
addition = add_three_no(add)
addition(8,5)


