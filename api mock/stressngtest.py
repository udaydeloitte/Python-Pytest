import requests
import responses

from Resource.allapiResources import ApiResources
from Resource.configurations import getconfig
from Resource.payload import stressng

url=getconfig()['API']['endpoint']+ApiResources.stressngR
@responses.activate
def test_stressng():
    responses.post(url, json=stressng(), status=200,
    )
    response = requests.post(url)

    assert response.status_code == 200
    assert response.json()["status"]=="success"
    assert response.json()["svc_status"]["is_running"]=="False"
    print(response.json())