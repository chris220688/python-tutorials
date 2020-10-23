"""
	Context managers are used when you want to perform some
	tasks before and after executing a block of code.

	They can be implemented either:
		1. as a class, using the __enter__ and __exit__ magic methods,
		2. or as decorators using the contextmanager from the contextlib library.

	Run the following program in a Linux machine:

		python3 context_manager_example.py
"""
from contextlib import contextmanager


class MyContextManager(object):
	""" Context manager implemented as a class """
	def __init__(self):
		print("Initializing context manager A")
	
	def __enter__(self):
		return self
	
	def __exit__(self, type, value, traceback):
		print("Leaving context manager A")

	def print_something(self, text):
		print(text)


@contextmanager
def my_context_manager():
	""" Context manager implemented as a decorator """
	print("Initializing context manager B")

	def print_something(text):
		print(text)

	try:
		yield print_something
	finally:
		print("Leaving context manager B")


if __name__ == "__main__":
	with MyContextManager() as my_ctx:
		my_ctx.print_something('Hello in A!')

	with my_context_manager() as my_ctx:
		my_ctx('Hello in B!')
