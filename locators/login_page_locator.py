from selenium.webdriver.common.by import By

class LoginPageLocater:
    # �������˺ŵ�¼��id = 	com.lchr.diaoyu:id/tv_account_login
    fishman_account_loc = (By.ID,"com.lchr.diaoyu:id/tv_account_login")
    #�û������λ��id= com.lchr.diaoyu:id/user_id
    username_inputbox_loc = (By.ID,"com.lchr.diaoyu:id/user_id")
    #���������
    password_inputbox_loc = (By.ID, "com.lchr.diaoyu: id / passwd_id")
    #��¼��ť
    login_loc_btn = (By.ID, "com.lchr.diaoyu: id / btn_login")