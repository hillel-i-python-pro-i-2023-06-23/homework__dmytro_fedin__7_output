from collections import defaultdict

from app.config import T_GROUP
from app.services.human import T_HUMANS


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
