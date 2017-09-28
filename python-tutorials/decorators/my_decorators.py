#! python3
# my_decorators.py
# Thanks so much Corey Schafer for the great explanation
# https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g


# step 1
def outher_function(msg):
    message = msg

    def inner_function():
        print(msg)
    return inner_function

hi_func = outher_function("Hi")  
bue_func = outher_function("Bye")

# hi_func()
# bue_func()    


#step2
def decorator_func(original_func):
    def  wrapper_func(*args, **kwargs):
    	print('wrapper executed this before {}'.format(original_func.__name__))
    	return original_func(*args, **kwargs)
    return wrapper_func

@decorator_func # the same - display = decorator_func(display)
def display():
    print('display function ran')

#display()

@decorator_func
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age)) 

# display_info('Dasha', 22)          

# step 3 Class's Decorators
class DecoratorClass(object):
    
    def __init__(self, original_func):
        self.original_func = original_func

    def __call__(self, *args, **kwargs):
        print('call method executed this before {}'.format(self.original_func.__name__))
        return self.original_func(*args, **kwargs)


@DecoratorClass # the same - display = decorator_func(display)
def display():
    print('display function ran')

# display()

@DecoratorClass
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age)) 

# display_info('Dasha', 22)              


# step 4: logger and timer
def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper
    

def my_timer(orig_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper        


@my_logger
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age)) 


#display_info('Dasha', 22)

import time

@my_timer
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name, age)) 


#display_info('Andrew', 24)      