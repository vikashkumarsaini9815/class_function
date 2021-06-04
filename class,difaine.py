class Person ():
    # how to initialize attributes
    # init method
    def __init__(self,person_name,person_age,person_weight,person_height):
        self.name=person_name
        self.age=person_age
        self.weight=person_weight
        self.height=person_height

person1 = Person("vicky",20,"69 kg" ,"170 cm")
# self = person1

print(person1.name)

person2 = Person("siva",18,"55 kg","159 cm")

print(person2.height)
