"""导入要测试的函数"""
from city_functions import city_country
"""定义一个测试函数，其中参数为空，不接受参数"""
def test_city_country():
    """使用一个值来接收调用要测试的函数的返回结果"""
    ci_co=city_country('santiago','chile','500000')
    """判断被测试函数的返回结果是否等于预期值"""
    assert ci_co == 'santiago,chile-500000'