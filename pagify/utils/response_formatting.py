import json
from typing import Any, Dict, Optional, List, Union

class JSONResponseFormatter:
    """Provides helper methods to format responses as JSON for consistency across the application."""

    @staticmethod
    def success(data: Any, message: str = "Success") -> str:
        response = {
            "status": "success",
            "message": message,
            "data": data
        }
        return json.dumps(response)

    @staticmethod
    def error(message: str, code: int = 400) -> str:
        response = {
            "status": "error",
            "message": message,
            "code": code
        }
        return json.dumps(response)

    @staticmethod
    def paginate(
        data: List[Any],
        pagination_info: Dict[str, Union[int, None]],
        message: str = "Paginated data"
    ) -> str:
        response = {
            "status": "success",
            "message": message,
            "data": data,
            "pagination": pagination_info
        }
        return json.dumps(response)

    @staticmethod
    def parse_response(json_response: str) -> Dict[str, Any]:
        return json.loads(json_response)
