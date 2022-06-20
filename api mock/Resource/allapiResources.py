class ApiResources:
    rebootreasonR = "/api/v1.0/system/reboot_reason"
    bootstatusR = "/api/v1.0/swupdate/boot-status"
    enablepulseR= "/api/v1.0/g2_5mp_camera/enable_trigger_pulse"
    softwareversionR= "/api/v1.0/swupdate/sw-versions"
    hardwarerevisionR= "/api/v1.0/swupdate/hw-revision"
    imxR="/api/v1.0/g2_5mp_camera/set_imx490_register"
    processrunningR= "/api/v1.0/system/is_running/<process_name>"
    pulseIntervalR= "/api/v1.0/g2_5mp_camera/set_trigger_pulse_interval/"
    pulsetimeR="/api/v1.0/g2_5mp_camera/set_trigger_pulse_time/"
    readIMxR="/api/v1.0/g2_5mp_camera/read_imx490_register/0x7663"
    RhtR='/api/v1.0/device/relative_humidity_temperature'
    stressappR="/api/v1.0/hardware_test/stressapptest"
    stressngR="/api/v1.0/hardware_test/stressng/status"
    systimeR='/api/v1.0/system/clock/value'
    enabletriggerR="/api/v1.0/g2_5mp_camera/enable_trigger_pulse"
    readpulsestatsR="/api/v1.0/g2_5mp_camera/read_trigger_pulse_stats"