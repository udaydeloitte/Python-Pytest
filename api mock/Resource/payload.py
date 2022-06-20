import datetime

def softwareversion():
    body = {
        "api": "/api/v1.0/swupdate/sw-versions",
        "status": "success",
        "versions": {
            "name": "Cruise 1.0",
            "version": "1.0",
        }
    }
    return body

def hardwarerevi():
    body = {
        "api": "/api/v1.0/swupdate/hw-revision",
        "status": "success",
        "board": "Cruiseboardname",
        "revision": "1.1",
    }
    return body


def getsystime():
    body = {"current_time": datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}
    return body


def bootstatusbody():
    body = {"api": "/api/v1.0/swupdate/boot-status",
            "boot-status": "success",
            "status": "fail"
            }
    return body

def RHtBody():
    body = {"device_name1": "device_relative_humidity",
            "readings1": [7.7],
            "unit1": "Relative Humidity (Percentage)",

            "device_name2": "device_temperature",
            "readings2": [55.799],
            "unit2": "Celsius"
            }
    return body


def IMXBody():
    body = {"Status": "Success",
            "register_details": {
                "register": ["0x01"],
                "register_value": ["100"]
            }
            }
    return body

def readimxbody():
    body = {"Register": "value",
            "Status": "success"
            }
    return body

def stressappbody():
    body = {"nodes": 1,
            "cpu_threads": 8,
            "copy_threads": 8,
            "memory": {
                "total_memory": "512MB",
                "free_memory": "256MB",
                "available_memory": "354MB",
                "Buffers": "2484kB",
                "Cached": "9520kB"
            },
            "time_set": 20,
            "status": "PASS",
            "message": "please verify no corrected errors",
            "stats": {
                "stats_message": "found 0 hardware incidents",
                "memory_copy": "13570.00M at 659.48MB/s",
                "file_copy": "176.00M at 8.44MB/s",
                "net_copy": "0.00M at 0.00MB/s",
                "invert_data": "0.00M at 0.00MB/s",
                "disk": "0.00M at 0.00MB/s"
            },
            "tempfile": [
                "/tmp/file2",
                "/tmp/file1"
            ],
            "time_remaining": 10,
            "content_type": "application/json",
            }
    return body

def pulsetime():
    body = {"sec": 1234,
            "nsec": 1234
            }
    return body

def stressng():
    body = {"api": "/api/v1.0/hardware_test/stressng",
            "status": "success",
            "svc_status": {
                "argument_string": "",
                "is_running": "False"
            }
            }
    return body

def pulseintervalbody():
    body={"sec":1234,
              "nsec":1234
              }
    return body

def rebootreasonbody():
    body={"reason":"reboot"}
    return body