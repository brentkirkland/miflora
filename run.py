from miflora.miflora_poller import MiFloraPoller, \
    MI_CONDUCTIVITY, MI_MOISTURE, MI_LIGHT, MI_TEMPERATURE, MI_BATTERY
import time
import threading

def postData (poller):
    print("Getting data from Mi Flora")
    print("FW: {}".format(poller.firmware_version()))
    print("Name: {}".format(poller.name()))
    print("Temperature: {}".format(poller.parameter_value("temperature")))
    print("Moisture: {}".format(poller.parameter_value(MI_MOISTURE)))
    print("Light: {}".format(poller.parameter_value(MI_LIGHT)))
    print("Conductivity: {}".format(poller.parameter_value(MI_CONDUCTIVITY)))
    print("Battery: {}".format(poller.parameter_value(MI_BATTERY)))

def fetchData():
    # this will be used to find all devices
    print("Getting devices")
    return ["C4:7C:8D:62:95:03"]

def main():
    pollers = []
    fetched_data = fetchData()
    for x in fetched_data:
        poller = postData(MiFloraPoller(x))
        pollers.append(poller)
    while True:
        for poller in pollers:
            postData(poller)
        time.sleep(600)

if __name__ == "__main__":
    main()
