import requests
import responses

from Resource.allapiResources import ApiResources
from Resource.configurations import getconfig
from Resource.payload import rebootreasonbody

url=getconfig()['API']['endpoint']+ApiResources.rebootreasonR

@responses.activate
def test_rebootreason():
    responses.get(url,json=rebootreasonbody(),status=200
    )
    response = requests.get(url)

    assert response.status_code == 200
    assert response.status_code !=404
    assert response.status_code !=401

    print(response.json())

