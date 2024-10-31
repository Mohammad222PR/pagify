import pytest
from pagify.adapters.paginate import paginate_with_offset, paginate_with_cursor, paginate_with_page_number
from pagify.utils.response_formatting import JSONResponseFormatter


@pytest.fixture
def queryset():
    """Mocked dataset for testing."""
    return [{'id': i} for i in range(1, 101)]  # Mocked dataset with 100 items


def test_paginate_with_offset_integration(queryset):
    result = paginate_with_offset(queryset, offset=20, limit=10)
    result_data = JSONResponseFormatter.parse_response(result)

    assert result_data['pagination']['next_offset'] == 30  # Next offset should be 30
    assert result_data['pagination']['previous_offset'] == 10  # Previous offset should be 10
    assert len(result_data['data']) == 10  # Ensure we have the correct number of items
    assert result_data['data'][0]['id'] == 21  # The first item should be 21 (offset of 20)


def test_paginate_with_cursor_integration(queryset):
    result = paginate_with_cursor(queryset, cursor=20, limit=10)
    result_data = JSONResponseFormatter.parse_response(result)

    assert result_data['pagination']['cursor'] == 20
    assert result_data['pagination']['next_cursor'] == 30
    assert len(result_data['data']) == 10
    assert result_data['data'][0]['id'] == 21  # Correct data should be returned


def test_paginate_with_page_number_integration(queryset):
    result = paginate_with_page_number(queryset, page=3, page_size=10)
    result_data = JSONResponseFormatter.parse_response(result)

    assert result_data['pagination']['current_page'] == 3
    assert result_data['pagination']['next_page'] == 4
    assert len(result_data['data']) == 10
    assert result_data['data'][0]['id'] == 21  # Correct data should be returned


def test_paginate_with_offset_edge_case(queryset):
    result = paginate_with_offset(queryset, offset=90, limit=10)
    result_data = JSONResponseFormatter.parse_response(result)

    assert result_data['pagination']['next_offset'] is None  # No next page should be available
    assert len(result_data['data']) == 10  # Should not exceed available data


def test_paginate_with_cursor_edge_case(queryset):
    result = paginate_with_cursor(queryset, cursor=100, limit=10)
    result_data = JSONResponseFormatter.parse_response(result)

    assert result_data['pagination']['next_cursor'] is None  # No next page should be available
    assert len(result_data['data']) == 0  # No data should be returned


def test_paginate_with_page_number_edge_case(queryset):
    result = paginate_with_page_number(queryset, page=11, page_size=10)
    result_data = JSONResponseFormatter.parse_response(result)

    assert result_data['pagination']['next_page'] is None  # No next page should be available
    assert len(result_data['data']) == 0  # No data should be returned
