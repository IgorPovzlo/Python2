def print_log(function):

	def wrapper():
		print(function.__name__, "Исполнена. Результат:")
		res = function
		return res
	return wrapper()



@print_log
def some_func(x, y):
	return x * y


print(some_func(4, 6))
print(some_func(10, -5))