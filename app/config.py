import pathlib

from typing import Final, TypeAlias
from app.services.human import Human

# Set directories to get services.
ROOT_DIR: Final[pathlib.Path] = pathlib.Path(__file__).parents[1]

# Set alias
T_GROUP_NAME: TypeAlias = str
T_GROUP_NAMES: TypeAlias = list[T_GROUP_NAME]
T_HUMANS: TypeAlias = list[Human]