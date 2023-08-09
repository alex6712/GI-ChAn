"""Database Genshin Impact Characters Analyzer Models

A package with descriptions of database entity tables.

It describes the tables of the database used and the interfaces for interacting with them.
"""

from .base import Base
from .character import Character
from .element import Element
from .region import Region
from .user import User
from .user_character import UserCharacter
from .weapon import Weapon
