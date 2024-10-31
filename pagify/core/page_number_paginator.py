from typing import List, Any, Optional

class PageNumberPaginator:
    def __init__(self, queryset: List[Any], page: int = 1, page_size: int = 10):
        """
        Initializes the paginator with the dataset, page number, and page size.

        :param queryset: The list of data items (queryset).
        :param page: The current page number.
        :param page_size: The number of items per page.
        """
        self.queryset = queryset
        self.page = page
        self.page_size = page_size

    def get_paginated_data(self) -> List[Any]:
        """
        Returns a slice of the data based on the page and page size.

        :return: A list of items for the current page.
        """
        start = (self.page - 1) * self.page_size
        return self.queryset[start:start + self.page_size]

    def get_next_page(self) -> Optional[int]:
        """
        Calculates the next page number. Returns None if there is no next page.

        :return: The next page number or None if no more pages are available.
        """
        if (self.page * self.page_size) < len(self.queryset):
            return self.page + 1
        return None

    def get_previous_page(self) -> Optional[int]:
        """
        Calculates the previous page number. Returns None if there is no previous page.

        :return: The previous page number or None if on the first page.
        """
        return self.page - 1 if self.page > 1 else None
