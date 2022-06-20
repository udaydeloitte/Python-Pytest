import requests
import responses

from Resource.allapiResources import ApiResources
from Resource.configurations import getconfig
from Resource.payload import stressappbody


url=getconfig()['API']['endpoint']+ApiResources.stressappR
@responses.activate
def test_stressapp():
    responses.get(url,
        json=stressappbody()
    )
    response=requests.get(url)
    assert response.status_code==200

    assert response.json()["status"]=="PASS"

    assert response.json()["cpu_threads"]==8

    assert response.json()["memory"]["total_memory"]=="512MB"

    assert response.json()["message"]== "please verify no corrected errors"
    print(response.json())