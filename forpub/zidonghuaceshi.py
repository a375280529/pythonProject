#!/usr/bin/python
# -*- coding: utf-8 -*-

from pyclass import conOracle,forExcel

if __name__ == '__main__':
    # aa="sw_jcxx_nsrjcxx_sfqs,sw_jcxx_nsrmc,sw_jcxx_clnx,sw_jcxx_hy,sw_jcxx_nsrxypj,sw_jcxx_nsrztdm,sw_jcxx_nsrlxdm,sw_jcxx_djzclxdm,sw_jcxx_djzclxmc,sw_jcxx_xzqh,sw_jcxx_sfzzy_a,sw_jcxx_sfgtgsh,sw_lxr_lxrxx_sfqs,sw_lxr_frxm,sw_lxr_frnl,sw_lxr_frzjhm,sw_tzf_tzfxx_sfqs,sw_tzf_frtzbl,sw_tzf_frtzbl_hmxm,sw_tzf_gqfsd,sw_tzf_tzfjjxzlx,sw_bg_fr_01m,sw_bg_fr_02m,sw_bg_fr_03m,sw_bg_fr_06m,sw_bg_fr_09m,sw_bg_fr_12m,sw_bg_fr_15m,sw_bg_fr_18m,sw_bg_fr_21m,sw_bg_fr_24m,sw_bg_cwfzr_01m,sw_bg_cwfzr_03m,sw_bg_cwfzr_06m,sw_bg_cwfzr_12m,sw_bg_cwfzr_24m,sw_bg_hy_01m,sw_bg_hy_02m,sw_bg_hy_03m,sw_bg_hy_06m,sw_bg_hy_09m,sw_bg_hy_12m,sw_bg_hy_15m,sw_bg_hy_18m,sw_bg_hy_21m,sw_bg_hy_24m,sw_bg_jydz_01m,sw_bg_jydz_03m,sw_bg_jydz_06m,sw_bg_jydz_12m,sw_bg_jydz_24m,sw_bg_bsry_12m,sw_bg_frbgjjts,sw_wfwz_01m,sw_wfwz_02m,sw_wfwz_03m,sw_wfwz_06m,sw_wfwz_09m,sw_wfwz_12m,sw_wfwz_15m,sw_wfwz_18m,sw_wfwz_21m,sw_wfwz_24m,sw_wfwz_yz_01m,sw_wfwz_yz_02m,sw_wfwz_yz_03m,sw_wfwz_yz_06m,sw_wfwz_yz_09m,sw_wfwz_yz_12m,sw_wfwz_yz_15m,sw_wfwz_yz_18m,sw_wfwz_yz_21m,sw_wfwz_yz_24m,sw_wfwz_jjys"
    #
    # print(len(aa.split(",")))

    # sql1="select nsrsbh,lrsj from zx_nsrjcxx where rownum<=200"

    sql2=""

    # re=conOracle.queryOracleAllReturnList("test_source/test_source@192.168.85.81:1521/emserver", sql1)
    #lists=[{"NSRSBH":"913307005669107196","LRSJ":"2020-04-13"},{"NSRSBH":"91430722MA4M105325","LRSJ":"2020-04-13"},{"NSRSBH":"913211813462100351","LRSJ":"2020-04-13"},{"NSRSBH":"913205945618109539","LRSJ":"2020-04-13"},{"NSRSBH":"915301276787105486","LRSJ":"2020-04-13"},{"NSRSBH":"911201037128101150","LRSJ":"2020-04-13"}]
    lists = [{"NSRSBH": "913307005669107196"},
             {"NSRSBH": "91430722MA4M105325"},
             {"NSRSBH": "913211813462100351"},
             {"NSRSBH": "913205945618109539"},
             {"NSRSBH": "915301276787105486"},
             {"NSRSBH": "911201037128101150"}]
    list1=[]
    i=0
    for dd in range(len(lists)):
        i+=1
        # print(str(lists[dd]["LRSJ"]))
        inlist = []
        outmap = {}
        # 获取和设置存储过程的入参和出参
        inlist.append(lists[dd]["NSRSBH"])
        # inlist.append(str(lists[dd]["LRSJ"]))
        # inlist.append("123")

        outmap["v_out_result"] = "String"
        outmap["v_out"] = "String"
        outmap["out_flag"] = "Float"
        outmap["rate_1"] = "String"
        outmap["ysxed"] = "String"
        outmap["xypj_1"] = "String"

        # 调用存储过程
        #result = conOracle.usePro("test_source/test_source@192.168.85.81:1521/emserver", "P_BZZB_CWBB", inlist, outmap)
        result = conOracle.usePro("tjbank_test/tjbank_test@192.168.85.81:1521/emserver", "p_mx_tjyh_hbh", inlist, outmap)
        print(result)
        # 验证存储过程是否调用成功
        # if result[3] == 0.0:
        #     pass
        # else:
        #     print("异常")


        #sql2 = "select t.* from (select nsrsbh,SW_CWBB_ZSBZSBL,SW_CWBB_XJLDFZL,SW_CWBB_LDBL,SW_CWBB_SDBL,SW_CWBB_ZCFZL,SW_CWBB_ZQFZL,SW_CWBB_CQBL,SW_CWBB_ZXJZZWL,SW_CWBB_YHLXBS,SW_CWBB_CQFZYYZJBL,SW_CWBB_ZZZJZWB,SW_CWBB_YXZCZWL,SW_CWBB_YHFZZCB,SW_CWBB_ZHZWFGB,SW_CWBB_ZHZWZBJZB,SW_CWBB_ZEWBEBITDA,SW_CWBB_CHLDFZB,SW_CWBB_XJBL,SW_CWBB_JKSRB,SW_CWBB_ZQJKSRB,SW_CWBB_DQJKSRB,SW_CWBB_QTZFKSRB,SW_CWBB_YFGZSRB,SW_CWBB_YFSJSRB,SW_CWBB_CQZBFZL,SW_CWBB_LXBZBS,SW_CWBB_EBITBDQJK,SW_CWBB_DQJKBEBIT,SW_CWBB_ZZLRZJKB,SW_CWBB_SRLXBZBS,SW_CWBB_XSQLRFZB,SW_CWBB_SQLRZJKB,SW_CWBB_YYLRZJKB,SW_CWBB_YYLRFZB,SW_CWBB_YYLRJJKB,SW_CWBB_ZZLRZJKB_2,SW_CWBB_KCZSZKHDFZBL,SW_CWBB_XJB,SW_CWBB_QZFZBL,SW_CWBB_LDZCZB,SW_CWBB_LDFZZB,SW_CWBB_GDZCQZBL,SW_CWBB_LDFZL,SW_CWBB_ZZZBZB,SW_CWBB_ZHFZJG,SW_CWBB_SZZQZBL,SW_CWBB_FXZWJGB,SW_CWBB_ZJKQYB,SW_CWBB_JJKQYB,SW_CWBB_FLDFZQZB,SW_CWBB_ZQFZZCB,SW_CWBB_ZZCZZL,SW_CWBB_ZSZKZZL,SW_CWBB_LDZCZZL,SW_CWBB_SZZQZZZL,SW_CWBB_GDZCZZL,SW_CWBB_CHZZL_CB,SW_CWBB_YFZKZZL,SW_CWBB_YYSRZZJKB,SW_CWBB_ZZCZZTS,SW_CWBB_YSZKZZTS,SW_CWBB_LDZCZZTS,SW_CWBB_SZZQZZZTS,SW_CWBB_GDZCZZTS,SW_CWBB_CHZZTS_CB,SW_CWBB_ZZCZZL_1,SW_CWBB_ZSZKZZL_2,SW_CWBB_LDZCZZL_1,SW_CWBB_SZZQZZZL_1,SW_CWBB_GDZCZZL_1,SW_CWBB_DQJKXJBL,SW_CWBB_SDZCZB,SW_CWBB_YYZBSRB,SW_CWBB_SRFYB,SW_CWBB_ZCLRL,SW_CWBB_ZZCSZL,SW_CWBB_ZZCJLL,SW_CWBB_ZZCBCL,SW_CWBB_ZCJLL,SW_CWBB_ZCJLL_1,SW_CWBB_SQXSJLL,SW_CWBB_SQZZCJLL,SW_CWBB_ZZMLL,SW_CWBB_XSJLL,SW_CWBB_XSFZBL,SW_CWBB_ZZWSZBL,SW_CWBB_TZSZBL,SW_CWBB_SXFZBL,SW_CWBB_QTZWLRBL,SW_CWBB_XSQLRL,SW_CWBB_GLFZBL,SW_CWBB_ZZSRCHB,SW_CWBB_ZSKZZZCBBL,SW_CWBB_CHZZZCBBL,SW_CWBB_ZFZKZZZCBBL,SW_CWBB_BWFZBL,SW_CWBB_SQLRL,SW_CWBB_JZCSZLV,SW_CWBB_ZCZZLRLV,SW_CWBB_JZCSZL_1,SW_CWBB_ZZCZZLV,SW_CWBB_ZZSRZZL,SW_CWBB_ZSZKTBZZL,SW_CWBB_YUSZKZZL,SW_CWBB_ZFKZZLV,SW_CWBB_CHTBZZLV,SW_CWBB_ZZLRZZLV,SW_CWBB_SZZQZZZLV,SW_CWBB_LRZEZZLV,SW_CWBB_JZCSZLZZLV,SW_CWBB_QTYWSRZZL,SW_CWBB_ZZWSRZZLV,SW_CWBB_JLRZZLV,SW_CWBB_GDZCZZLV,SW_CWBB_XJZHQ,SW_CWBB_GLFYZZC,SW_CWBB_GLFYFZHJ,SW_CWBB_SSZBSR,SW_CWBB_WFPLRZCHJ,SW_CWBB_JLRZCHJ,SW_CWBB_YSZKYYSR,SW_CWBB_LJZJZZC,SW_CWBB_LDZCYYSR,SW_CWBB_SDSZCHJ,SW_CWBB_LJZJZJZCHJ,SW_CWBB_LRSRBL_A,SW_CWBB_XSJLL_2,SW_CWBB_YYSRYSZKPPL_A,SW_CWBB_YSZKZZL_A,SW_CWBB_GDZCBCL_A,SW_CWBB_GDZCZZL_A,SW_CWBB_MLLZZL_A,SW_CWBB_WFPLRBHL_A,SW_CWBB_LDFZYYSR_QJ,SW_CWBB_LDBL_QJ,SW_CWBB_GLFYZCHJ_QJ,SW_CWBB_JLRSYZQY_QJ,SW_CWBB_LJZJSYZQY_QJ,SW_CWBB_MLLHY,SW_CWBB_SYZQY_LAST,SW_CWBB_GLFZBL_QJ,SW_CWBB_JLRL_01S,SW_CWBB_CHZZL_SR,SW_CWBB_YFZKZZTS,SW_CWBB_ZQZCSHL,SW_CWBB_CBSFQS,SW_CWBB_JLRL_02J,SW_CWBB_JLRL_01J,SW_CWBB_HBZJFGZGXC_CZ,SW_CWBB_YYZBZB_Y,SW_CWBB_LRB_SFQS,SW_CWBB_ZCFZB_SFQS,SW_CWBB_ZCFZB_SSQZ_MAX,SW_CWBB_ZCFZB_SSQQ_MIN,SW_CWBB_LRB_SSQZ_MAX,SW_CWBB_LRB_SSQQ_MIN,SW_CWBB_QTYSKBSSZBZBGJ,SW_CWBB_YSZKBXSSR,SW_CWBB_YSZKZZBXSSRZZ,SW_CWBB_SFYCB,SW_CWBB_YYLRZCHJ_Y,SW_CWBB_DQJKZCHJ_Y,SW_CWBB_JYYZB_ZZL_Y,SW_CWBB_YXZCFZL_QJ,SW_CWBB_HYYYSRCHB,SW_CWBB_XSQLRL_M,SW_CWBB_ZCFZL_M,SW_CWBB_MLL,SW_CWBB_QYZZL,SW_CWBB_SYZQY_ZZL_Y FROM T_CWBB_ZB where nsrsbh='%s' order by lrsj desc) t where rownum=1" % (lists[dd]["NSRSBH"])
        sql2 = "select t.* from (select ysxed,code,reason,bz,djxh,nsrmc,frxm,frsfzjhm,sfzjlx,nsrsbh_wj,zchj_1,qbxse_6_avg,kyrq_1,hyml_1,jkze_1,zcfzl_1,qbxse_12_byxs,fr_chigu,fr_csrq,qbxse_zzl,xypf_1 from t_gsyh_result where NSRSBH='%s' and lrsj is not null order by lrsj desc) t where rownum=1" % (lists[dd]["NSRSBH"])

        print(sql2)
        # all=conOracle.queryOracleAllReturnList("test_source/test_source@192.168.85.81:1521/emserver", sql2)
        all = conOracle.queryOracleAllReturnList("tjbank_test/tjbank_test@192.168.85.81:1521/emserver", sql2)
        for le in all:
            map1={}
            #map1["LRSJ"]=str(lists[dd]["LRSJ"])
            for d in le.keys():
                if d=="NSRSBH":
                    map1[d]=str(le[d])
                else:
                    map1[d] = d + "=" + str(le[d])
            list1.append(map1)
        print(i)
    map={}
    map["sheet1"]=list1
    list=[]
    list.append(map)
    print(list)
    forExcel.getExcel(list)