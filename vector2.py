import math

# -------------------------------------------------------------------------------

class Vector2:
	def __init__(self, arr):
		self.x = arr[0]
		self.y = arr[1]


	def Vget(self):
		return Vector2((self.x, self.y))

	def Aget(self):
		return self.x, self.y


	def Vset(self, vec):
		self.x = vec.x
		self.y = vec.y

	def Aset(self, arr):
		self.x = arr[0]
		self.y = arr[1]

	def set(self, x, y):
		self.x = x
		self.y = y


	def Vadd(self, vec):
		self.x += vec.x
		self.y += vec.y

	def Aadd(self, arr):
		self.x += arr[0]
		self.y += arr[1]

	def add(self, num):
		self.x += num
		self.y += num


	def Vsub(self, vec):
		self.x -= vec.x
		self.y -= vec.y

	def Asub(self, arr):
		self.x -= arr[0]
		self.y -= arr[1]

	def sub(self, num):
		self.x -= num
		self.y -= num


	def Vmult(self, vec):
		self.x *= vec.x
		self.y *= vec.y

	def Amult(self, arr):
		self.x *= arr[0]
		self.y *= arr[1]

	def mult(self, num):
		self.x *= num
		self.y *= num


	def Vdiv(self, vec):
		self.x /= vec.x
		self.y /= vec.y

	def Adiv(self, arr):
		self.x /= arr[0]
		self.y /= arr[1]

	def div(self, num):
		self.x /= num
		self.y /= num


	def rounding(self, num):
		self.x = round(self.x, num)
		self.y = round(self.y, num)

	def setMag(self, length):
		self.normalize()
		self.mult(length)

	def Vdist(self, vec):
		return math.sqrt( (self.x - vec.x)**2 + (self.y - vec.y)**2 )

	def from_angle(self, angle, length=1):
		radians = angle*math.pi/180
		return Vector2((length * math.sin(radians), length * math.cos(radians)))

	def Vdetermine_direction(self, vec):
		self.set( abs(self.x) - abs(vec.x), abs(self.y) - abs(vec.y) )

	def mag(self):
		return math.sqrt( self.x**2 + self.y**2 )

	def magSq(self):
		return ( self.x**2 + self.y**2 )

	def normalize(self):
		max_ = self.mag()
		if ( max_ != 0 and max_ != 1 ):
			self.div(max_)

	def limit(self, max_):
		if ( self.magSq() > max_**2 ):
			self.normalize()
			self.mult(max_)