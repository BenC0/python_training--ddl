# ------------------------------------------------------------------------------
# Exercise
# 1. Use the below class to define 2 different cars.
# ------------------------------------------------------------------------------

# Exercise
# 1. Use the below class to define 2 different cars and print the description
# message for each car.

# - Car 1 should have the following properties
# 	- name = "Perry"
# 	- color = "red"
# 	- value = "5000.00"

# - Car 2 should have the following properties
# 	- name = "John"
# 	- color = "black"
# 	- value = "1200.49"

class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
