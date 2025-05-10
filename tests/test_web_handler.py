from unittest.mock import MagicMock
from src.rpachallenge.web_handler import fill_the_form

def test_fill_the_form():
    """Test for filling the form with mock data without actually launching the browser."""
    mock_driver = MagicMock()
    sample_row = {
        "First Name": "Matti",
        "Last Name ": "Barabadabastu",
        "Company Name": "BastuCompany Inc.",
        "Role in Company": "Senior Developer",
        "Address": "Testikatu 7",
        "Email": "matti.barabadabastu@example.com",
        "Phone Number": "1234567890"
    }
    fill_the_form(mock_driver, sample_row)

    expected_fields = {
        "labelFirstName": sample_row["First Name"],
        "labelLastName": sample_row["Last Name "],
        "labelCompanyName": sample_row["Company Name"],
        "labelRole": sample_row["Role in Company"],
        "labelAddress": sample_row["Address"],
        "labelEmail": sample_row["Email"],
        "labelPhone": sample_row["Phone Number"],
    }

    assert mock_driver.find_element.call_count == len(expected_fields) + 1
    for field, value in expected_fields.items():
        # verify that the correct XPath was used to locate the field
        mock_driver.find_element.assert_any_call(
            "xpath", f"//input[@ng-reflect-name='{field}']"
        )
        # verify that send_keys was called with the correct value
        mock_driver.find_element.return_value.send_keys.assert_any_call(value)

    mock_driver.find_element.assert_any_call("xpath", "//input[@type='submit' and @value='Submit']")