from fastapi import FastAPI
from pagify.adapters.paginate import paginate_with_page_number

app = FastAPI()

# Sample data
data = [{'id': i, 'name': f'Item {i}'} for i in range(1, 101)]  # A list of 100 items

@app.get("/items/page/")
async def get_items_with_page(page: int = 1, page_size: int = 10):
    result = paginate_with_page_number(data, page, page_size)
    return result

# Run the server and visit: http://127.0.0.1:8000/items/page/?page=3&page_size=10


# Result
"""
{
    "data": [
        {"id": 21, "name": "Item 21"},
        {"id": 22, "name": "Item 22"},
        {"id": 23, "name": "Item 23"},
        {"id": 24, "name": "Item 24"},
        {"id": 25, "name": "Item 25"},
        {"id": 26, "name": "Item 26"},
        {"id": 27, "name": "Item 27"},
        {"id": 28, "name": "Item 28"},
        {"id": 29, "name": "Item 29"},
        {"id": 30, "name": "Item 30"}
    ],
    "pagination_info": {
        "current_page": 3,
        "next_page": 4,
        "previous_page": 2,
        "page_size": 10
    },
    "message": "Page number pagination results"
}
"""