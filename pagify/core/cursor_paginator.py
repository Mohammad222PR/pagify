from typing import Optional, List, Union

class CursorPaginator:
    def __init__(self, queryset: List[dict], cursor: Optional[Union[int, str]] = None, limit: int = 10):
        """
        Initializes the paginator with a dataset, cursor, and limit.

        :param queryset: The dataset, typically a list of dictionaries with an 'id' field.
        :param cursor: The id of the last item from the previous page to continue pagination.
        :param limit: The number of items per page.
        """
        self.queryset = queryset
        self.cursor = cursor
        self.limit = limit

    def get_paginated_data(self) -> List[dict]:
        """
        Retrieves a slice of the data based on the cursor and limit.

        :return: A list of items for the current page.
        """
        if self.cursor is not None:
            return [item for item in self.queryset if 'id' in item and item['id'] > self.cursor][:self.limit]
        return self.queryset[:self.limit]

    def get_next_cursor(self, data: List[dict]) -> Optional[Union[int, str]]:
        """
        Determines the next cursor based on the last item of the current data.

        :param data: The list of items from the current page.
        :return: The id of the last item in the data to be used as the cursor for the next page, or None if empty.
        """
        return data[-1]['id'] if data and 'id' in data[-1] else None
