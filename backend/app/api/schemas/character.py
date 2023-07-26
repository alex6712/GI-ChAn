from pydantic import (
    BaseModel,
    Field,
    field_validator,
)
from pydantic_extra_types.phone_numbers import PhoneNumber


class CharacterSchema(BaseModel):
    """Scheme of the character object.

    Used to represent base (general) character information.

    Attributes
    ----------
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
    level: int = Field(example=90)

    @classmethod
    @field_validator("level", mode="before")
    def check_character_level_interval(cls, v: int) -> int:
        if 1 <= v <= 90:
            return v

        raise ValueError(v)

    constellations: int = Field(example=3)

    @classmethod
    @field_validator("constellations", mode="before")
    def check_constellations_interval(cls, v: int) -> int:
        if 1 <= v <= 6:
            return v

        raise ValueError(v)

    attack_level: int = Field(example=1)
    skill_level: int = Field(example=6)
    burst_level: int = Field(example=6)

    @classmethod
    @field_validator("attack_level", "skill_level", "burst_level", mode="before")
    def check_skill_level_interval(cls, v: int) -> int:
        if 1 <= v <= 10:
            return v

        raise ValueError(v)


class FullCharacterSchema(CharacterSchema, UserCharacterSchema):
    """Scheme of the full character object (union of ``character`` and ``user_character``).

    Used to represent full character information.

    See Also
    --------
    CharacterSchema
    UserCharacterSchema
    """
    pass
