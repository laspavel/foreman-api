
# -*- coding: utf-8 -*-

"""Простое API для работы с Foreman API на Python.
"""

import json
import urllib3
import requests
from requests.auth import HTTPBasicAuth
from urllib.parse import urljoin

urllib3.disable_warnings()

class ForemanAPI:
    """Реализация API.

    """

    def __init__(self, apihost, login, password):
        """Инициализируем API.

        """
        self.apihost=apihost
        self.login=login
        self.password=password
        self.auth=HTTPBasicAuth(login,password)

    def __getattr__(self, attr):
        return ForemanAPIObject(attr,self)

    def api_request(self, api_type='get', api_method='', **params):
        """Метод для выполнения запроса к API.
        :param api_type: название запроса (put, get, post, etc.)
        :param api_method: название метода из списка функций API
        :param params: параметры соответствующего метода API
        :return: данные в формате JSON
        """
        
        # Формируем URL метода       
        api_method_url = urljoin(self.apihost, api_method)
        for param in params:
            if param=='id':
                api_method_url += '/' +str(params[param])
                
        # Делаем запрос к API и возвращаем JSON-объект
        if api_type=='post':
            fapi = requests.post(api_method_url, verify=False, auth=self.auth, params=params,headers={'Accept': 'application/json'}).json()
        elif api_type=='put':
            fapi = requests.put(api_method_url, verify=False, auth=self.auth, params=params,headers={'Accept': 'application/json'}).json()
        elif api_type=='delete':
            fapi = requests.detete(api_method_url, verify=False, auth=self.auth, params=params,headers={'Accept': 'application/json'}).json()
        else:
            fapi = requests.get(api_method_url, verify=False, auth=self.auth, params=params,headers={'Accept': 'application/json'}).json()
        
        return fapi

class ForemanAPIObject:
    """Динамически вычисляемые объекты API.

    """
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent

    def __getattr__(self, attr):
        """Динамически создаем методы объекта API.

        """
        def wrapper(*args, **kw):
            return self.parent.api_request(api_type=self.name, api_method='{}'.format(str(attr)),**kw)
        return wrapper
            
