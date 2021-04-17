
from common.bases.base_page import BasePage
from locators.login_page_locator import LoginPageLocater
from locators.me_page_locator import MePageLocator
from locators.setting_page_locator import SettingPageLocator
from locators.main_page_locator import MainPageLocator
from run import logger


class Page_Action(BasePage):
    def login(self, username, password):
        self.send_data(LoginPageLocater.username_inputbox_loc, username)
        self.send_data(LoginPageLocater.password_loc, password)
        self.click_element(LoginPageLocater.login_btn_loc)
        self.sleep(3)

    # 判断是否用户已登录
    def is_user_login(self):
        try:
            logger.info('is search for element {}'.format(MePageLocator.click_to_login_loc))
            if self.search_element(MePageLocator.click_to_login_loc):
                logger.info('find the element {}'.format(MePageLocator.click_to_login_loc))
                return False  #未登录
        except Exception as e:
            logger.info('the element {} not found.'.format(MePageLocator.click_to_login_loc))
            logger.info(e)
            return True  #已登录





    #退出登录
    def logout(self):
        logger.info('begin to perform logout aperation')
        try:
            #点击 设置 按钮
            self.click_element(MePageLocator.setting_btn_loc)
            self.sleep(2)
            #点击 退出登录 按钮
            self.click_element(SettingPageLocator.logout_btn_loc)
            self.sleep(1)
            #点击 确定 按钮
            self.click_element(SettingPageLocator.confirm_btn_loc)
        except Exception as e:
            logger.info('element not found.')
            logger.info(e)



    #进入钓鱼人账号登录页面
    def go_to_login_page(self):
        #从钓鱼人首页进入“我的”按钮
        logger.info('进入 我的 页面')
        self.go_to_me_page()
        #判断用户是否已登录
        if self.is_user_login():
            #如果已登录，则退出登录
            self.logout()

        # 如果未登录，则点击  “点击登录”按钮
        self.click_element(MePageLocator.click_to_login_loc)
        self.sleep(2)
        #点击  钓鱼人账号登录
        self.click_element(LoginPageLocater.fishman_account_loc)
        self.sleep(2)



    def go_to_me_page(self):
        self.click_element((MainPageLocator.me_icon_loc))
        self.sleep(2)
    #点击 登录 按钮后，判断是否登录成功
    def is_nickname_exists(self):
        if self.search_element(MePageLocator.nickname_loc):
            return True
        else:
            return False








