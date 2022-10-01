from functools import update_wrapper, partial

def power(a, b):
	''' a to the power b'''
	return a**b

# partial function
pow2 = partial(power, b = 2)
pow2.__doc__='''a to the power 2'''
pow2.__name__ = 'pow2'

print('Before wrapper update -')
print('Documentation of pow2 :', pow2.__doc__)
print('Name of pow2 :', pow2.__name__)
print()
update_wrapper(pow2, power)
print('After wrapper update -')
print('Documentation of pow2 :', pow2.__doc__)
print('Name of pow2 :', pow2.__name__)
