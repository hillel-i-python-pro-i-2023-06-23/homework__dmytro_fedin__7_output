# Define class with keys: name, group
from typing import TypedDict, TypeAlias

T_GROUP_NAME: TypeAlias = str
T_GROUP_NAMES: TypeAlias = list[T_GROUP_NAME]


class Human(TypedDict):
    name: str
    group: T_GROUP_NAME


T_HUMANS: TypeAlias = list[Human]



