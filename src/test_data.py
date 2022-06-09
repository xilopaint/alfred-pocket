def get_normal():
    return {
        "1": {
            "excerpt": "abc123",
            "favorite": "0",
            "given_title": "",
            "given_url": "http://google.com",
            "has_image": "0",
            "is_article": "1",
            "is_index": "1",
            "item_id": "1111",
            "resolved_id": "1111",
            "resolved_title": "",
            "resolved_url": "",
            "status": "0",
            "time_added": "54321",
            "time_favorited": "0",
            "time_updated": "54321",
            "tags": {"mytag": {}},
        },
        "2": {
            "excerpt": "abc",
            "favorite": "1",
            "given_title": "",
            "given_url": "http://fniephaus.com",
            "has_image": "0",
            "is_article": "0",
            "is_index": "0",
            "item_id": "2222",
            "resolved_id": "2222",
            "resolved_title": "",
            "resolved_url": "",
            "status": "0",
            "time_added": "1396054841",
            "time_favorited": "0",
            "time_updated": "1396054841",
            "tags": {"foo": {}},
        },
        "300": {
            "excerpt": "text2",
            "favorite": "0",
            "given_title": "title321",
            "given_url": "http://github.com",
            "has_image": "1",
            "is_article": "0",
            "is_index": "0",
            "item_id": "3333",
            "resolved_id": "722186783",
            "resolved_title": "resolvedtitle",
            "resolved_url": "",
            "status": "0",
            "time_added": "1411528927",
            "time_favorited": "0",
            "time_updated": "1411528927",
            "videos": {},
            "tags": {},
        },
        "4": {
            "excerpt": "text2",
            "favorite": "0",
            "given_title": "title321",
            "given_url": "http://archive.com",
            "has_image": "0",
            "is_article": "0",
            "has_video": "1",
            "is_index": "0",
            "item_id": "3333",
            "resolved_id": "722186783",
            "resolved_title": "resolvedtitle",
            "resolved_url": "",
            "status": "1",
            "time_added": "1411528927",
            "time_favorited": "0",
            "time_updated": "1411528927",
            "videos": {},
            "tags": {},
        },
    }


def get_refresh_initial():
    return {"status": 1, "error": None, "complete": 1, "since": 1, "list": get_normal()}


def get_refresh_delta(since):
    return {
        "status": 1,
        "error": None,
        "complete": 0,
        "since": since + 10,
        "list": {
            "1337": {
                "status": "0",
                "is_index": "0",
                "time_updated": "1420711247",
                "time_favorited": "0",
                "excerpt": "",
                "has_image": "0",
                "favorite": "0",
                "given_title": "title123",
                "resolved_url": "",
                "is_article": "0",
                "item_id": "4444",
                "time_added": "1420711246",
                "resolved_id": "4444",
                "given_url": "http://nasa.gov",
                "resolved_title": "",
            },
            "42": {
                "status": "2",
                "is_index": "0",
                "time_updated": "1420892898",
                "time_favorited": "0",
                "excerpt": "ec",
                "has_image": "1",
                "favorite": "0",
                "given_title": "",
                "resolved_url": "",
                "is_article": "1",
                "item_id": "1111",
                "time_added": "1420828162",
                "resolved_id": "1111",
                "given_url": "http://github.com",
                "resolved_title": "",
            },
        },
    }


def get_refresh_end(since):
    return {"status": 0, "error": None, "complete": 0, "since": since + 10, "list": {}}
