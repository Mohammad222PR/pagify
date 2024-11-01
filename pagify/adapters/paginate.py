from typing import List, Any, Optional
from pagify import OffsetPaginator, CursorPaginator, PageNumberPaginator
from pagify.utils.response_formatting import JSONResponseFormatter
from pagify.utils.serializer import Serializer


def paginate_with_offset(queryset: List[Any], offset: int, limit: int) -> str:
    paginator = OffsetPaginator(queryset, offset, limit)
    data = Serializer.serialize(paginator.get_paginated_data())

    return JSONResponseFormatter.paginate(
        data=data,
        pagination_info={
            "next_offset": paginator.get_next_offset(),
            "previous_offset": paginator.get_previous_offset(),
            "limit": limit
        },
        message="Offset pagination results"
    )


def paginate_with_cursor(queryset: List[Any], cursor: Optional[int], limit: int) -> str:
    paginator = CursorPaginator(queryset, cursor, limit)
    data = Serializer.serialize(paginator.get_paginated_data())

    return JSONResponseFormatter.paginate(
        data=data,
        pagination_info={
            "cursor": cursor,
            "next_cursor": paginator.get_next_cursor(data),
            "limit": limit
        },
        message="Cursor pagination results"
    )


def paginate_with_page_number(queryset: List[Any], page: int, page_size: int) -> str:
    paginator = PageNumberPaginator(queryset, page, page_size)
    data = Serializer.serialize(paginator.get_paginated_data())

    return JSONResponseFormatter.paginate(
        data=data,
        pagination_info={
            "current_page": page,
            "next_page": paginator.get_next_page(),
            "previous_page": paginator.get_previous_page(),
            "page_size": page_size
        },
        message="Page number pagination results"
    )
