from selenium.webdriver.common.by import By

class LoginPageLocater:
    # 钓鱼人账号登录：id = 	com.lchr.diaoyu:id/tv_account_login
    fishman_account_loc = (By.ID,"com.lchr.diaoyu:id/tv_account_login")
    #用户输入框定位：id= com.lchr.diaoyu:id/user_id
    username_inputbox_loc = (By.ID,"com.lchr.diaoyu:id/user_id")
    #密码输入框
    password_inputbox_loc = (By.ID, "com.lchr.diaoyu: id / passwd_id")
    #登录按钮
    login_loc_btn = (By.ID, "com.lchr.diaoyu: id / btn_login")