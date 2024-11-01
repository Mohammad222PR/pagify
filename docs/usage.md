# Usage of Pagify Package

This document offers comprehensive instructions on how to use the **Pagify** package to implement pagination in Python projects.

## Getting Started

### 1. Basic Setup

To start using **Pagify**, import the appropriate pagination class or method from the package and apply it to your data or query result.

```python
from pagify.adapters.paginate import paginate_with_page_number

data = [{'id': i} for i in range(1, 101)]  # Example dataset
result = paginate_with_page_number(data, page=1, page_size=10)
print(result)
```

### 2. Pagination Types

**Pagify** supports multiple pagination methods. Choose the one that suits your project needs:

- **Page Number Pagination**:
  ```python
  from pagify.adapters.paginate import paginate_with_page_number

  result = paginate_with_page_number(data, page=3, page_size=15)
  ```

- **Offset Pagination**:
  ```python
  from pagify.adapters.paginate import paginate_with_offset

  result = paginate_with_offset(data, offset=20, limit=10)
  ```

- **Cursor Pagination**:
  ```python
  from pagify.adapters.paginate import paginate_with_cursor

  result = paginate_with_cursor(data, cursor='next_page_id', limit=10)
  ```

### 3. Configuring Pagination

Each pagination method allows customization:

- `page` or `cursor`: Specifies the current page or cursor token.
- `page_size` or `limit`: Defines the number of items per page.

**Example with configuration**:
```python
from pagify.adapters.paginate import paginate_with_page_number

custom_result = paginate_with_page_number(data, page=2, page_size=20)
print("Custom paginated result:", custom_result)
```

### 4. Response Structure

The pagination functions return a structured response, which typically includes:

- **data**: The paginated data items.
- **meta**: Metadata such as `total_items`, `current_page`, `next_page`, and `previous_page`.

**Example of response**:
```json
{
  "data": [...],
  "pagination": {
    "total_items": 100,
    "current_page": 2,
    "next_page": 3,
    "previous_page": 1,
    "page_size": 20
  }
}
```

### 5. Handling Edge Cases

To manage potential issues like out-of-bounds pages or empty datasets, handle exceptions or check metadata properties:

```python
if not result['data']:
    print("No items found for the current page.")
```

## Conclusion

**Pagify** provides a straightforward and flexible way to implement pagination in Python applications. For further customization and advanced usage, refer to the [API reference](api_reference.md) section.