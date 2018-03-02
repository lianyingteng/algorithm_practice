"""猫狗队列

	左程云<程序员代码面试指南> 第10页
"""
class Pet(object):

	def __init__(self, typeName):
		self.typeName = typeName

	def getPetType(self):
		return self.typeName

class Dog(Pet):

	def __init__(self):
		super(Dog, self).__init__("Dog")

class Cat(Pet):

	def __init__(self):
		super(Cat, self).__init__("Cat")

#########################################
"""解决方法：定义一个新的类给每一个实例盖上一个时间戳"""
class PetEnterQueue(object):

	def __init__(self, pet, count):

		self.pet = pet
		self.count = count

	def getPet(self):
		return self.pet

	def getCount(self):
		return self.count

	def getEnterPetType(self):
		return self.pet.getPetType()

                                                                                         
class CatDogQueue(object):

	def __init__(self):
		self.qCat = []
		self.qDog = []
		self.count = 0

	def add(self, pet):
		if pet.getPetType() == "Dog":
			self.count += 1
			self.qDog.append(PetEnterQueue(pet, self.count))
		elif pet.getPetType() == "Cat":
			self.count += 1
			self.qCat.append(PetEnterQueue(pet, self.count))
		else:
			raise TypeError("Not Cat Or Dog!")

	def isEmpty(self):
		return len(self.qCat) == 0 and len(self.qDog) == 0

	def isDogEmpty(self):
		return len(self.qDog) == 0

	def isCatEmpty(self):
		return len(self.qCat) == 0

	def pollAll(self):
		if not self.isDogEmpty() and not self.isCatEmpty():
			if self.qCat[0].getCount() < self.qDog[0].getCount():
				return self.qCat.pop(0).getPet()
			else:
				return self.qDog.pop(0).getPet()
		elif not self.isDogEmpty():
			return self.qDog.pop(0).getPet()
		elif not self.isCatEmpty():
			return self.qCat.pop(0).getPet()
		else:
			raise IndexError("The queue is empty!")

	def pollDog(self):
		if not self.isDogEmpty():
			return self.qDog.pop(0).getPet()
		else:
			raise IndexError("The dog queue is empty!")

	def pollCat(self):
		if not self.isCatEmpty():
			return self.qCat.pop(0).getPet()
		else:
			raise IndexError("The cat queue is empty!")



