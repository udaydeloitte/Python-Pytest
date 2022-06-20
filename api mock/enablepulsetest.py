import requests
import responses

from Resource.allapiResources import ApiResources
from Resource.configurations import getconfig

url=getconfig()['API']['endpoint']+ApiResources.enablepulseR
@responses.activate
def test_enabletriggerpulse():
    responses.post(url, json={"enables":1}, status=200
    )
    response = requests.post(url)
    print(response.json())
    assert response.status_code == 200
    assert response.json()["enables"]==1
