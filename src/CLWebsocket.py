# websocket implementation

import asyncio
import websockets
import json
import TPPEntry

class CLWS:

    Gloop = None
    TPClient = None 
    listening = True

    folWidgetId = ""
    subWidgetId = ""
    radWidgetId = ""
    authorization = ""

    # these are just like this
    # me literally just spoofing being a widget lmao
    clIp = "127.0.0.1"
    clPort = "8092"
    pluginId = "co.casterlabs.defaultwidgets"
    widgetMode = "WIDGET" 


    def __init__(self, tpc, socType):
        global TPClient, authorization, folWidgetId, subWidgetId, radWidgetId
        TPClient = tpc

        self.socketType = socType
        if(socType == "follower"):
            self.widgetId = CLWS.folWidgetId
        elif(socType == "subscriber"):
            self.widgetId = CLWS.subWidgetId
        elif(socType == "raid"):
            self.widgetId = CLWS.radWidgetId
        return

    async def listen(self):
        self.uri = f"ws://{CLWS.clIp}:{CLWS.clPort}/api/plugin/{CLWS.pluginId}/widget/{self.widgetId}/realtime?authorization={CLWS.authorization}&mode={CLWS.widgetMode}"
        print(self.widgetId[:3] + "Listening...")
        async with websockets.connect(self.uri) as websocket:
            global listening
            listening = True
            while listening:
                incoming = await websocket.recv()
                try:
                    msg = json.loads(incoming)
                except Exception as ex:
                    print(f"EXCEPTION:\n{ex}")
                    return
                
                print('< ' + self.socketType + ': ' + msg["type"])
                await self.handleMsg(websocket,msg)
                await asyncio.sleep(0.05) 
        return


    async def handleMsg(self, websocket, msg):
        if msg["type"] == "ERROR":
            print(f"CL WEBSOCKET RECEIVED:\n{msg}")
        elif msg["type"] == "PING":
            await self.send(websocket,"PONG",r"{}")
        elif msg["type"] == "INIT":
            await self.send(websocket,"READY",r"{}")
        elif msg["type"] == "UPDATE":
            pass
        elif msg["type"] == "EMISSION": # the beans
            print(f"\n{msg}\n")
            title = msg["data"]["data"]["title"]
            startmatch = r"<span class='highlight'>"
            endmatch = r"</span>"
            name = title[title.find(startmatch)+len(startmatch):title.find(endmatch)]
            self.sendStates(name)
        elif msg["type"] == "KOI_STATICS":
            pass
        elif msg["type"] == "KOI":
            pass
        elif msg["type"] == "MUSIC":
            pass
        elif msg["type"] == "APP":
            pass
        return
    
    def sendStates(self,name):
        global TPClient
        prefix = TPPEntry.PLUGIN_ID + ".state."
        if(self.socketType == "follower"):
            TPClient.stateUpdate(prefix + "cl.lastfollowername",name)
            TPClient.stateUpdate(prefix + "cl.newfollower","New")
            TPClient.stateUpdate(prefix + "cl.newfollower","Waiting")
        elif (self.socketType == "subscriber"):
            TPClient.stateUpdate(prefix + "cl.lastsubscribername",name)
            TPClient.stateUpdate(prefix + "cl.newsubscriber","New")
            TPClient.stateUpdate(prefix + "cl.newsubscriber","Waiting")
        elif (self.socketType == "raid"):
            TPClient.stateUpdate(prefix + "cl.lastraidname",name)
            TPClient.stateUpdate(prefix + "cl.newraid","New")
            TPClient.stateUpdate(prefix + "cl.newraid","Waiting")
        return

    async def send(self, websocket, type, data):
        out = r'{"type":"' + type + r'","data":' + data + r'}'
        await websocket.send(out)
        print(f"> {out}")
        return

    def connect(self):
        global TPClient, Gloop
        print(self.widgetId[:3] + "Connecting...")
        Gloop.create_task(self.listen())


    def disconnect():
        global listening, Gloop
        listening = False
        Gloop.stop()
        asyncio.get_event_loop().stop()
        # print("CLWS DISCONNECT PLEASE")
        return

    def summon(TPClient):
        global Gloop
        Gloop = asyncio.new_event_loop()
        asyncio.set_event_loop(Gloop)
        
        clwsF = CLWS(TPClient,"follower")
        clwsS = CLWS(TPClient,"subscriber")
        clwsR = CLWS(TPClient,"raid")
        
        Gloop.create_task(CLWS.multiConnect(clwsF,clwsS,clwsR))
        try:
            Gloop.run_forever()
        except asyncio.CancelledError:
            pass
        return
        
    async def multiConnect(clwsF,clwsS,clwsR):
        tasks = [clwsF.connect(), clwsS.connect(), clwsR.connect()]
        await asyncio.gather(*tasks)
        return