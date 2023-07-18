# import pathlib
#
# from typing import Final
#
# # Set directories to get services.
# ROOT_DIR: Final[pathlib.Path] = pathlib.Path(__file__).parents[1]
import collections
from typing import TypeAlias

T_GROUP: TypeAlias = collections.defaultdict[list[str]]
