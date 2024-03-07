class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type. Must be one of: " + ", ".join(self.PET_TYPES))
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.all.append(self)

    def set_owner(self, owner):
        if not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of Owner class.")
        self.owner = owner

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        return self._pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Only instances of Pet class can be added as pets.")
        self._pets.append(pet)
        pet.set_owner(self)

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)
