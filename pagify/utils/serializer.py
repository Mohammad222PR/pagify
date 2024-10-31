from typing import List, Any


class Serializer:
    @staticmethod
    def serialize(data: List[Any]) -> List[dict]:
        """Converts a list of items into a list of dictionaries."""
        return [dict(item) for item in data]
