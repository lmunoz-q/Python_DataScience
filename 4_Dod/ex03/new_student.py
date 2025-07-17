import random
import string
from dataclasses import dataclass, field

def generate_id() -> str:
    """
    Generate a random identifier composed of 15 lowercase letters.

    Returns:
        str: A string of 15 random lowercase characters.
    """
    return "".join(random.choices(string.ascii_lowercase, k = 15))


@dataclass
class Student:
    """
    Represents a student with a generated login and a unique identifier.

    Attributes:
        name (str): The student's first name.
        surname (str): The student's last name.
        active (bool): Whether the student is currently active (default: True).
        login (str): Automatically generated login.
        First letter of name + full surname, capitalized.
                     Example: name="Edward", surname="agle" → login="Eagle"
                     (42 style)
        id (str): A random 15-character identifier
        generated automatically using generate_id().
        This attribute is not initializable from outside.
    """
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False, repr=True)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        """
        Called automatically after __init__ to set the login attribute
        based on the name and surname of the student.
        """
        self.login = (self.name[0] + self.surname).capitalize()
