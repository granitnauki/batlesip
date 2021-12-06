import random

5
class Field(object):
	"""docstring for Field"""
	def __init__(self, field):
		super(Field, self).__init__()
		#инициализируем игровое поле
		self.__cells__ = field
		

	
	#получаем свободные клетки поля
	def get_free_cells(self):
		free = []
		for i in range(6):
			for j in range(6):
				if self.__cells__[i][j] != 'X' and self.__cells__[i][j] != 'V' and self.__cells__[i][j] != 'T' :
					free.append([i,j])
		return free

	#функция вывода поля
	def print(self):
		print(' | 1| 2| 3| 4| 5| 6|')
		print('--------------------')
		for i in range(6):
			print(str(i + 1) + '|', end='')
			for j in range(6):
				print(self.__cells__[i][j], end=' |')
			print()

	#функция выстрела
	def shot(self, other, x, y):
		if (x > 6 or x < 1) or (y > 6 or y < 1):
			print('Некорректные координаты выстрела!')
			return False
		if (other.get(x - 1, y - 1) == True):
			print('Есть попадание!')
			other.set(x - 1, y - 1, 'X')
			return True
		else:
			print('Мимо...')
			other.set(x - 1, y - 1, 'T')
			return True

	#функция для компютера
	def shot_comp(self, other):
		free = other.get_free_cells()
		cell = random.choice(free)
		print('X: ' + str(cell[0] + 1))
		print('Y: ' + str(cell[1] + 1))
		if (other.get(cell[0], cell[1]) == True):
			print('Есть попадание!')
			other.set(cell[0], cell[1], 'X')
			return True
		else:
			print('Мимо...')
			other.set(cell[0], cell[1], 'T')
			return False

	def set(self, x, y, val):
		self.__cells__[x][y] = val

	def get(self, x, y):
		if self.__cells__[x][y] == 'V':
			return True
		else :
			return False

	def get_ships(self):
		ships = []
		for i in range(6):
			for j in range(6):
				if self.__cells__[i][j] == 'V' :
					ships.append([i,j])
		return ships

def main():
	user = Field([
		['O','O','O', 'V','V','V'],
		['V','V','O', 'O','O','O'],
		['O','O','O', 'V','O','V'],
		['V','V','O', 'O','O','O'],
		['O','O','O', 'O','O','O'],
		['O','V','O', 'V','O','O']
		])
	#user.print()

	comp = Field([
		['O','O','O', 'O','V','O'],
		['V','V','O', 'O','O','O'],
		['O','O','O', 'V','V','V'],
		['O','O','V', 'O','O','O'],
		['O','O','O', 'O','O','V'],
		['O','V','O', 'V','V','O']
		])

	#comp.print()

	print('Игра началась!')
	print('==============')
	while True:
		print()
		print('Ваше поле')
		user.print()
		print()
		print('Поле компьютера')
		comp.print()
		print()

		print('Ваш ход:')
		x = int(input('X: '))
		y = int(input('Y: '))
		user.shot(comp, x, y) 

		print()
		print('Ход компьютера:')
		comp.shot_comp(user)

		if user.get_ships() == []:
			print('Вы проиграли...')
			break
		if comp.get_ships() == []:
			print('Вы выиграли!')
			break
	input('Нажмите Enter для выхода...')

if __name__ == '__main__':
	main()