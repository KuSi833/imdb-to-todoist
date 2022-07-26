from src.todoist import is_valid_api_key


def test_is_valid_api_key():
    assert (not is_valid_api_key("123"))
