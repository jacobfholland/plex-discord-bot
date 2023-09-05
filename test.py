connections = [
    'http://169.254.233.151:32433',
    'http://127.0.0.1:32433',
    'http://192.168.139.1:32433',
    'http://192.168.241.1:32433',
    'http://192.168.0.99:32433',
    'http://127.0.0.2:32433',
    'http://169.254.122.102:32433'
]


def custom_sort_key(url):
    if '127.0' in url:
        return (0, url)
    elif '192.168' in url:
        return (1, url)
    else:
        return (2, url)


sorted_connections = sorted(connections, key=custom_sort_key)
print(sorted_connections)
