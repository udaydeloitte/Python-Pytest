import requests
import responses

from Resource.allapiResources import ApiResources
from Resource.configurations import getconfig
from Resource.payload import pulseintervalbody
url=getconfig()['API']['endpoint']+ApiResources.pulseIntervalR

@responses.activate
def test_pulseInterval():
    responses.post(url, json=pulseintervalbody(), status=200
    )
    response = requests.post(getconfig()['API']['endpoint']+"/api/v1.0/g2_5mp_camera/set_trigger_pulse_interval/")

    assert response.status_code == 200
    assert response.json()["sec"]==1234
    print(response.json())