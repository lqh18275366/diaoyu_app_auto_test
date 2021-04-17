#在首页定位页面元素

from selenium.webdriver.common.by import By
class MainPageLocator:
    #定位钓鱼人“我的”页面元素id=com.lchr.diaoyu:id/btn_tab_mine
    me_icon_loc = (By.ID,'com.lchr.diaoyu:id/btn_tab_mine')