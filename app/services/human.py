from typing import TypedDict, TypeAlias
from app.config import T_GROUP_NAME


# Define class with keys: name, group
class Human(TypedDict):
    name: str
    group: T_GROUP_NAME


T_HUMANS: TypeAlias = list[Human]
