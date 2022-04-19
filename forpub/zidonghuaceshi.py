#!/usr/bin/python
# -*- coding: utf-8 -*-

from pyclass import conOracle,forExcel

if __name__ == '__main__':
    # aa="SW_JCXX_CLNX,SW_JCXX_DJZCLXDM,SW_JCXX_HY,SW_JCXX_NSRLXDM,SW_JCXX_NSRXYPJ,SW_JCXX_NSRZTDM,SW_JCXX_SCJYQXZ,SW_JCXX_XZQH,SW_JCXX_ZCZB,SW_LXR_CWFZRXB,SW_LXR_FRNL,SW_LXR_CWFZRNL,SW_LXR_FRXB,SW_LXR_FRZJHM,SW_LXR_CWFZRZJHM,SW_LXR_FRXM,SW_LXR_CWFZRXM,SW_TZF_FRTZBL,SW_TZF_GDGS,SW_TZF_GDGS_FR,SW_TZF_GDGS_ZRR,SW_TZF_GDTZBL_FIRST,SW_TZF_GDTZBL_FIRST_SFFR,SW_BG_BSRY_01M,SW_BG_BSRY_03M,SW_BG_BSRY_06M,SW_BG_BSRY_12M,SW_BG_BSRY_24M,SW_BG_CWFZR_01M,SW_BG_CWFZR_03M,SW_BG_CWFZR_06M,SW_BG_CWFZR_12M,SW_BG_CWFZR_24M,SW_BG_FR_01M,SW_BG_FR_03M,SW_BG_FR_06M,SW_BG_FR_12M,SW_BG_FR_24M,SW_BG_HY_01M,SW_BG_HY_03M,SW_BG_HY_06M,SW_BG_HY_12M,SW_BG_HY_24M,SW_BG_JYDZ_01M,SW_BG_JYDZ_03M,SW_BG_JYDZ_06M,SW_BG_JYDZ_12M,SW_BG_JYDZ_24M,SW_BG_JYFW_01M,SW_BG_JYFW_03M,SW_BG_JYFW_06M,SW_BG_JYFW_12M,SW_BG_JYFW_24M,SW_BG_TZF_01M,SW_BG_TZF_03M,SW_BG_TZF_06M,SW_BG_TZF_12M,SW_BG_TZF_24M,SW_BG_ZCZB_01M,SW_BG_ZCZB_03M,SW_BG_ZCZB_06M,SW_BG_ZCZB_12M,SW_BG_ZCZB_24M,SW_BG_ZCZBJZ_01M,SW_BG_ZCZBJZ_03M,SW_BG_ZCZBJZ_06M,SW_BG_ZCZBJZ_12M,SW_BG_ZCZBJZ_24M,SW_WFWZ_01M,SW_WFWZ_03M,SW_WFWZ_06M,SW_WFWZ_12M,SW_WFWZ_24M,SW_WFWZ_YB_01M,SW_WFWZ_YB_03M,SW_WFWZ_YB_06M,SW_WFWZ_YB_12M,SW_WFWZ_YB_24M,SW_WFWZ_YZ_01M,SW_WFWZ_YZ_03M,SW_WFWZ_YZ_06M,SW_WFWZ_YZ_12M,SW_WFWZ_YZ_24M,SW_JCAJ_01M,SW_JCAJ_03M,SW_JCAJ_06M,SW_JCAJ_12M,SW_JCAJ_24M,ID,SW_JCXX_NSRMC_FGSBS,SW_JCXX_HYJRBS,SW_JCXX_DQJRBS,SW_JCXX_NSRMC,SW_JCXX_SFZZY_A,SW_JCXX_DJZCLXMC,SW_TZF_FRTZBL_HMXM,SW_BG_FR_02M,SW_BG_FR_09M,SW_BG_FR_15M,SW_BG_FR_18M,SW_BG_FR_21M,SW_BG_HY_02M,SW_BG_HY_09M,SW_BG_HY_15M,SW_BG_HY_18M,SW_BG_HY_21M,SW_WFWZ_02M,SW_WFWZ_09M,SW_WFWZ_15M,SW_WFWZ_18M,SW_WFWZ_21M,SW_WFWZ_YZ_02M,SW_WFWZ_YZ_09M,SW_WFWZ_YZ_15M,SW_WFWZ_YZ_18M,SW_WFWZ_YZ_21M,SW_JCXX_NSRJCXX_SFQS,SW_LXR_LXRXX_SFQS,SW_TZF_TZFXX_SFQS,SW_BG_FRBGJJTS,SW_TZF_TZFJJXZLX,SW_JCXX_SFGTGSH,SW_TZF_GQFSD,SW_WFWZ_JJYS,SW_WFWZ_YZ_DH,SW_BG_FR_DH,SW_BG_HY_DH,SW_BG_BSRY_DH,SW_BG_FRYDDH_12M"
    #
    # print(len(aa.split(",")))

    # sql1="select nsrsbh,lrsj from zx_nsrjcxx where rownum<=200"

    sql2=""

    # re=conOracle.queryOracleAllReturnList("test_source/test_source@192.168.85.81:1521/emserver", sql1)
    lists=[{"NSRSBH":"913307005669107196","LRSJ":"2020-04-13"},{"NSRSBH":"91430722MA4M105325","LRSJ":"2020-04-13"},{"NSRSBH":"913211813462100351","LRSJ":"2020-04-13"},{"NSRSBH":"913205945618109539","LRSJ":"2020-04-13"},{"NSRSBH":"915301276787105486","LRSJ":"2020-04-13"},{"NSRSBH":"911201037128101150","LRSJ":"2020-04-13"},{"NSRSBH":"91410221MA45100001","LRSJ":"2020-04-13"},{"NSRSBH":"914107023956100002","LRSJ":"2020-04-13"},{"NSRSBH":"914203040554100003","LRSJ":"2020-04-13"},{"NSRSBH":"914208023317100004","LRSJ":"2020-04-13"},{"NSRSBH":"914201125848100005","LRSJ":"2020-04-13"},{"NSRSBH":"914201036823100006","LRSJ":"2020-04-13"},{"NSRSBH":"91420800MA48100007","LRSJ":"2020-04-13"},{"NSRSBH":"91430281MA4L100008","LRSJ":"2020-04-13"},{"NSRSBH":"914302005910100009","LRSJ":"2020-04-13"},{"NSRSBH":"914301023293100010","LRSJ":"2020-04-13"},{"NSRSBH":"91430104MA4M100011","LRSJ":"2020-04-13"},{"NSRSBH":"914406067398100012","LRSJ":"2020-04-13"},{"NSRSBH":"914419003151100013","LRSJ":"2020-04-13"},{"NSRSBH":"914403005598100014","LRSJ":"2020-04-13"},{"NSRSBH":"91442000MA4W100015","LRSJ":"2020-04-13"},{"NSRSBH":"913201150626100016","LRSJ":"2020-04-13"},{"NSRSBH":"913204125855100017","LRSJ":"2020-04-13"},{"NSRSBH":"913206917596100018","LRSJ":"2020-04-13"},{"NSRSBH":"913202045837100019","LRSJ":"2020-04-13"},{"NSRSBH":"91320113MA1W100020","LRSJ":"2020-04-13"},{"NSRSBH":"913301220888100021","LRSJ":"2020-04-13"},{"NSRSBH":"913307815985100022","LRSJ":"2020-04-13"},{"NSRSBH":"913306047434100023","LRSJ":"2020-04-13"},{"NSRSBH":"913303826725100024","LRSJ":"2020-04-13"},{"NSRSBH":"913410046104100025","LRSJ":"2020-04-13"},{"NSRSBH":"91340103MA2N100026","LRSJ":"2020-04-13"},{"NSRSBH":"913506280953100027","LRSJ":"2020-04-13"},{"NSRSBH":"913607027969100028","LRSJ":"2020-04-13"},{"NSRSBH":"913611233225100029","LRSJ":"2020-04-13"},{"NSRSBH":"91360402MA38100030","LRSJ":"2020-04-13"},{"NSRSBH":"91411503MA44100031","LRSJ":"2020-04-13"},{"NSRSBH":"914107817906100032","LRSJ":"2020-04-13"},{"NSRSBH":"914114036728100033","LRSJ":"2020-04-13"},{"NSRSBH":"914109000559100034","LRSJ":"2020-04-13"},{"NSRSBH":"91410225MA44100035","LRSJ":"2020-04-13"},{"NSRSBH":"91341825MA2M100036","LRSJ":"2020-04-13"},{"NSRSBH":"92340802MA2P100037","LRSJ":"2020-04-13"},{"NSRSBH":"913401005663100038","LRSJ":"2020-04-13"},{"NSRSBH":"91341222MA2M100039","LRSJ":"2020-04-13"},{"NSRSBH":"913506813157100040","LRSJ":"2020-04-13"},{"NSRSBH":"913501001543100041","LRSJ":"2020-04-13"},{"NSRSBH":"913506240561100042","LRSJ":"2020-04-13"},{"NSRSBH":"913501007983100043","LRSJ":"2020-04-13"},{"NSRSBH":"913502050511100044","LRSJ":"2020-04-13"},{"NSRSBH":"911408296942100045","LRSJ":"2020-04-13"},{"NSRSBH":"914403003564100046","LRSJ":"2020-04-13"},{"NSRSBH":"914403001922100047","LRSJ":"2020-04-13"},{"NSRSBH":"91450100MA5L100048","LRSJ":"2020-04-13"},{"NSRSBH":"91469006MA5T100049","LRSJ":"2020-04-13"},{"NSRSBH":"91460200MA5T100050","LRSJ":"2020-04-13"}]
    #lists = [{"NSRSBH": "120109066870104324"},
             #{"NSRSBH": "120113L83297104844"},
             #{"NSRSBH": "121000004660103721"},
             #{"NSRSBH": "123204004672106279"},
             #{"NSRSBH": "123205000141103223"},
             #{"NSRSBH": "123209237424108253"}]
    list1=[]
    i=0
    for dd in range(len(lists)):
        i+=1
        # print(str(lists[dd]["LRSJ"]))
        inlist = []
        outmap = {}
        # 获取和设置存储过程的入参和出参
        inlist.append(lists[dd]["NSRSBH"])
        inlist.append(str(lists[dd]["LRSJ"]))
        inlist.append("123")
        outmap["v_flag"] = "Float"
        outmap["v_remark"] = "String"
        # outmap["v_out_result"] = "String"
        # outmap["v_out"] = "String"
        # outmap["out_flag"] = "Float"
        # outmap["rate_1"] = "String"
        # outmap["ysxed"] = "String"
        # outmap["xypj_1"] = "String"

        # 调用存储过程
        result = conOracle.usePro("test_source/test_source@192.168.85.81:1521/emserver", "p_bzzb_cwbb", inlist, outmap)
        #result = conOracle.usePro("tjbank_test/tjbank_test@192.168.85.81:1521/emserver", "p_mx_tjyh_hbh", inlist, outmap)
        print(result)

        #验证存储过程是否调用成功
        if result[3] == 0.0:
            pass
        else:
            print("异常")


        sql2 = "select t.* from (select * from t_cwbb_zb where nsrsbh='%s' order by lrsj desc) t where rownum=1" % (lists[dd]["NSRSBH"])
        #sql2 = "select t.* from (select ysxed,code,reason,bz,djxh,nsrmc,frxm,frsfzjhm,sfzjlx,nsrsbh_wj,zchj_1,qbxse_6_avg,kyrq_1,hyml_1,jkze_1,zcfzl_1,qbxse_12_byxs,fr_chigu,fr_csrq,qbxse_zzl,xypf_1 from t_gsyh_result where NSRSBH='%s' and lrsj is not null order by lrsj desc) t where rownum=1" % (lists[dd]["NSRSBH"])

        print(sql2)
        all=conOracle.queryOracleAllReturnList("test_source/test_source@192.168.85.81:1521/emserver", sql2)
        #all = conOracle.queryOracleAllReturnList("tjbank_test/tjbank_test@192.168.85.81:1521/emserver", sql2)
        for le in all:
            map1={}
            keyall=""
            #map1["LRSJ"]=str(lists[dd]["LRSJ"])
            for d in le.keys():
                if d=="NSRSBH":
                    map1[d]=str(le[d])
                    keyall += d + ","
                elif d=="ID":
                    pass
                else:
                    map1[d] = d + "=" + str(le[d])
                    keyall += d + ","
            list1.append(map1)
            print(keyall[:-1])
        print(i)
    map={}
    map["sheet1"]=list1
    list=[]
    list.append(map)
    print(list)
    forExcel.getExcel(list)