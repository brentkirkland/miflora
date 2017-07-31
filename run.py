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

def getMacs():
    # will implement call to scan for all devices
    print("Getting macs")
    return ["C4:7C:8D:62:95:03"]

def getPollers(macs):
    print("Getting pollers")
    pollers = []
    for x in fetched_data:
        print(x)
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
