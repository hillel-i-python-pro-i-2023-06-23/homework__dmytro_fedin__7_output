import collections
from collections import defaultdict
from typing import TypeAlias

from app.services.human import T_HUMANS

T_GROUP: TypeAlias = collections.defaultdict[list[str]]


def organize_data(humans: T_HUMANS) -> T_GROUP:
    """
    Use default-dict object to organized data
    """
    grouped_data = defaultdict(list)

    for item in humans:
        group = item['group']
        name = item['name']
        grouped_data[group].append(name)

    return grouped_data
