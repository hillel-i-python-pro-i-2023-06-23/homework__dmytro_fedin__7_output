import collections
from typing import TypeAlias

T_GROUP: TypeAlias = collections.defaultdict[list[str]]
T_GROUP_NAME: TypeAlias = str
T_GROUP_NAMES: TypeAlias = list[T_GROUP_NAME]
