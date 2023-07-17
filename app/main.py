from app.services.data_provider import DataProvider
from app.services.organizer import organize_data
from app.services.formatter import get_formatted_output


def main():
    """
    You have a list of humans. Every human have "name" and "group".
    Your task is to show all groups, with amount and names of members of each group.
    """
    group_members = DataProvider().generate_group_members()
    organized_data = organize_data(humans=group_members)
    output = get_formatted_output(data=organized_data)
    print(output)

