# get teh super
from Character import Character

# make it a sub
class Vampire(Character):
	def __init__(self):
		super(Vampire,self).__init__('Vampire',15,4)
		# self.name = "Vampire"
		# self.health = 15
		# self.power = 4
	# def take_damage(self,amount_of_damage):
	# 	self.health -= amount_of_damage
	# def get_health(self):
	# 	return self.health
	# def is_alive(self):
	# 	return self.health > 0
	def make_girls_swoon(self):
		print "The skin of the vampire flashes like diamonds in the sunlight. All the girls at Forks High School go berzerk."
		