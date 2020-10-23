"""
	Decorators are just functions that wrap other functions.
	For example, they take function 'my_func' as an argument,
	do something and then return function 'my_func' back.

	Run the following program in a Linux machine:

		python3 decorator_example.py
"""
import functools


def my_decorator(func):
	""" Decorator function """
	print("Doing some stuff here..")

	@functools.wraps(func)
	def wrapper(*args, **kwargs):
		return func(*args, **kwargs)

	# Return the original function wrapped
	return wrapper


@my_decorator
def my_func(p1, p2):
	""" Decorated function """
	return p1, p2


if __name__ == "__main__":
	p1, p2 = my_func('param1', 'param2')
	print(f"my_func returned {p1}, {p2} as expected!")
