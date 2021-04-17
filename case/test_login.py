from test_data.test_data import success_data
from test_data.test_data import failed_data
from run import logger
import pytest

#进入 钓鱼人账号登录  页面
@pytest.fixture(scope='module')
def prepare_to_login(handler):
    handler[1].go_to_login_page()


#执行登录的用户名和密码登录操作
@pytest.mark.usefixtures('prepare_to_login')
class TestLogin:
    def test_login_success(self,handler):
        handler[1].login(success_data['username'],success_data['password'])
        logger.info("用户名，密码输入且已点击登录按钮 ，后续需要判断是否登录成功")
        assert handler[1].is_nickname_exists()

