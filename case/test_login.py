from test_data.test_data import success_data
from test_data.test_data import failed_data
from run import logger
import pytest

#���� �������˺ŵ�¼  ҳ��
@pytest.fixture(scope='module')
def prepare_to_login(handler):
    handler[1].go_to_login_page()


#ִ�е�¼���û����������¼����
@pytest.mark.usefixtures('prepare_to_login')
class TestLogin:
    def test_login_success(self,handler):
        handler[1].login(success_data['username'],success_data['password'])
        logger.info("�û����������������ѵ����¼��ť ��������Ҫ�ж��Ƿ��¼�ɹ�")
        assert handler[1].is_nickname_exists()

