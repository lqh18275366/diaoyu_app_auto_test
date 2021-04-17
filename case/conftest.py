import pytest
from appium import webdriver
import time
from pages.page_action import Page_Action


#启动钓鱼人app的启动，进入首页
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
        #页面操作类 进行实例化
        pa = Page_Action()
        time.sleep(3)
        yield driver,pa
        driver.quit()
#控制测试用例的mark执行顺序，config是什么意思
def pytest_configure(config):
        #多个标识：仅执行smoke修饰的用例，登录成功的方法最后执行
        markers = ['smoke','last'] #冒烟测试、最后执行
        #遍历
        for mark in markers:
                config.addinivalue_line('markers',mark)