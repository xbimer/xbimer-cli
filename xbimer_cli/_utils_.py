import requests
import json
import click

VERSION = '1.0.0'

__xbimer_domain__ = "http://127.0.0.1:3000"


def httpPost(path, *args, **kwargs):
    url = '/'.join([__xbimer_domain__, path])
    kwargs.setdefault("headers", {"Content-Type": "application/json"})
    data = kwargs.pop("data")
    kwargs.setdefault("data", json.dumps(data))
    res = requests.post(url, *args, **kwargs)
    data = res.json()
    if res.status_code != 200:
        raise click.ClickException(data['message'])

    return data


def httpGet(path, *args, **kwargs):
    url = '/'.join([__xbimer_domain__, path])
    res = requests.get(url, *args, **kwargs)
    if res.status_code != 200:
        raise click.ClickException(res.json()['message'])

    if res.headers['Content-Type'] == 'application/json':
        return res.json()

    return res.text
