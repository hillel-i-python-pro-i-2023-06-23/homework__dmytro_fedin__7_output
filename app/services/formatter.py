from app.config import T_GROUP


def get_formatted_output(data: T_GROUP) -> str:
    """
    Get output string, that can be used to print in console.
    """
    formatted_output = ''

    for group, names in data.items():
        formatted_output += f"Group: {group} - "
        formatted_output += f"Members: {', '.join(names)}\n"

    return formatted_output
