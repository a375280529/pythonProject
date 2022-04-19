# -*- coding: utf-8 -*-
from flask import Flask,request,jsonify,render_template,Response
import json
import config
from pyclass import conOracle as con
import traceback
app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def hello_world():
    return render_template("login.html")

@app.route('/welcome', methods=['POST'])
def welcome():
	name=request.form.get('name')
	pwd=request.form.get('pwd')
	if name=="zxc" and pwd=="123":
		return "welcome："+name
	else:
		return render_template("login.html",biaoshi="0")

@app.route('/jkzdh', methods=['GET'])
def jkzdh():
	print(123321)
	nsr=request.args.get("nsrsbh")
	if nsr=="":
		return jsonify({"msg":"参数不能为空","code":200})
	if nsr==None:
		return jsonify({"msg":"参数名不正确","code":200})
	sql = """insert into zx_nsrjcxx (ID_QY, NSRSBH, NSRMC, ZCDZ, YYDZ, DHHM, YB, QYHGDM, SSHYDM, SSHYMC, DJZCLXDM, DJZCLXMC, NSLXDM, NSLXMC, XYDJ, GSZCH, SCJYQX_Z, 
		ZCZB, SYKJZD, SYKJZDMC, LSGXDM, LSGXMC, NSRZTDM, NSRZTMC, SWJG_DM, SWJG_MC, ZGY, LRSJ, KYRQ, ZCZBBZ, ZYRS, JYFW, XYPFSJ, XYPFFS, ZCD_DHHM, ZCZB_BZMC, 
		ZZJGDM, HZDJRQ, KEYVERSION) values (sys_guid(), '%s', '部署测试企业用100018化有限公司', '开发区星湖****', '开发区星湖****', 
		'13888888888', '226006', null, '4029', '其他专用仪器制造', '173', '私营有限责任公司', '22', '一般纳税人', 'B', '913206917596655423', '9999-12-31', '2000000', '201', 
		'企业会计制度（2001）', '61', '街道', '03', '正常', '13206900000', '国家税务总局南通市税务局第三税务分局', null, to_date('02-03-2020 05:31:23', 'dd-mm-yyyy hh24:mi:ss'), 
		'2004-04-01', null, '25', '工业机器人集成、焊接专用设备、焊接辅助机械及专用数控机床自动化配套系统等研发、设计、制造、销售维修；焊接结构件的制造、销售；自营和代理各类商品的进出口业务，
		但国家限定公司经营或禁止进出口的商品及技术除外；焊接技术的咨询与服务。（依法须经批准的项目，经相关部门批准后方可开展经营活动）', '2018', null, '13888888888', 
		null, '759665542', '2004-04-01', null)"""%(nsr)
	re=con.updateOracleReturn("zxc/zxc@192.168.85.81:1521/emserver",sql)
	if re=="false":
		return jsonify({"msg": "sql异常", "code": 200})
	else:
		return jsonify({"msg": "成功", "code": 200})

@app.route('/add', methods=['POST'])
def add():
    result = {'sum': request.json['a'] + request.json['b'],"code":200,"msg":"成功"}
    resp=Response(json.dumps(result), mimetype='application/json')
    resp.headers.add('Server', 'python flask')
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
