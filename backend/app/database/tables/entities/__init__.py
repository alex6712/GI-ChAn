"""Database Genshin Impact Characters Analyzer Entities Models

A package with descriptions of database entity tables.

It describes the tables of the database used and the interfaces for interacting with them.
"""

from .artifact import Artifact, Set, Stat
from .character import Character, Element, Region, Weapon
from .user import User
