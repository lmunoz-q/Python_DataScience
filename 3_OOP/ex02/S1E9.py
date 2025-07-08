from abc import ABC, abstractmethod


class Character(ABC):
    """
    Abstract base class representing a generic character.

    Attributes
    ----------
    first_name : str
        The character's first name.
    is_alive : bool
        True if the character is alive, False otherwise.
    """
    def __init__(self, first_name, is_alive=True):
        """
        Initialize a character with a first name and alive status.

        Parameters
        ----------
        first_name : str
            The character's first name.
        is_alive : bool, optional
            Alive status, True by default.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        pass


class Stark(Character):
    """
    Class representing a Stark character, inheriting from Character.
    """
    def __init__(self, first_name, is_alive=True):
        """
        Initialize a Stark character.

        Parameters
        ----------
        first_name : str
            The character's first name.
        is_alive : bool, optional
            Alive status, True by default.
        """
        super().__init__(first_name, is_alive)

    def die(self):
        """
        Mark the character as dead by setting is_alive to False.
        """
        self.is_alive = False
