import responses
import requests

from Resource.allapiResources import ApiResources
from Resource.configurations import getconfig
from Resource.payload import *
url=getconfig()['API']['endpoint']+ApiResources.softwareversionR
@responses.activate
def test_softwareversion():
    responses.get(url, json=softwareversion(), status=200
    )
    response = requests.get(url)

    assert response.status_code == 200

    assert response.json()['status']=="success"

    assert response.json()['versions']['name']=='Cruise 1.0'

    assert response.json()['versions']['version']=='1.0'
    print(response.json())

    if response.json()['versions']['version']=='1.0':
        print("Exit")
    else:
        print("update component")

