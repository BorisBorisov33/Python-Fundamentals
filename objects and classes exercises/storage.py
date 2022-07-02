# for one object works good only
class Storage:
    storage = []

    def __init__(self, capacity: int):
        self.capacity = capacity

    def add_product(self, product: str):
        # if self.capacity > 0:
        #     Storage.storage.append(product)
        #     self.capacity -= 1
        if len(Storage.storage) < self.capacity:
            Storage.storage.append(product)

    def get_products(self):
        return Storage.storage

# for more than one object
# class Storage:
#     storage = []
#
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#
#     def add_product(self, product: str):
#       if self.capacity > 0:
#           Storage.storage.append(product)
#           self.capacity -= 1
#
#
#     def get_products(self):
#         return self.storage
#
