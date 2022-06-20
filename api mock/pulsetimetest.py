import requests
import responses

from Resource.allapiResources import ApiResources
from Resource.configurations import getconfig
from Resource.payload import pulsetime

url=getconfig()['API']['endpoint']+ApiResources.pulsetimeR
@responses.activate
def test_pulsetime():
    responses.post(url, json=pulsetime(), status=200
    )
    response = requests.post(url)
    print(response.json())
    assert response.status_code == 200
    assert response.json()["sec"]==1234
