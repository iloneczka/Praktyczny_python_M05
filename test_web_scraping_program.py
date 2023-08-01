import pytest
from web_scraping_program import extract_text

def test_extract_text_with_valid_content():
    # Test when the content is valid and the XPath expression matches some elements.
    content = """
    <div>
        <p>Hello, World!</p>
        <p>Testing extraction.</p>
    </div>
    """
    xpath = "//p"
    expected_output = ["Hello, World!", "Testing extraction."]
    assert extract_text(content, xpath) == expected_output

def test_extract_text_with_no_match():
    # Test when the XPath expression does not match any elements in the content.
    content = "<div><p>Some text.</p></div>"
    xpath = "//span"
    expected_output = []
    assert extract_text(content, xpath) == expected_output

def test_extract_text_with_none_content():
    # Test when the content is None.
    with pytest.raises(AttributeError):
        extract_text(None, "//p")

def test_extract_text_with_invalid_xpath():
    # Test when the XPath expression is invalid.
    content = "<div><p>Some text.</p></div>"
    xpath = "invalid_xpath"
    result = extract_text(content, xpath)
    assert result == []

def test_extract_text_with_nested_elements():
    # Test when the XPath expression matches nested elements.
    content = """
    <div>
        <p>Hello, <span>World</span>!</p>
    </div>
    """
    xpath = "//p"
    expected_output = ["Hello, World!"]
    assert extract_text(content, xpath) == expected_output


