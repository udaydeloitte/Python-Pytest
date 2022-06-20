import requests
import responses

from Resource.allapiResources import ApiResources
from Resource.configurations import getconfig
from Resource.payload import hardwarerevi


url=getconfig()['API']['endpoint']+ApiResources.hardwarerevisionR
@responses.activate
def test_hardwarerevision():
    responses.get(url, json=hardwarerevi(), status=200
    )
    response = requests.get(url)

    assert response.status_code==200

    assert response.json()["board"]=="Cruiseboardname"

    assert response.json()["revision"]=="1.1"
    if response.json()["revision"]=="1.1":
        print("Pass")
    else:
        print("Fail")
    print(response.json())