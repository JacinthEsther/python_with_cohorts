voted = {}


def check_voter(name):
    if voted.get(name):
        print("not allowed")
    else:
        voted[name] = True
        print("welcome " + name)


check_voter("Esther")
check_voter("Jacinta")
check_voter("Esther")

cache = {}


def get_data_from_server(url):
    pass


def get_page(url):
    if cache.get(url):
        return cache[url]
    else:
        data = get_data_from_server(url)
        cache[url] = data
        return data
