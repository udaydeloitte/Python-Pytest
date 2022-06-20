import requests
import responses

from Resource.allapiResources import ApiResources
from Resource.configurations import getconfig
from Resource.payload import bootstatusbody

url=getconfig()['API']['endpoint']+ApiResources.bootstatusR
@responses.activate
def test_bootstatus():
    responses.get(url, json=bootstatusbody(), status=200
    )
    response = requests.get(url)

    assert response.json()["boot-status"]=="success"

    assert response.status_code==200

    assert response.status_code!=401
    assert response.status_code!=400
    assert response.json()["status"]=="fail"
    if response.json()["status"]=="fail":
        print("Reset Device")