from selenium.webdriver.common.by import By

class MePageLocator:
    #在“我的”页面定位元素“设置”按钮
    setting_btn_loc = (By.ID,'com.lchr.diaoyu:id/iv_top_navi_setting')

    #点击“登录”：id = 	com.lchr.diaoyu:id/tv_click2login
    click_to_login_loc = (By.ID,'com.lchr.diaoyu:id/tv_click2login')

    #在 我的 页面定位昵称 ：nickname_loc
    nickname_loc = (By.ID, 'com.lchr.diaoyu:id/user_nick_name')



