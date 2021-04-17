from selenium.webdriver.common.by import By
class SettingPageLocator:
    #退出登录：id=com.lchr.diaoyu:id/rtv_setting_logout
    logout_btn_loc = (By.ID,"com.lchr.diaoyu:id/rtv_setting_logout")
    #确定：id=android:id/button1
    confirm_btn_loc = (By.ID,"id=android:id/button1")
    #取消