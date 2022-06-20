import time

import requests
import responses

from Resource.allapiResources import ApiResources
from Resource.configurations import getconfig
from Resource.payload import RHtBody

url=getconfig()['API']['endpoint'] + ApiResources.RhtR
@responses.activate
def test_RHT():
    start = time.time()
    responses.get(url, json=RHtBody(), status=200
    )

    response = requests.get(url)
    assert response.status_code == 200
    assert response.json()["unit1"] == "Relative Humidity (Percentage)"
    assert response.json()["unit2"] == "Celsius"
    end = time.time()
    print(response.json())
    assert (end - start) * 1000 < 100
