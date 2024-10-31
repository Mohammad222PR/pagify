from typing import List, Any, Optional

class OffsetPaginator:
    def __init__(self, queryset: List[Any], offset: int = 0, limit: int = 10):
        """
        Initializes the paginator with the dataset, offset, and limit.

        :param queryset: The list of data items (queryset).
        :param offset: The starting index of the items for each page.
        :param limit: The number of items per page.
        """
        self.queryset = queryset
        self.offset = offset
        self.limit = limit

    def get_paginated_data(self) -> List[Any]:
        """
        Returns a slice of the data based on the offset and limit.

        :return: A list of items for the current page.
        """
        return self.queryset[self.offset:self.offset + self.limit]

    def get_next_offset(self) -> Optional[int]:
        """
        Calculates the offset for the next page. Returns None if there is no next page.

        :return: The next offset or None if no more pages are available.
        """
        next_offset = self.offset + self.limit
        return next_offset if next_offset < len(self.queryset) else None

    def get_previous_offset(self) -> Optional[int]:
        """
        Calculates the offset for the previous page. Returns None if there is no previous page.

        :return: The previous offset or None if on the first page.
        """
        return max(0, self.offset - self.limit) if self.offset > 0 else None
