from pydantic import BaseModel
from requests import Response
import requests

YOUGILE_URL = 'https://ru.yougile.com'

def query(arg:BaseModel,token:str|None=None) -> Response:
    arg = arg.model_copy()
    url = arg._url
    headers = {}
    headers.update({'Content-Type':'application/json'})
    
    if hasattr(arg,'token'):
        if token == None:
            headers.update({'Authorization':f'Bearer {arg.token}'})
            delattr(arg,'token')
        else:
            headers.update({'Authorization':f'Bearer {token}'})
    if hasattr(arg,'_url_parse'):
        for i in arg._url_parse:
            url = url.format(**{i:getattr(arg,i)})
            delattr(arg,i)
    if hasattr(arg,'_url_params'):
        params = []
        for i in arg._url_params:
            if getattr(arg,i) != None:
                params.append(f'{i}={getattr(arg,i)}')
            delattr(arg,i)
        params = '&'.join(params)
        url += '?' + params
    body = arg.model_dump()
    bres = {}
    for i in zip(body.keys(),body.values()):
        if i[1] != None:
            bres.update({i[0]:i[1]})
    if bres != {}:
        return getattr(requests,arg._method)(url=YOUGILE_URL+url,headers=headers,json=bres)
    else:
        return getattr(requests,arg._method)(url=YOUGILE_URL+url,headers=headers)