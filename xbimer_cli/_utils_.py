import requests
import json
import click
import os
from os import path

VERSION = '1.0.0'

__xbimer_domain__ = "http://127.0.0.1:3000"
__xbimer_token__ = "xbimer-token"
__xbimer_temp__ = "cli.json"


def httpPost(path, *args, **kwargs):
    url = '/'.join([__xbimer_domain__, path])
    kwargs.setdefault("headers", {"Content-Type": "application/json"})
    data = kwargs.pop("data")
    kwargs.setdefault("data", json.dumps(data))
    res = requests.post(url, *args, **kwargs)
    res.raise_for_status()
    return res


def httpGet(path, *args, **kwargs):
    url = '/'.join([__xbimer_domain__, path])
    res = requests.get(url, *args, **kwargs)
    res.raise_for_status()

    if 'application/json' in res.headers['Content-Type']:
        return res.json()

    return res.text


def httpGetWithCookies(url, *args, **kwargs):
    usrHome = path.expanduser("~")
    ximFile = path.join(usrHome, '.xbimer', __xbimer_temp__)
    if not path.exists(ximFile):
        raise click.ClickException("No signin")

    with open(ximFile) as f:
        jcookies = json.loads(f.read())
        f.close()

    kwargs.setdefault('cookies', requests.utils.cookiejar_from_dict(jcookies))
    return httpGet(url, *args, **kwargs)


def httpPostWithCookies(url, *args, **kwargs):
    usrHome = path.expanduser("~")
    ximFile = path.join(usrHome, '.xbimer', __xbimer_temp__)
    if not path.exists(ximFile):
        raise click.ClickException("No signin")

    with open(ximFile) as f:
        jcookies = json.loads(f.read())
        f.close()

    kwargs.setdefault('cookies', requests.utils.cookiejar_from_dict(jcookies))
    return httpPost(url, *args, **kwargs)


def saveToken(res):
    cookiesDit = requests.utils.dict_from_cookiejar(res.cookies)
    if (not (__xbimer_token__ in cookiesDit)):
        raise click.ClickException("xbimer login fail!!")

    usrHome = path.expanduser("~")
    ximHome = path.join(usrHome, ".xbimer")
    if not path.exists(ximHome):
        os.mkdir(ximHome)

    ximFile = path.join(ximHome, __xbimer_temp__)
    ctx = json.dumps({__xbimer_token__: cookiesDit[__xbimer_token__]})

    with open(ximFile, "w") as f:
        f.write(ctx)
        f.close()