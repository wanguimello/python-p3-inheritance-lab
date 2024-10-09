#!/usr/bin/env python

import random
from user import User  # Make sure to import User class

knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)  # Call the parent constructor
        self.knowledge = knowledge  # Store knowledge strings in an attribute

    def teach(self):
        index = random.randint(0, len(self.knowledge) - 1)  # Get a random index
        return self.knowledge[index]  # Return a random knowledge string
