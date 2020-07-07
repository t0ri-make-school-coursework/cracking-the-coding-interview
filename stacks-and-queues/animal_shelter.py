# 3.6
# Animal Shelter
# An animal shelter holds only dogs and cats, and operates on a
# strictly "first in, first out" basis. People must adopt either
# the "oldest" (based on arrival time) of all animals at the
# shelter, or they can select whether they would prefer a dog or
# a cat (and will receive the oldest animal of that type). They
# cannot select which specific animal they would like. Create
# the data structures to maintain this system and implement
# operations such as enqueue, dequeueAny, dequeueDog and dequeueCat.
from LinkedList import LinkedList
from Node import Node


class AnimalShelter:
    def __init__(self):
        self.dogs = LinkedList()
        self.cats = LinkedList()
        self.pets = LinkedList()
    
    def enqueue(self, pet):
        # if animal enqueued is a dog
        if pet.data['animal'] is 'dog':
            # if the dog ll is empty, `pet` is `self.dogs.head`
            if self.dogs.head is None:
                self.dogs.head = pet
            else:
            # if dog ll is not empty, traverse to end of ll
            # to make `pet` the new tail
                node = self.dogs.head
                while node.next is not None:
                    print('i\'m here!')
                    node = node.next
                node.next = pet
            # if pets ll is empty, `pet is self.pets.head`
            if self.pets.head is None:
                self.pets.head = pet
            else:
            # if pets ll is not empty, traverse to end of ll
            # to make `pet` the new tail
                node = self.pets.head
                while node.next is not None:
                    node = node.next
                node.next = pet
        # self.dogs.print_list()
        # self.pets.print_list()
            # add to tail of self.cats or dogs
        # add to tail of self.pets
    
    def dequeueAny(self):
        # remove head from self.pets
        # check head's pet type
            # loop through pet type ll and remove node
        pass

    def dequeueCat(self):
        pass

    def dequeueDog(self):
        pass


if __name__ == "__main__":
    shelter = AnimalShelter()
    lucy = Node({ 'name': 'Lucy', 'animal': 'dog' })
    steve = Node({ 'name': 'Steve', 'animal': 'dog' })
    jo = Node({ 'name': 'Jo', 'animal': 'dog' })
    shelter.enqueue(lucy)
    shelter.enqueue(steve)
    shelter.enqueue(jo)
