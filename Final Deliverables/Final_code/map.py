import wiotp.sdk.device 
import time 
import random 
myConfig = { 
    "identity": { 
        "orgId": "7cdi8z", 
        "typeId": "railway23", 
        "deviceId":"987654321" 
    },
    "auth": {
        "token": "987654321" 
    }
 }

def myCommandCallback (cmd):
    print ("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']
                                                                   
client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None) 
client.connect()
                                                                   
def pub (data):
    client.publishEvent(eventId="status", msgFormat="json", data=myData,onPublish=None)
    print ("Published data Successfully: %s", myData) 
while True: 
    myData={'name': 'Train1', 'lat': 11.6285, 'lon': 78.12116} 
    pub (myData) 
    time.sleep (3)
    # myData={'name': 'Train', 'lat': 11.54943, 'lon': 78.13141) 
    # pub (myData)
    # time.sleep (3) 
    myData={'name': 'Train1', 'lat': 11.5055, 'lon': 78.15704} 
    pub(myData)
    time.sleep(3)
    myData={'name': 'Train1', 'lat': 11.42137, 'lon': 78.16088} 
    pub (myData) 
    time.sleep (3) 
    myData={'name': 'Train1', 'lat': 11.32717, 'lon': 78.17754} 
    pub (myData) 
    time.sleep (3) 
    myData={'name': 'Train1', 'lat': 11.24174, 'lon': 78.17754} 
    pub (myData) 
    time.sleep (3) 
    myData={'name': 'Train1', 'lat': 11.16735, 'lon': 78.20938} 
    pub (myData) 
    time.sleep (3) 
    myData={'name': 'Train1', 'lat': 11.11783, 'lon': 78.22989} 
    pub (myData) 
    time.sleep (3) 
    myData={'name': 'Train1', 'lat': 11.05591, 'lon': 78.27405} 
    pub (myData) 
    time.sleep (3) 
    myData={'name': 'Train1', 'lat': 11.01566, 'lon': 78.30245} 
    pub (myData) 
    time.sleep (3) 
    myData={'name': 'Train1', 'lat': 10.96767, 'lon': 78.36239} 
    pub (myData) 
    time.sleep (3) 
    client.commandCallback = myCommandCallback 
client.disconnect ()