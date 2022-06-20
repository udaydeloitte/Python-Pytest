import requests
import responses

from Resource.allapiResources import ApiResources
from Resource.configurations import getconfig
from Resource.payload import readimxbody

url=getconfig()['API']['endpoint']+ApiResources.readIMxR
@responses.activate
def test_readIMX():
    responses.get(url,json=readimxbody()
    )
    response=requests.get(getconfig()['API']['endpoint']+"/api/v1.0/g2_5mp_camera/read_imx490_register/0x7663")
    assert response.status_code==200
    assert response.json()["Status"]=="success"
    assert response.json()["Register"]=="value"
    print(response.json())