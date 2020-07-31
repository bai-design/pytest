import pytest

datas = [["1710448461@qq.com"], ["1659935784@qq.com"]]
myids = ["email_address0", "eamil_address1"]
@pytest.mark.usefixtures("test_read_env")
class Test_browers(object):

    # @pytest.mark.flaky(reruns=3, reruns_delay=2)
    @pytest.mark.xfail(reason="no test", ids="测试人人网")
    # @pytest.mark.run(order=1)
    # @pytest.mark.dependency(name="test_default_get")
    def test_default_get(self, get_url):
        assert "renren" in get_url.current_url

    # @pytest.mark.dependency(depends=["test_default_get"])

    @pytest.mark.parametrize(argnames="get_url", argvalues=["https://www.baidu.com/","https://www.google.cn"],
                             indirect=True, ids=["测试百度", "测试谷歌"])
    # @pytest.mark.run(order=3)
    def test_much_get(self, get_url):
        assert get_url.current_url

    # @pytest.mark.run(order=2)
    @pytest.mark.xfail(reason="no test")
    @pytest.mark.funny
    def test_math(self):
        assert True

    def test_env(self, test_read_env):
        print(f'url: {test_read_env["info"]["url"]}')
        print(f'ids: {test_read_env["info"]["ids"]}')

    def test_param(self, param):
        print(f"message:{param}")
