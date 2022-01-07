def testaUrl(site):
    site = input(site)
    from urllib.request import Request, urlopen
    from urllib.error import URLError, HTTPError
    req = Request(site)
    try:
        response = urlopen(req)
    except HTTPError as erro:
        print(f'O site não está disponível devido a {erro.code}')
    except URLError as erro:
        print(f'O erro encontrado foi {erro.reason}')
    else:
        print(f'{site} Online')


testaUrl('Digite um endereço')