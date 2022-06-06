import time
import traceback
import requests
from json import loads, dumps
from . import AppConfig
from customexceptions.base import UrlBad, ServerError


class BaseThreadRequest:
    close: bool = False

    def __init__(self, **kwargs):
        super().__init__()
        # self.setDaemon(True)
        # self.threadID = kwargs['threadID']
        # self.name = kwargs['name']
        self._api: str = AppConfig.base_api + f"verify/{kwargs['api_endpoint']}"
        self._headers: dict = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        self._close = False

    def run(self) -> None:
        """ Threads logic goes here"""
        pass

    @staticmethod
    def data_serialization(obj: dict) -> object:
        return loads(dumps(obj).encode('utf-8'))

    def make_request(self, data=None, timeout=10) -> object:
        """ accept data as a json object, timeout as int
        returns response of the api call"""

        for count in range(0, 10, 1):
            try:
                if not data:
                    response = requests.post(self._api, headers=self._headers, timeout=timeout)
                    return response
                else:
                    response = requests.post(self._api, json=data,
                                             headers=self._headers, timeout=timeout)
                    return response

            except requests.exceptions.Timeout:
                # try again
                continue

            except requests.exceptions.TooManyRedirects as e:
                raise UrlBad("Bad url. Contact Support!!!")

            except requests.exceptions.RequestException as e:
                raise ServerError("Error at server. Report Admin!!!")

            # terminate when these values become True
            if BaseThreadRequest.close or self._close:
                break

            time.sleep(1)

        else:
            raise TimeoutError("Connection timed out.\n Check you internet connection")
