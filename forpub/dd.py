import asyncio
import websockets
from pyclass import getInterface as gi

# 检测客户端权限，用户名密码通过才能退出循环
async def check_permit(websocket):
    while True:
        recv_str = await websocket.recv()
        cred_dict = recv_str.split(":")
        # if cred_dict[0] == "admin" and cred_dict[1] == "123456":
        response_str = "congratulation, you have connect with server\r\nnow, you can do something else"
        await websocket.send(response_str)
        return True
        # else:
        #     response_str = "sorry, the username or password is wrong, please submit again"
        #     await websocket.send(response_str)

# 接收客户端消息并处理，这里只是简单把客户端发来的返回回去
async def recv_msg(websocket):
    while True:
        recv_text = await websocket.recv()
        print(recv_text)
        if "嘻嘻" in recv_text:
            url="http://127.0.0.1:8080/gateway/anhui"
            params={}
            headers={}
            dd=gi.getJsonForGetInterface(url,params,headers)
            print(dd)
            response_text = f"your submit context: {dd['json']}"
            await websocket.send(response_text)
        elif "测试" in recv_text:
            url = "http://127.0.0.1:8080/vz-service-collect-henan/api/collect/preloan"
            params = {}
            headers = {}
            dd = gi.getJsonForPostInterface(url, params, headers)
            print(dd)
            response_text = f"your submit context: {dd['json']}"
            await websocket.send(response_text)
        else:
            response_text = f"your submit context: 123"
            await websocket.send(response_text)

# 服务器端主逻辑
# websocket和path是该函数被回调时自动传过来的，不需要自己传
async def main_logic(websocket, path):
    #await check_permit(websocket)

    await recv_msg(websocket)

# 把ip换成自己本地的ip
start_server = websockets.serve(main_logic, '192.168.87.65', 5678)
# 如果要给被回调的main_logic传递自定义参数，可使用以下形式
# 一、修改回调形式
# import functools
# start_server = websockets.serve(functools.partial(main_logic, other_param="test_value"), '10.10.6.91', 5678)
# 修改被回调函数定义，增加相应参数
# async def main_logic(websocket, path, other_param)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()