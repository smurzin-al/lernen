import math
def print_in_grad_rad(grads,mins,secs):
	# """
 # 	возвращает десятичные градусы
 # 	grad значение градусов
 # 	min значение минут, если не заданы то ноль
 # 	sec значение секунд, есди не заданы то ноль
 # 	"""
 	grads=int(grads)
 	mins=int(mins)
 	secs=int(secs)
 	value_grad= (grads + mins/60 + secs/3600)
 	value_rad=value_grad*math.pi/180
 	print(grads,'°',mins, "'",secs, "'' =",value_grad,'°')
 	print(grads,'°',mins, "'",secs, "'' =",value_rad,'rad')

print('Функция перевода из градусов минут секунд в десятичные градусы и радианы') 
while(1):	
	i=0
	while i==0:
		inp_grad = input("\nВведи значение градусов: ")
		try:
			inp_grad=int(inp_grad)
			if inp_grad<=360 and inp_grad>=-360:
				i=1
			else: print('Ошибка ввода. Допустимый диапазон -360..360')
		except ValueError:
			print('Ошибка ввода, введи число')

	i=0
	while i==0:
		inp_min = input("Введи значение минут: ")
		try:
			inp_min=int(inp_min)
			if inp_min<=59 and inp_min>=0:
				i=1
			else: print('Ошибка ввода. Допустимый диапазон 0..59')
		except ValueError:
			print('Ошибка ввода, введи число')

	i=0
	while i==0:
		inp_sec = input("Введи значение секунд: ")
		try:
			inp_sec=int(inp_sec)
			if inp_sec<=59 and inp_sec>=0:
				i=1
			else: print('Ошибка ввода. Допустимый диапазон 0..59')
		except ValueError:
			print('Ошибка ввода, введи число')

	print('Расчитанные значения на основании введенных')
	print_in_grad_rad(inp_grad,inp_min,inp_sec)


