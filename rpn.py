#!/usr/bin/env python3

import operator

<<<<<<< HEAD
operators - {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv
=======

operators = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': operator.pow,
>>>>>>> ead13824b87f7518fd2868f1b93abe807edd79d7
}

def calculate(myarg):
	stack = list()
	for token in myarg.split():
		try:
			token = int(token)
			stack.append(token)
		except ValueError:
			function = operators[token]
			arg2 = stack.pop()
			arg1 = stack.pop()
			result = function(arg1, arg2)
			stack.append(result)
<<<<<<< HEAD
	print(stack)
=======
		print(stack)
>>>>>>> ead13824b87f7518fd2868f1b93abe807edd79d7
	if len(stack) != 1:
		raise TypeError("Too many parameters")
	return stack.pop()

def main():
	while True:
		result = calculate(input("rpn calc> "))
		print("Result: ", result)

if __name__ == '__main__':
	main()
<<<<<<< HEAD

=======
>>>>>>> ead13824b87f7518fd2868f1b93abe807edd79d7
