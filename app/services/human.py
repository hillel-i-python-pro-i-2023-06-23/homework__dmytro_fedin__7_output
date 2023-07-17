# Define class with keys: name, group
from typing import TypedDict, TypeAlias

from app.config import T_GROUP_NAME


class Human(TypedDict):
    name: str
    group: T_GROUP_NAME


