from miflora.miflora_poller import MiFloraPoller, \
    MI_CONDUCTIVITY, MI_MOISTURE, MI_LIGHT, MI_TEMPERATURE, MI_BATTERY, MI_MAC
import time
import requests
import simplejson as json

def scanDevices (poller, mac):
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
        'temp': temperature,
        'moist': moisture,
        'light': light,
        'room': mac['room'],
        'valve': mac['valve']
        'tray': mac['tray']
        'fert': conductivity,
        'battery': battery }
    print('sending')
    url = "https://us-central1-soilwatch-206306.cloudfunctions.net/uploadData"
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(r.status_code)


def getMacs():
    # will implement call to scan for all devices
    print("Getting macs")
    return [
      {
        'mac': 'c4:7c:8d:62:b2:9c',
        'name': 'first',
        'valve': 1,
        'tray': 1,
        'room': 1
      },
      {
        'mac': 'c4:7c:8d:62:14:64',
        'name': 'unmarked',
        'valve': 1,
        'tray': 2,
        'room': 1
      },
      {
        'mac': 'c4:7c:8d:61:9e:ec',
        'name': 'bob',
        'valve': 2,
        'tray': 1,
        'room': 1
      },
      {
        'mac': 'c4:7c:8d:61:9f:1c',
        'name': 'ryan',
        'valve': 2,
        'tray': 2,
        'room': 1
      },
      {
        'mac': 'c4:7c:8d:61:8b:9a',
        'name': 'susan',
        'valve': 3,
        'tray': 1,
        'room': 1
      },
      {
        'mac': 'c4:7c:8d:61:9e:e4',
        'name': 'reba',
        'valve': 3,
        'tray': 2,
        'room': 1
      },
      {
        'mac': 'c4:7c:8d:61:9f:22',
        'name': 'chang',
        'valve': 4,
        'tray': 1,
        'room': 1
      },
      {
        'mac': 'c4:7c:8d:61:ff:78',
        'name': 'cow',
        'valve': 4,
        'tray': 2,
        'room': 1
      },
      {
        'mac': 'c4:7c:8d:62:74:fd',
        'name': 'rogo',
        'valve': 5,
        'tray': 1,
        'room': 1
      },
      {
        'mac': 'c4:7c:8d:62:10:85',
        'name': 'deko',
        'valve': 5,
        'tray': 2,
        'room': 1
      },
      {
        'mac': 'c4:7c:8d:61:9e:b7',
        'name': 'peggy',
        'valve': 6,
        'tray': 1,
        'room': 1
      },
      {
        'mac': 'c4:7c:8d:61:8c:0a',
        'name': 'ted',
        'valve': 6,
        'tray': 2,
        'room': 1
      },
      {
        'mac': 'c4:7c:8d:61:ff:f1',
        'name': 'daphni',
        'valve': 7,
        'tray': 1,
        'room': 1
      },
      {
        'mac': 'c4:7c:8d:62:75:45',
        'name': 'shiga',
        'valve': 7,
        'tray': 2,
        'room': 1
      },
      {
        'mac': 'c4:7c:8d:62:3e:8f',
        'name': 'roco',
        'valve': 8,
        'tray': 1,
        'room': 1
      },
      {
        'mac': 'c4:7c:8d:61:9e:d1',
        'name': 'rico',
        'valve': 8,
        'tray': 2,
        'room': 1
      },
      {
        'mac': 'c4:7c:8d:61:9e:bc',
        'name': 'treddy',
        'valve': 9,
        'tray': 1,
        'room': 1
      },
      {
        'mac': 'c4:7c:8d:62:3e:78',
        'name': 'rod',
        'valve': 9,
        'tray': 2,
        'room': 1
      },
      {
        'mac': 'c4:7c:8d:62:3e:f4',
        'name': 'treddy',
        'valve': 10,
        'tray': 1,
        'room': 1
      },
      {
        'mac': 'c4:7c:8d:62:75:7f',
        'name': 'treddy',
        'valve': 10,
        'tray': 2,
        'room': 1
      },
    ];

def getPollers(macs):
    print("Getting pollers")
    pollers = []
    for x in macs:
        mac = x["mac"]
        poller = MiFloraPoller(mac)
        pollers.append(poller)
    return pollers

def grabNewData(pollers, macs):
    while True:
        for x in range(len(pollers)):
            scanDevices(pollers[x], macs[x])
        print("\nSleeping\n")
        time.sleep(3000)

def main():
    macs = getMacs()
    print(macs)
    pollers = getPollers(macs)
    grabNewData(pollers, macs)


if __name__ == "__main__":
    main()
