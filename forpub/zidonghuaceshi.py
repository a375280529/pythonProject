#!/usr/bin/python
# -*- coding: utf-8 -*-

from pyclass import conOracle,forExcel

if __name__ == '__main__':
    # aa="sw_cwbb_zsbzsbl,sw_cwbb_xjldfzl,sw_cwbb_ldbl,sw_cwbb_sdbl,sw_cwbb_zcfzl,sw_cwbb_zqfzl,sw_cwbb_cqbl,sw_cwbb_zxjzzwl,sw_cwbb_yhlxbs,sw_cwbb_cqfzyyzjbl,sw_cwbb_zzzjzwb,sw_cwbb_yxzczwl,sw_cwbb_yhfzzcb,sw_cwbb_zhzwfgb,sw_cwbb_zhzwzbjzb,sw_cwbb_zewbebitda,sw_cwbb_chldfzb,sw_cwbb_xjbl,sw_cwbb_jksrb,sw_cwbb_zqjksrb,sw_cwbb_dqjksrb,sw_cwbb_qtzfksrb,sw_cwbb_yfgzsrb,sw_cwbb_yfsjsrb,sw_cwbb_cqzbfzl,sw_cwbb_lxbzbs,sw_cwbb_ebitbdqjk,sw_cwbb_dqjkbebit,sw_cwbb_zzlrzjkb,sw_cwbb_srlxbzbs,sw_cwbb_xsqlrfzb,sw_cwbb_sqlrzjkb,sw_cwbb_yylrzjkb,sw_cwbb_yylrfzb,sw_cwbb_yylrjjkb,sw_cwbb_zzlrzjkb_2,sw_cwbb_kczszkhdfzbl,sw_cwbb_xjb,sw_cwbb_qzfzbl,sw_cwbb_ldzczb,sw_cwbb_ldfzzb,sw_cwbb_gdzcqzbl,sw_cwbb_ldfzl,sw_cwbb_zzzbzb,sw_cwbb_zhfzjg,sw_cwbb_szzqzbl,sw_cwbb_fxzwjgb,sw_cwbb_zjkqyb,sw_cwbb_jjkqyb,sw_cwbb_fldfzqzb,sw_cwbb_zqfzzcb,sw_cwbb_zzczzl,sw_cwbb_zszkzzl,sw_cwbb_ldzczzl,sw_cwbb_szzqzzzl,sw_cwbb_gdzczzl,sw_cwbb_chzzl_cb,sw_cwbb_yfzkzzl,sw_cwbb_yysrzzjkb,sw_cwbb_zzczzts,sw_cwbb_yszkzzts,sw_cwbb_ldzczzts,sw_cwbb_szzqzzzts,sw_cwbb_gdzczzts,sw_cwbb_chzzts_cb,sw_cwbb_zzczzl_1,sw_cwbb_zszkzzl_2,sw_cwbb_ldzczzl_1,sw_cwbb_szzqzzzl_1,sw_cwbb_gdzczzl_1,sw_cwbb_dqjkxjbl,sw_cwbb_sdzczb,sw_cwbb_yyzbsrb,sw_cwbb_srfyb,sw_cwbb_zclrl,sw_cwbb_zzcszl,sw_cwbb_zzcjll,sw_cwbb_zzcbcl,sw_cwbb_zcjll,sw_cwbb_zcjll_1,sw_cwbb_sqxsjll,sw_cwbb_sqzzcjll,sw_cwbb_zzmll,sw_cwbb_xsjll,sw_cwbb_xsfzbl,sw_cwbb_zzwszbl,sw_cwbb_tzszbl,sw_cwbb_sxfzbl,sw_cwbb_qtzwlrbl,sw_cwbb_xsqlrl,sw_cwbb_glfzbl,sw_cwbb_zzsrchb,sw_cwbb_zskzzzcbbl,sw_cwbb_chzzzcbbl,sw_cwbb_zfzkzzzcbbl,sw_cwbb_bwfzbl,sw_cwbb_sqlrl,sw_cwbb_jzcszlv,sw_cwbb_zczzlrlv,sw_cwbb_jzcszl_1,sw_cwbb_zzczzlv,sw_cwbb_zzsrzzl,sw_cwbb_zszktbzzl,sw_cwbb_yuszkzzl,sw_cwbb_zfkzzlv,sw_cwbb_chtbzzlv,sw_cwbb_zzlrzzlv,sw_cwbb_szzqzzzlv,sw_cwbb_lrzezzlv,sw_cwbb_jzcszlzzlv,sw_cwbb_qtywsrzzl,sw_cwbb_zzwsrzzlv,sw_cwbb_jlrzzlv,sw_cwbb_gdzczzlv,sw_cwbb_xjzhq,sw_cwbb_glfyzzc,sw_cwbb_glfyfzhj,sw_cwbb_sszbsr,sw_cwbb_wfplrzchj,sw_cwbb_jlrzchj,sw_cwbb_yszkyysr,sw_cwbb_ljzjzzc,sw_cwbb_ldzcyysr,sw_cwbb_sdszchj,sw_cwbb_ljzjzjzchj,SW_CWBB_LRSRBL_A,sw_cwbb_xsjll_2,sw_cwbb_yysryszkppl_a,sw_cwbb_yszkzzl_a,sw_cwbb_gdzcbcl_a,sw_cwbb_gdzczzl_a,sw_cwbb_mllzzl_a,sw_cwbb_wfplrbhl_a,sw_cwbb_ldfzyysr_qj,sw_cwbb_ldbl_qj,sw_cwbb_glfyzchj_qj,sw_cwbb_jlrsyzqy_qj,sw_cwbb_ljzjsyzqy_qj,sw_cwbb_mllhy,sw_cwbb_syzqy_last,sw_cwbb_glfzbl_qj,sw_cwbb_jlrl_01s,SW_CWBB_CHZZL_SR,SW_CWBB_YFZKZZTS,SW_CWBB_ZQZCSHL,SW_CWBB_CBSFQS,SW_CWBB_JLRL_02J,SW_CWBB_JLRL_01J,SW_CWBB_HBZJFGZGXC_CZ,SW_CWBB_YYZBZB_Y,SW_CWBB_LRB_SFQS,SW_CWBB_ZCFZB_SFQS,SW_CWBB_ZCFZB_SSQZ_MAX,SW_CWBB_ZCFZB_SSQQ_MIN,SW_CWBB_LRB_SSQZ_MAX,SW_CWBB_LRB_SSQQ_MIN,SW_CWBB_QTYSKBSSZBZBGJ,SW_CWBB_YSZKBXSSR,SW_CWBB_YSZKZZBXSSRZZ,SW_CWBB_SFYCB,SW_CWBB_YYLRZCHJ_Y,SW_CWBB_DQJKZCHJ_Y,SW_CWBB_JYYZB_ZZL_Y,SW_CWBB_YXZCFZL_QJ,SW_CWBB_HYYYSRCHB,SW_CWBB_XSQLRL_M,SW_CWBB_ZCFZL_M,SW_CWBB_MLL,SW_CWBB_QYZZL,SW_CWBB_SYZQY_ZZL_Y"
    #
    # print(len(aa.split(",")))

    # sql1="select nsrsbh,lrsj from zx_nsrjcxx where rownum<=200"

    sql2=""

    # re=conOracle.queryOracleAllReturnList("test_source/test_source@192.168.85.81:1521/emserver", sql1)
    lists=[{"NSRSBH":"120109066870104324","LRSJ":"2020-04-13"},{"NSRSBH":"120113L83297104844","LRSJ":"2020-04-13"},{"NSRSBH":"121000004660103721","LRSJ":"2020-04-13"},{"NSRSBH":"123204004672106279","LRSJ":"2020-04-13"},{"NSRSBH":"123205000141103223","LRSJ":"2020-04-13"},{"NSRSBH":"123209237424108253","LRSJ":"2020-04-13"}]
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
        result = conOracle.usePro("vzoom/vzoom2020@192.168.85.96:1521/vzoom", "P_BZZB_CWBB", inlist, outmap)
        #result = conOracle.usePro("tjbank_test/tjbank_test@192.168.85.81:1521/emserver", "p_mx_tjyh_hbh", inlist, outmap)
        print(result)
        #验证存储过程是否调用成功
        if result[3] == 0.0:
            pass
        else:
            print("异常")


        sql2 = "select t.* from (select NSRSBH,sw_cwbb_zsbzsbl,sw_cwbb_xjldfzl,sw_cwbb_ldbl,sw_cwbb_sdbl,sw_cwbb_zcfzl,sw_cwbb_zqfzl,sw_cwbb_cqbl,sw_cwbb_zxjzzwl,sw_cwbb_yhlxbs,sw_cwbb_cqfzyyzjbl,sw_cwbb_zzzjzwb,sw_cwbb_yxzczwl,sw_cwbb_yhfzzcb,sw_cwbb_zhzwfgb,sw_cwbb_zhzwzbjzb,sw_cwbb_zewbebitda,sw_cwbb_chldfzb,sw_cwbb_xjbl,sw_cwbb_jksrb,sw_cwbb_zqjksrb,sw_cwbb_dqjksrb,sw_cwbb_qtzfksrb,sw_cwbb_yfgzsrb,sw_cwbb_yfsjsrb,sw_cwbb_cqzbfzl,sw_cwbb_lxbzbs,sw_cwbb_ebitbdqjk,sw_cwbb_dqjkbebit,sw_cwbb_zzlrzjkb,sw_cwbb_srlxbzbs,sw_cwbb_xsqlrfzb,sw_cwbb_sqlrzjkb,sw_cwbb_yylrzjkb,sw_cwbb_yylrfzb,sw_cwbb_yylrjjkb,sw_cwbb_zzlrzjkb_2,sw_cwbb_kczszkhdfzbl,sw_cwbb_xjb,sw_cwbb_qzfzbl,sw_cwbb_ldzczb,sw_cwbb_ldfzzb,sw_cwbb_gdzcqzbl,sw_cwbb_ldfzl,sw_cwbb_zzzbzb,sw_cwbb_zhfzjg,sw_cwbb_szzqzbl,sw_cwbb_fxzwjgb,sw_cwbb_zjkqyb,sw_cwbb_jjkqyb,sw_cwbb_fldfzqzb,sw_cwbb_zqfzzcb,sw_cwbb_zzczzl,sw_cwbb_zszkzzl,sw_cwbb_ldzczzl,sw_cwbb_szzqzzzl,sw_cwbb_gdzczzl,sw_cwbb_chzzl_cb,sw_cwbb_yfzkzzl,sw_cwbb_yysrzzjkb,sw_cwbb_zzczzts,sw_cwbb_yszkzzts,sw_cwbb_ldzczzts,sw_cwbb_szzqzzzts,sw_cwbb_gdzczzts,sw_cwbb_chzzts_cb,sw_cwbb_zzczzl_1,sw_cwbb_zszkzzl_2,sw_cwbb_ldzczzl_1,sw_cwbb_szzqzzzl_1,sw_cwbb_gdzczzl_1,sw_cwbb_dqjkxjbl,sw_cwbb_sdzczb,sw_cwbb_yyzbsrb,sw_cwbb_srfyb,sw_cwbb_zclrl,sw_cwbb_zzcszl,sw_cwbb_zzcjll,sw_cwbb_zzcbcl,sw_cwbb_zcjll,sw_cwbb_zcjll_1,sw_cwbb_sqxsjll,sw_cwbb_sqzzcjll,sw_cwbb_zzmll,sw_cwbb_xsjll,sw_cwbb_xsfzbl,sw_cwbb_zzwszbl,sw_cwbb_tzszbl,sw_cwbb_sxfzbl,sw_cwbb_qtzwlrbl,sw_cwbb_xsqlrl,sw_cwbb_glfzbl,sw_cwbb_zzsrchb,sw_cwbb_zskzzzcbbl,sw_cwbb_chzzzcbbl,sw_cwbb_zfzkzzzcbbl,sw_cwbb_bwfzbl,sw_cwbb_sqlrl,sw_cwbb_jzcszlv,sw_cwbb_zczzlrlv,sw_cwbb_jzcszl_1,sw_cwbb_zzczzlv,sw_cwbb_zzsrzzl,sw_cwbb_zszktbzzl,sw_cwbb_yuszkzzl,sw_cwbb_zfkzzlv,sw_cwbb_chtbzzlv,sw_cwbb_zzlrzzlv,sw_cwbb_szzqzzzlv,sw_cwbb_lrzezzlv,sw_cwbb_jzcszlzzlv,sw_cwbb_qtywsrzzl,sw_cwbb_zzwsrzzlv,sw_cwbb_jlrzzlv,sw_cwbb_gdzczzlv,sw_cwbb_xjzhq,sw_cwbb_glfyzzc,sw_cwbb_glfyfzhj,sw_cwbb_sszbsr,sw_cwbb_wfplrzchj,sw_cwbb_jlrzchj,sw_cwbb_yszkyysr,sw_cwbb_ljzjzzc,sw_cwbb_ldzcyysr,sw_cwbb_sdszchj,sw_cwbb_ljzjzjzchj,SW_CWBB_LRSRBL_A,sw_cwbb_xsjll_2,sw_cwbb_yysryszkppl_a,sw_cwbb_yszkzzl_a,sw_cwbb_gdzcbcl_a,sw_cwbb_gdzczzl_a,sw_cwbb_mllzzl_a,sw_cwbb_wfplrbhl_a,sw_cwbb_ldfzyysr_qj,sw_cwbb_ldbl_qj,sw_cwbb_glfyzchj_qj,sw_cwbb_jlrsyzqy_qj,sw_cwbb_ljzjsyzqy_qj,sw_cwbb_mllhy,sw_cwbb_syzqy_last,sw_cwbb_glfzbl_qj,sw_cwbb_jlrl_01s,SW_CWBB_CHZZL_SR,SW_CWBB_YFZKZZTS,SW_CWBB_ZQZCSHL,SW_CWBB_CBSFQS,SW_CWBB_JLRL_02J,SW_CWBB_JLRL_01J,SW_CWBB_HBZJFGZGXC_CZ,SW_CWBB_YYZBZB_Y,SW_CWBB_LRB_SFQS,SW_CWBB_ZCFZB_SFQS,SW_CWBB_ZCFZB_SSQZ_MAX,SW_CWBB_ZCFZB_SSQQ_MIN,SW_CWBB_LRB_SSQZ_MAX,SW_CWBB_LRB_SSQQ_MIN,SW_CWBB_QTYSKBSSZBZBGJ,SW_CWBB_YSZKBXSSR,SW_CWBB_YSZKZZBXSSRZZ,SW_CWBB_SFYCB,SW_CWBB_YYLRZCHJ_Y,SW_CWBB_DQJKZCHJ_Y,SW_CWBB_JYYZB_ZZL_Y,SW_CWBB_YXZCFZL_QJ,SW_CWBB_HYYYSRCHB,SW_CWBB_XSQLRL_M,SW_CWBB_ZCFZL_M,SW_CWBB_MLL,SW_CWBB_QYZZL,SW_CWBB_SYZQY_ZZL_Y from t_cwbb_zb where nsrsbh='%s' order by lrsj desc) t where rownum=1" % (lists[dd]["NSRSBH"])
        #sql2 = "select t.* from (select ysxed,code,reason,bz,djxh,nsrmc,frxm,frsfzjhm,sfzjlx,nsrsbh_wj,zchj_1,qbxse_6_avg,kyrq_1,hyml_1,jkze_1,zcfzl_1,qbxse_12_byxs,fr_chigu,fr_csrq,qbxse_zzl,xypf_1 from t_gsyh_result where NSRSBH='%s' and lrsj is not null order by lrsj desc) t where rownum=1" % (lists[dd]["NSRSBH"])

        print(sql2)
        all=conOracle.queryOracleAllReturnList("vzoom/vzoom2020@192.168.85.96:1521/vzoom", sql2)
        #all = conOracle.queryOracleAllReturnList("tjbank_test/tjbank_test@192.168.85.81:1521/emserver", sql2)
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