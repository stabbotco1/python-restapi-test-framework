def build_request_headers(access_token, content_type="application/json"):
        request_header = {
        "Authorization":f"Bearer {access_token}",
        "Accept":content_type
        }
        return request_header
