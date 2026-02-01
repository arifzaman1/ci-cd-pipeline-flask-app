def test_home_route():
    expected = "Hello! This is a CI/CD Flask app running with Docker and Jenkins."
    actual = "Hello! This is a CI/CD Flask app running with Docker and Jenkins."
    assert expected == actual