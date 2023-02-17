# -*-coding:utf-8-*-
import json
import random
import stomp
import string

def conActiveMq(host='',port=0,username='',passcode=''):
    try:
        conn=stomp.Connection([(host,port)])
        conn.connect(username=username,passcode=passcode,wait=True)
    except:
        pass
    return conn

def send_to_queue(con,msg,queuename):
    result= {}
    # body=数据, destination=根据队列名传输数据,如果队列不存在,就创建一个
    try:
        con.send(body=str(msg), destination=queuename, headers={"amq-msg-type": "text"})
        result={"result":"True","msg":msg}
    except Exception as e:
        result={"result":"False"}
    return result

def send_activemq(quename,host,port,username,password,params):
    try:
        con = conActiveMq(host=host, port=port, username=username, passcode=password)
        result=send_to_queue(con,params,quename)
        return result
    except:
        return "erro"
    finally:
        con.disconnect()

def create_string_number(n):
    """生成一串指定位数的字符+数组混合的字符串"""
    m = random.randint(1, n)
    a = "".join([str(random.randint(0, 9)) for _ in range(m)])
    b = "".join([random.choice(string.ascii_letters) for _ in range(n - m)])
    return ''.join(random.sample(list(a + b), n))

if __name__ == '__main__':
    # queuename= "vz.queue.service.collect.taxdata.xiamen"
    # queuename= "vz.queue.service.feedback.xiamen"
    # con=conActiveMq(host='192.168.84.230',port=61613,username='admin',passcode='admin')
    # map="""{"head":{"nsrsbh":"913502000583983816","source":"feedback_server","target":"dataCollect_server"},"body":{"reason":"成功","zyje":"","city":"厦门市","dkzzrq":"","sxsj":"2021-05-22","dkcpbh":"WYD","zdye":"","feedback_message":"总行版默认发送一次就是反馈成功","qyyhzh":"9999648290050100004000","update_time":"2022-12-06 10:16:18.0","datatype":"dksp","sjlx":"","sxje":"300.00","product_id":"","spjgms":"","feedback_status":"1111","sdsj":"2046-11-28","sfyq":"","sfcxydk":"Y","dkhtbh":"2105200K702190GCFYIZZH74Y1N61111","nsrmc":"厦门哲林软件科技有限公司","sfxw":"Y","zqqx":"","dkll":"7.2%","spje":"","spjg":"Y","zysj":"","lrsj":"2022-12-04 15:12:36.0","yqts":"","sfzjed":"","nsrsbh":"913502000583983816","dqyqje":"","zjed":"","zqsj":"","spjgdm":"","sxqx":"2023-05-22","dkcpmc":"微业贷","sfzq":"","md5":"cf0c631744cb8c82d6b7727b80ed6451"}}"""
    # map=json.loads(json.dumps(map,ensure_ascii=False))
    # print(map)
    # result=send_to_queue(con,map,queuename)
    # print(result)
    # con.disconnect()
    quename = "vz.queue.service.feedback.xiamen"
    #quename = "vz.queue.service.collect.taxdata.xiamen"
    host='192.168.84.230'
    port=61613
    username='admin'
    password='admin'
    dkhtbh=create_string_number(32)
    #params="""{"head":{"nsrsbh":"913502000583983816","source":"feedback_server","target":"dataCollect_server"},"body":{"reason":"成功","zyje":"","city":"厦门市","dkzzrq":"","sxsj":"2021-05-22","dkcpbh":"WYD","zdye":"","feedback_message":"总行版默认发送一次就是反馈成功","qyyhzh":"9999648290050100004000","update_time":"2022-12-06 10:16:18.0","datatype":"dksp","sjlx":"","sxje":"300.00","product_id":"","spjgms":"","feedback_status":"1111","sdsj":"2046-11-28","sfyq":"","sfcxydk":"Y","dkhtbh":\""""+dkhtbh+"""\","nsrmc":"厦门哲林软件科技有限公司","sfxw":"Y","zqqx":"","dkll":"7.2%","spje":"","spjg":"Y","zysj":"","lrsj":"2022-12-04 15:12:36.0","yqts":"","sfzjed":"","nsrsbh":"913502000583983816","dqyqje":"","zjed":"","zqsj":"","spjgdm":"","sxqx":"2023-05-22","dkcpmc":"微业贷","sfzq":"","md5":"cf0c631744cb8c82d6b7727b80ed6451"}}"""
    params="""{
 "head": {
  "actionName": "vz.queue.service.collect.taxdata.global",
  "reqId": "",
  "source": "vz_postloan_server",
  "nsrsbh": "913502000583983816"
 },
 "body": {
  "collect_sub": {
   "nsrsbh": "913502000583983816",
   "flag": "1",
   "createtime": 1669878106000,
   "remark": "{\\\"ext0\\\":\\\"0\\\",\\\"sqrxm\\\":\\\"张敏\\\",\\\"yhdm\\\":\\\"027\\\",\\\"qqsj\\\":\\\"2022-12-01\\\",\\\"city\\\":\\\"厦门\\\",\\\"nsrmc\\\":\\\"厦门哲林软件科技有限公司\\\",\\\"sqrsfzh\\\":\\\"430725197906280027\\\",\\\"frzjhm\\\":\\\"430725197906280027\\\",\\\"orgId\\\":\\\"wz\\\",\\\"serialNo\\\":\\\"\\\",\\\"areaCode\\\":\\\"xiamen\\\",\\\"nsrsbh\\\":\\\"913502000583983816\\\",\\\"qqlx\\\":\\\"0\\\",\\\"sqqdrq\\\":\\\"2022-12-01\\\",\\\"yhmc\\\":\\\"深圳前海微众银行股份有限公司\\\"}",
   "sign": "XIAMEN"
  },
  "collect": {
   "nsrsbh": "913502000583983816",
   "dataType": "1"
  }
 }
}"""
    params="""{"head":{"nsrsbh":"913502000583983816","source":"feedback_server","target":"dataCollect_server"},"body":{"reason":"成功","zyje":"","city":"厦门市","dkzzrq":"","sxsj":"2021-05-22","dkcpbh":"WYD","zdye":"","feedback_message":"总行版默认发送一次就是反馈成功","qyyhzh":"9999648290050100004000","update_time":"2022-12-06 10:16:18.0","datatype":"dksp","sjlx":"","sxje":"300.00","product_id":"","spjgms":"","feedback_status":"1111","sdsj":"2046-11-28","sfyq":"","sfcxydk":"Y","dkhtbh":\""""+dkhtbh+"""\","nsrmc":"厦门哲林软件科技有限公司","sfxw":"Y","zqqx":"","dkll":"7.2%","spje":"","spjg":"Y","zysj":"","lrsj":"2022-12-04 15:12:36.0","yqts":"","sfzjed":"","nsrsbh":"913502000583983816","dqyqje":"","zjed":"","zqsj":"","spjgdm":"","sxqx":"2023-05-22","dkcpmc":"微业贷","sfzq":"","md5":"cf0c631744cb8c82d6b7727b80ed6451"}}"""
    params=json.loads(json.dumps(params,ensure_ascii=False))
    ret=send_activemq(quename, host, port, username, password, params)
    print(ret)
