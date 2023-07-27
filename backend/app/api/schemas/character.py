from uuid import UUID

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    field_validator,
)
from pydantic_extra_types.phone_numbers import PhoneNumber


class CharacterSchema(BaseModel):
    """Scheme of the character object.

    Used to represent base (general) character information.

    Attributes
    ----------
    id : UUID
        Character's UUID.
    name : str
        Character's name.
    legendary : bool
        If character is five stars, this flag is True, False otherwise.
    weapon : str
        Character's weapon type.
    element : PhoneNumber
        Character's element.
    region : str
        Character's nation.
    """

    model_config = ConfigDict(from_attributes=True)

    id: UUID = Field(example="7a0fac1b-0ff6-46ab-906b-a4eb173bce21")
    name: str = Field(example="Эмбер")
    legendary: bool = Field(example=False)
    weapon: str = Field(example="Стрелковое")
    element: str = Field(example="Пиро")
    region: str = Field(example="Мондштадт")


class UserCharacterSchema(BaseModel):
    """Scheme of the user_character object.

    Used to represent specific user's character information.

    Attributes
    ----------
    id : UUID
        Character's UUID.
    level : int
        Character's level (1-90).
    constellations : int
        The number of character's constellations (1-6).
    attack_level : int
        Character's attack level (1-10).
    skill_level : int
        Character's elemental skill level (1-10).
    burst_level : int
        Character's elemental burst level (1-10).
    """

    model_config = ConfigDict(from_attributes=True)

    id: UUID = Field(example="7a0fac1b-0ff6-46ab-906b-a4eb173bce21")
    level: int = Field(example=90)

    @classmethod
    @field_validator("level", mode="before")
    def check_character_level_interval(cls, value: int) -> int:
        if 1 <= value <= 90:
            return value

        raise ValueError(value)

    constellations: int = Field(example=3)

    @classmethod
    @field_validator("constellations", mode="before")
    def check_constellations_interval(cls, value: int) -> int:
        if 1 <= value <= 6:
            return value

        raise ValueError(value)

    attack_level: int = Field(example=1)
    skill_level: int = Field(example=6)
    burst_level: int = Field(example=6)

    @classmethod
    @field_validator("attack_level", "skill_level", "burst_level", mode="before")
    def check_skill_level_interval(cls, value: int) -> int:
        if 1 <= value <= 10:
            return value

        raise ValueError(value)


class FullCharacterSchema(CharacterSchema, UserCharacterSchema):
    """Scheme of the full character object (union of ``character`` and ``user_character``).

    Used to represent full character information.

    See Also
    --------
    CharacterSchema
    UserCharacterSchema
    """
