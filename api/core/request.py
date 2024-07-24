import requests
import json

class Request(object):
  

  def _header(self, token=""):
      headers = {
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",  # noqa: E501
          "Content-Type": "application/json",
          # "Authorization": "%s" % token
      }

      return headers


  def requestData(self, data, url, token=""):
      response = requests.post(url, data=json.dumps(data), headers=self._header())
      return response.json()