from 协程的例子 import stupid_fib
import random
def copy_stupid_fib(n):
	print('I am copy from stupid fib')
	yield from stupid_fib(n)
	print('Copy end')
print('-'*10 + 'test yield from and send' + '-'*10)
N = 20
csfib = copy_stupid_fib(N)
fib_res = next(csfib)
while True:
	print(fib_res)
	try:
		fib_res = csfib.send(random.uniform(0, 0.5))
	except StopIteration:
		break