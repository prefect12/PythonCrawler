import re

def listProcess(listString):
    func = lambda x: re.sub('\\xa0|\\r|\\n| |','',x)
    resultList = [func(i) for i in listString]
    return [i for i in resultList if len(i) > 1]


if __name__ == "__main__":
    testString = ['深圳\xa0\xa0', '\xa0\xa05-7年经验\xa0\xa0', '\xa0\xa0本科\xa0\xa0', '\xa0\xa0招若干人\xa0\xa0', '\xa0\xa005-25发布']
    test = ['1.\xa0至少1个完整MDM项目实施经验，熟悉掌握MDM理论和实施方法论；', '2.\xa0熟悉Oracle、Mysql、SQLServer等至少一种大型数据库，熟悉SQL语言；', '3.\xa0熟悉ETL处理工具的使用；', '4.\xa0熟悉数据模型、数据标准、数据质量、元数据、主数据等数据治理相关领域的知识。', '5.\xa0熟悉房地产成本、招采、销售、计划等业务系统逻辑；']
    print(listProcess(test))