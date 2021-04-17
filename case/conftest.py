import pytest
from appium import webdriver
import time
from pages.page_action import Page_Action


#����������app��������������ҳ
@pytest.fixture(scope="session")
def handler():
        caps = {"platformName": "Android",
                "platformVersion": "5",
                "deviceName": "127.0.0.1:21503",
                "appPackage": "com.lchr.diaoyu",
                "appActivity": "com.lchr.diaoyu.SplashActivity",
                "noReset": True,
                "newCommandTimeout": 6000,
                "skipServerInstallation": True,
                "automationName": "UiAutomator2",
                "ensureWebviewsHavePages": True
                }

        url = "http://127.0.0.1:4723/wd/hub"

        driver = webdriver.Remote(url, caps)
        #ҳ������� ����ʵ����
        pa = Page_Action()
        time.sleep(3)
        yield driver,pa
        driver.quit()
#���Ʋ���������markִ��˳��config��ʲô��˼
def pytest_configure(config):
        #�����ʶ����ִ��smoke���ε���������¼�ɹ��ķ������ִ��
        markers = ['smoke','last'] #ð�̲��ԡ����ִ��
        #����
        for mark in markers:
                config.addinivalue_line('markers',mark)