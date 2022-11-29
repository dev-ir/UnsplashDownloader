def response_code(code):
    match code:
        case 200:
            return {
                'label': 'success',
                'code': code,
            }
        case 400:
            return {
                'label': 'The request was unacceptable, often due to missing a required parameter',
                'code': code,
            }
        case 401:
            return {
                'label': 'Invalid Access Token',
                'code': code,
            }
        case 403:
            return {
                'label': 'Missing permissions to perform request',
                'code': code,
            }
        case 404:
            return {
                'label': 'The requested resource doesn’t exist',
                'code': code,
            }
        case 500 | 503:
            return {
                'label': 'Something went wrong on our end',
                'code': code,
            }