import datetime

import requests
import responses

from Resource.allapiResources import ApiResources
from Resource.configurations import getconfig
from Resource.payload import getsystime
url=getconfig()['API']['endpoint']+ApiResources.systimeR
@responses.activate
def test_getsystime():
    responses.get(url, json=getsystime(), status=200
    )
    response = requests.get(url)

    print(response.json()["current_time"])

    assert response.json()["current_time"] == datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    assert response.status_code == 200
    print(response.json())