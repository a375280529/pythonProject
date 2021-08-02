import re
from kazoo.client import KazooClient
import random
from prestool.Tool import Tool
tool=Tool()

def dubboTelnet(host, port, service, method, args):
    try:
        res = tool.invoke_dubbo(host, port, service, method, args)[0]
        print(123321)
        print(res)
        invoke_time = re.findall('elapsed: (.*).\r', res)[0]
        res = res.replace(f'elapsed: {invoke_time}.', '').strip()
        print(666)
        print(res)
        print(888)
    except Exception as e:
        res=e
        invoke_time = False
    return res, invoke_time

class ZooKeeper():
    # 初始化
    def __init__(self,host):
        #self.zk = KazooClient(hosts='127.0.0.1:2181')
        #self.zk = KazooClient(hosts='192.168.85.135:2181')
        self.zk = KazooClient(hosts=host)
        self.zk.start()

    def disconnect(self):
        self.zk.stop()
        self.zk.close()

    def getProviderUrlsByService(self, testService):
        urls = []
        serviceList = self.getServiceList()
        print(serviceList)
        for service in serviceList:
            if testService in service:
                try:
                    providers = self.zk.get_children(f'/dubbo/{service}/providers')
                    if providers:
                        for provider in providers:
                            url = tool.url_decode(provider)
                            if url.startswith('dubbo:'):
                                urls.append(url.split('dubbo://')[1])
                except Exception as e:
                    print(e)
        return urls

    def getDubboInfo(self, testService):
        print(testService)
        urls = self.getProviderUrlsByService(testService)
        paths = []
        for url in urls:
            try:
                path, temp = url.split('/')
                host, port = path.split(':')
                serviceName = temp.split('?')[0]
                methodName = temp.split('methods=')[1].split('&')[0].split(',')
                paths.append({'serviceName': serviceName, 'host': host, 'port': port, 'methodName': methodName})
            except Exception:
                pass
        print(random.choice(paths))
        return random.choice(paths)

    def getServiceList(self):
        return self.zk.get_children("/dubbo")