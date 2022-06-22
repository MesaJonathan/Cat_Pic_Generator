import requests

def get_cat():
    url = 'https://cataas.com/cat'
    file_name = 'cat.png'

    r = requests.get(url)

    with open(file_name, 'wb') as f:
        f.write(r.content)