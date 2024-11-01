# API Reference for Pagify Package

This document serves as a complete reference for the available classes, methods, and utilities in the **Pagify** package. It helps developers use the package effectively for adding pagination to Python applications.

## Core Modules

### `core.pagination`

The main module containing functions for paginating different data structures and query sets.

#### Key Functions


- **`paginate_with_page_number(data: List[Any], page: int, page_size: int) -> Dict[str, Any]`**
  - Paginates the given list based on the page number method.
  - **Parameters**:
    - `data` (List[Any]): The data to be paginated.
    - `page` (int): The current page number (1-indexed).
    - `page_size` (int): The number of items per page.
  - **Returns**: A dictionary with `data` and `meta` keys, containing the paginated data and metadata.


- **`paginate_with_offset(data: List[Any], offset: int, limit: int) -> Dict[str, Any]`**
  - Implements offset-based pagination.
  - **Parameters**:
    - `data` (List[Any]): The data to be paginated.
    - `offset` (int): The starting position in the data.
    - `limit` (int): The number of items to display.
  - **Returns**: A dictionary with `data` and `meta` keys, containing the paginated data and metadata.


- **`paginate_with_cursor(data: List[Any], cursor: str, limit: int) -> Dict[str, Any]`**
  - Cursor-based pagination for navigating large datasets efficiently.
  - **Parameters**:
    - `data` (List[Any]): The data to be paginated.
    - `cursor` (str): The cursor position (e.g., a token representing the last item).
    - `limit` (int): The number of items to display per page.
  - **Returns**: A dictionary with `data`, `meta`, and `next_cursor` keys.

---

## Utility Modules

### `utils.helpers`

This module provides utility functions that help with handling pagination logic.

#### Key Functions

- **`generate_meta(total_items: int, page: int, page_size: int) -> Dict[str, Any]`**
  - Generates metadata for pagination responses.
  - **Parameters**:
    - `total_items` (int): The total number of items in the dataset.
    - `page` (int): The current page number.
    - `page_size` (int): The number of items per page.
  - **Returns**: A dictionary containing metadata such as `total_pages`, `current_page`, and `page_size`.

---

## Exceptions

### `PagifyError`

An exception raised when the pagination process encounters an error. It allows for effective error handling and debugging.

#### Initialization

```python
PagifyError(message: str)
```

- **Parameters**:
  - **`message`** (str): A descriptive message about the error.

### Example Usage

```python
from pagify.core.pagination import paginate_with_page_number
from pagify.exceptions import PagifyError

try:
    result = paginate_with_page_number(data=[1, 2, 3], page=1, page_size=2)
except PagifyError as e:
    print(f"Pagination error: {e}")
```

---

## Conclusion

This API reference outlines the main components and utilities of the **Pagify** package, enabling developers to add flexible and efficient pagination to their Python applications. For practical examples and a guide on getting started, please refer to the [usage documentation](usage.md).