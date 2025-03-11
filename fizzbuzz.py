for i in range(51):
	if(i%3==0 and i%5!=0):
		print(i ,"Fizz")
	elif(i%3!=0 and i%5==0):
		print(i ,"Buzz")
	elif(i%3==0 and i%5==0):
		print(i ,"FizzBuzz")
	else:
		print(i)
