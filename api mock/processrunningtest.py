import requests
import responses

from Resource.allapiResources import ApiResources
from Resource.configurations import getconfig

url=getconfig()['API']['endpoint']+ApiResources.processrunningR
@responses.activate
def test_processrunning():
    responses.get(url, json={}, status=200
    )
    response = requests.get(url)

    assert response.status_code == 200
