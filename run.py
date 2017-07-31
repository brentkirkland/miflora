from miflora.miflora_poller import MiFloraPoller, \
    MI_CONDUCTIVITY, MI_MOISTURE, MI_LIGHT, MI_TEMPERATURE, MI_BATTERY
import time

def postData (poller):
    print("Getting data from Mi Flora")

    fw = poller.firmware_version()
    name = poller.name()
    temperature = poller.parameter_value(MI_TEMPERATURE)
    moisture = poller.parameter_value(MI_MOISTURE)
    light = poller.parameter_value(MI_LIGHT)
    conductivity = poller.parameter_value(MI_CONDUCTIVITY)
    battery = poller.parameter_value(MI_BATTERY)

    print("FW: {}".format(fw))
    print("Name: {}".format(name))
    print("Temperature: {}".format(temperature))
    print("Moisture: {}".format(moisture))
    print("Light: {}".format(light))
    print("Conductivity: {}".format(conductivity))
    print("Battery: {}".format(battery))

    url = "http://localhost:8080"
    data = {'fw': fw,
        'name': name,
        'temperature': temperature,
        'moisture': moisture,
        'light': light,
        'conductivity': conductivity,
        'battery': battery }
    headers = {'Content-type': 'application/json'}
    # r = requests.post(url, data=json.dumps(data), headers=headers)

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

def grabNewData(pollers):
    while True:
        for p in pollers:
            postData(p)
        print("\nSleeping\n")
        time.sleep(600)

def main():
    macs = getMacs()
    pollers = getPollers(macs)
    grabNewData(pollers)


if __name__ == "__main__":
    main()
