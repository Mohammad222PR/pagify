from fastapi import FastAPI
from pagify.adapters.paginate import paginate_with_offset

app = FastAPI()

# Sample data
data = [{'id': i, 'name': f'Item {i}'} for i in range(1, 101)]  # A list of 100 items

@app.get("/items/offset/")
async def get_items_with_offset(offset: int = 0, limit: int = 10):
    result = paginate_with_offset(data, offset, limit)
    return result

# Run the server and visit: http://127.0.0.1:8000/youre-endpoint/offset/?offset=20&limit=10


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
        "next_offset": 30,
        "previous_offset": 10,
        "limit": 10
    },
    "message": "Offset pagination results"
}
"""