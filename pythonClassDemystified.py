

class Pizza:
	def __init__(self, ingredients):
		self.ingredients = ingredients
		
	def __repr__(self):
		return 'Pizza({self.ingredients})'

	@classmethod
	def margherita(cls):
		return cls(['mozzarella', 'tomatoes'])

	@classmethod
	def prosciutto(cls):
		return cls(['mozzarella', 'tomatoes', 'ham'])

if __name__ == "__main__":
	margherita = Pizza.margherita()
	prosciutto = Pizza.prosciutto()

	print margherita.ingredients
	print repr(margherita)
	print prosciutto.ingredients
