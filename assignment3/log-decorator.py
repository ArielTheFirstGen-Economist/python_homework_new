################## TASK 1 ##################

import logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))


def logger_decorator(func):
    def wrapper(*args, **kwargs):
        if args:
            pos_params = args
        else:
            pos_params = "none"
        if kwargs:
            kw_params = kwargs
        else:
            kw_params = "none"

        logger.info(f"function: {func.__name__}")
        logger.info(f"positional parameters:{pos_params}")
        logger.info(f"keyword parameters:{kw_params}")
        result = func(*args, **kwargs)
        logger.info(f"return:{result}")        
        return result
    return wrapper

@logger_decorator
def empty_func():
    print("Hello World")

@logger_decorator
def num_func(*args):
    return True

@logger_decorator
def last_func(**kwargs):
    return logger_decorator

empty_func()
print(num_func(1,2,3))
last_func(name="Mel", color="red")


################## TASK 2 ##################