from pyclass import conDb2
if __name__ == '__main__':
    sql = "SELECT index_code,index_value FROM T_ZX_INDEX_RESULT where nsrsbh='9136071111111110TT'"
    resultsql = conDb2.queryDbAllReturnList("192.168.85.199", "50000", "zx_gxt", "zx_gxt199", "SAMPLE", sql)
    print(resultsql)
    mapre={}
    for resultva in resultsql:
        mapre[resultva["INDEX_CODE"]]=resultva["INDEX_VALUE"]
    print(mapre)