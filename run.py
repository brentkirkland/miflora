from miflora.miflora_poller import MiFloraPoller, \
    MI_CONDUCTIVITY, MI_MOISTURE, MI_LIGHT, MI_TEMPERATURE, MI_BATTERY, MI_MAC
import time
import requests

def scanDevices (poller):
    print("Getting data from Mi Flora")

    fw = poller.firmware_version()
    mac = poller.parameter_value(MI_MAC)
    temperature = poller.parameter_value(MI_TEMPERATURE)
    moisture = poller.parameter_value(MI_MOISTURE)
    light = poller.parameter_value(MI_LIGHT)
    conductivity = poller.parameter_value(MI_CONDUCTIVITY)
    battery = poller.parameter_value(MI_BATTERY)

    print("FW: {}".format(fw))
    print("Mac: {}".format(mac))
    print("Temperature: {}".format(temperature))
    print("Moisture: {}".format(moisture))
    print("Light: {}".format(light))
    print("Conductivity: {}".format(conductivity))
    print("Battery: {}".format(battery))


    data = {'fw': fw,
        'mac': mac,
        'temperature': temperature,
        'moisture': moisture,
        'light': light,
        'conductivity': conductivity,
        'battery': battery }

    return data

def getMacs():
    # will implement call to scan for all devices
    print("Getting macs")
    return ["C4:7C:8D:62:95:03"]

def getPollers(macs):
    print("Getting pollers")
    pollers = []
    for x in macs:
        poller = MiFloraPoller(x)
        pollers.append(poller)
    return pollers

def postData(readings):

    sumTemp = 0
    for r in readings:
        sumTemp += r["temperature"]
    avgTemp = sumTemp / len(readings)

    payload = {
        'readings': readings,
        'avgTemp': avgTemp,
        'timestamp': time.time(),
        'room_id': 'test_garage',
    }

    print(payload)

    url = "https://us-central1-slurp-165217.cloudfunctions.net/pubEndpoint?topic=processScans"
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(r.status_code)


def grabNewData(pollers):
    while True:
        readings = []
        for p in pollers:
            readings.append(scanDevices(p))
        postData(readings)
        print("\nSleeping\n")
        time.sleep(600)

def main():
    macs = getMacs()
    pollers = getPollers(macs)
    grabNewData(pollers)


if __name__ == "__main__":
    main()
