from cat import get_random_cat_image

def test_get_random_cat_image_success(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{'url': 'https://cdn2.thecatapi.com/images/abc.jpg'}]
    mocker.patch('requests.get', return_value=mock_response)

    result = get_random_cat_image()
    assert result == 'https://cdn2.thecatapi.com/images/abc.jpg'

def test_get_random_cat_image_failure(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 404
    mock_response.json.return_value = []
    mocker.patch('requests.get', return_value=mock_response)

    result = get_random_cat_image()
    assert result is None