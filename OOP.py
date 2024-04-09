class Person:
    """A class representing a person with name, age, and gender attributes."""

    # Class attribute (shared by all Person instances)
    species = "Homo Sapiens"  

    def __init__(self, name, age, gender):
        """
        Initializes a Person object with instance attributes.

        Args:
            name (str): The person's name.
            age (int): The person's age (optional, can be calculated from birth year).
            gender (str): The person's gender (optional).
        """
        self.name = name
        self.age = age
        self.gender = gender if gender else "Male"

    @classmethod
    def from_birth_year(cls, name, birth_year,):
        """
        Creates a Person object from a birth year, calculating the age.

        Args:
            name (str): The person's name.
            birth_year (int): The person's birth year.

        Returns:
            Person: A Person object with calculated age.
        """
        age = 2024 - birth_year
        return cls(name, age, None)  # Gender can be provided if known

    def introduce(self):
        """
        Prints a message introducing the person with their name, age, and gender.
        """
        age_str = "unknown" if self.age is None else str(self.age)
        gender_str = "unknown" if self.gender is None else self.gender
        print(f"Hello! Let's put our hands together and welcome {self.name}, a bright {gender_str}, {age_str} years old.") 

# Create Person instances
israel = Person("Isra", 27, "Male")
israel2 = Person.from_birth_year("Isra", 1997,)  

# Call the introduce method on both instances
israel.introduce()
israel2.introduce()

