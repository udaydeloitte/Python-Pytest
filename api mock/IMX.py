import requests
import responses
from responses import matchers

from Resource.allapiResources import ApiResources
from Resource.configurations import getconfig
from Resource.payload import IMXBody
url=getconfig()['API']['endpoint']+ApiResources.imxR

@responses.activate
def test_setIMX():
    responses.post(url,
        json=IMXBody(),
        match=[matchers.urlencoded_params_matcher({"register": "0x01", "register_value": "100"})],
        status=200
    )
    response = requests.post(url, data={"register": "0x01", "register_value": "100"})

    assert response.status_code==200
    assert response.json()["register_details"]["register"]==["0x01"]
    print(response.json())