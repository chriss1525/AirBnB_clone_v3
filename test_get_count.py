<<<<<<< HEAD
<<<<<<< HEAD
=======
#!/usr/bin/python3
>>>>>>> ddab3a8ccc69bae4392251f2dc4019c7bf3fc707
=======
#!/usr/bin/python3
>>>>>>> 3e1910784406a73baa2ef096d8da0e16c6dbec33
""" Test .get() and .count() methods
"""
from models import storage
from models.state import State

print("All objects: {}".format(storage.count()))
print("State objects: {}".format(storage.count(State)))

first_state_id = list(storage.all(State).values())[0].id
print("First state: {}".format(storage.get(State, first_state_id)))
