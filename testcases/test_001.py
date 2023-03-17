# -*- coding: utf-8 -*-
# @Time  : 2023/3/13 19:12
# Author : Adan

from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestClass:
    def setup(self):
        # 創建⼀個字典,⽤於存儲設備和應用訊息
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "11.0",
            "deviceName": "127.0.0.1:5555",
            "appPackage": "com.nineyi.shop.s002131",
            "appActivity": "com.nineyi.MainActivity"
        }

        # 與appium session之間建⽴聯繫，括號為appium服務地址
        global driver
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        # 进入app，輸入手機號碼 and 登入
        driver.find_element(MobileBy.ID,"com.nineyi.shop.s002131:id/close_btn").click()
        time.sleep(5)
        #driver.find_element(MobileBy.ID,"com.nineyi.shop.s002131:id/bottom_navigation_view_item_text").click()
        driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("我的帳戶")').click()
        time.sleep(5)
        driver.find_element(MobileBy.ID,"com.nineyi.shop.s002131:id/id_et_input").send_keys("0919541317")
        time.sleep(5)
        driver.find_element(MobileBy.ID,"com.nineyi.shop.s002131:id/id_btn_login").click()
        time.sleep(3)
        driver.find_element(MobileBy.ID,"com.nineyi.shop.s002131:id/id_et_input").send_keys("dlink5229")
        time.sleep(5)
        driver.find_element(MobileBy.ID,"com.nineyi.shop.s002131:id/id_btn_input_passwd").click()
        time.sleep(5)

        # driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入您的手機號碼")').send_keys("0919541317")
        # time.sleep(2)
        # agree_locator = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("同意")')
        # WebDriverWait(driver, 10).until(EC.visibility_of_element_located(agree_locator)).click()
        # 点击我知道了按钮
        #driver.find_element(MobileBy.ACCESSIBILITY_ID,"关闭").click()
        # know_locator = (MobileBy.ACCESSIBILITY_ID, "关闭")
        # WebDriverWait(driver, 10).until(EC.visibility_of_element_located(know_locator)).click()
        #time.sleep(10)

        # 滑动屏幕，露出新品tab
        # x = driver.get_window_size()['width']
        # y = driver.get_window_size()['height']
        # driver.swipe(int(x * 0.5), int(y * 0.5), int(x * 0.5), int(y * 0.1), duration=500)

        # 点击手机数码tab
        #driver.find_element(MobileBy.XPATH,'//android.widget.RelativeLayout[@content-desc="苏宁超市"]/android.widget.ImageView').click()
        # newcomm_locator = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("手机数码")')
        # WebDriverWait(driver, 10).until(EC.visibility_of_element_located(newcomm_locator)).click()
       # time.sleep(3)

    def test_001(self):
        # 獲取登入後eshop會員卡
        home_name_locator = (MobileBy.ID, "com.nineyi.shop.s002131:id/membercard_card_front_img")
        home_name = (WebDriverWait(driver, 10).until(EC.visibility_of_element_located(home_name_locator))).text
        print(home_name)
        time.sleep(5)
        homep = (MobileBy.XPATH,'//android.view.ViewGroup[@content-desc="tabBarHome"]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(homep)).click()
        time.sleep(3)
        #彈出關閉 截圖提醒
        popupclose = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("關閉")')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(popupclose)).click()
        time.sleep(3)
        # 點選熱銷排行
        hotInfo_locator = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("熱銷排行")')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(hotInfo_locator)).click()
        time.sleep(2)
        # 獲取折扣活動
        discountInfo_locator = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("折扣活動")')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(discountInfo_locator)).click()
        time.sleep(2)
        #
        # # 获取详情页商品名称
        # pageInfo_name_locator = (MobileBy.ID, 'com.suning.mobile.ebuy:id/tv_1')
        # pageInfo_name = (WebDriverWait(driver, 10).until(EC.visibility_of_element_located(pageInfo_name_locator))).text
        # print(pageInfo_name)
        #
        # # 断言首页商品名称等于详情页商品名称
        # assert home_name == pageInfo_name, f"预期名称为{home_name}，实际结果为{pageInfo_name}"

    def test_002(self):

        homep2 = (MobileBy.XPATH,'//android.view.ViewGroup[@content-desc="tabBarHome"]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(homep2)).click()
        time.sleep(3)
        # 彈出關閉
        popupclose = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("關閉")')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(popupclose)).click()
        #領折價券
        discountcoupon_locator = (MobileBy.ID, 'com.nineyi.shop.s002131:id/brand_link_btn2')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(discountcoupon_locator)).click()
        time.sleep(2)

    def test_003(self):
        homep3 = (MobileBy.XPATH,'//android.view.ViewGroup[@content-desc="tabBarHome"]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(homep3)).click()
        time.sleep(5)
        #彈出關閉
        popupclose = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("關閉")')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(popupclose)).click()
        time.sleep(3)

        #點數兌換
        pointexchange_locator = (MobileBy.ID, 'com.nineyi.shop.s002131:id/brand_link_btn1')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(pointexchange_locator)).click()
        time.sleep(3)
        #我的帳戶
       # driver.find_element(MobileBy.XPATH,'//android.view.ViewGroup[@content-desc="tabBarMember"]/android.view.ViewGroup/android.widget.TextView').click()
        # member = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="tabBarMember"]/android.view.ViewGroup/android.widget.TextView')
        # WebDriverWait(driver, 10).until(EC.visibility_of_element_located(member)).click()
       # time.sleep(5)
        # 修改密碼
        # changepw = (MobileBy.XPATH, '//android.widget.FrameLayout[@content-desc="memberChangePwBtn"]/android.widget.RelativeLayout/android.widget.TextView')
        # WebDriverWait(driver, 10).until(EC.visibility_of_element_located(changepw)).click()
        # time.sleep(3)
        # driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("原始密碼")').send_keys("dlink5229")
        # time.sleep(3)
        # driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("輸入新密碼6-20碼英數字")').send_keys("icash1234")
        # time.sleep(3)
        # driver.find_element(MobileBy.ID, "com.nineyi.shop.s002131:id/id_btn_next").click()
        # time.sleep(3)
        # 領折價券
        # discountcoupon_locator = (MobileBy.ID, 'com.nineyi.shop.s002131:id/brand_link_btn2')
        # WebDriverWait(driver, 10).until(EC.visibility_of_element_located(discountcoupon_locator)).click()

    def test_004(self):
        homep4 = (MobileBy.XPATH,'//android.view.ViewGroup[@content-desc="tabBarHome"]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(homep4)).click()
        time.sleep(5)
        # 彈出關閉
        popupclose2 = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("關閉")')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(popupclose2)).click()
        time.sleep(3)

        # 買一送一
        driver.find_element(MobileBy.ID,'com.nineyi.shop.s002131:id/cms_item_view_carousel_img_left').click()
        time.sleep(4)

    def test_005(self):
        homep4 = (MobileBy.XPATH,'//android.view.ViewGroup[@content-desc="tabBarHome"]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(homep4)).click()
        time.sleep(5)
        # 彈出關閉
        popupclose2 = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("關閉")')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(popupclose2)).click()
        time.sleep(3)

        # 購物車
        
        #driver.find_element(MobileBy.ID, 'com.nineyi.shop.s002131:id/cms_item_view_carousel_img_left').click()
        driver.find_element(MobileBy.ACCESSIBILITY_ID,'tabBarCart').click()
        time.sleep(3)
        #定位商品價格元素
        item_price_element = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("NT$420")')

        #獲取商品價格本文
        item_price_text = item_price_element.text

        # 定義期望價格
        expected_price = "NT$410"

        # 判斷價格是否正確
        if item_price_text == expected_price:
            print("Item price is correct!")
        else:
            print(f"Item price is incorrect. Expected {expected_price}, but got {item_price_text}")
       

        #下一步
        driver.find_element(MobileBy.ID, "com.nineyi.shop.s002131:id/shoppingcart_next_step_button").click()
        time.sleep(3)

        #設定手機條碼載具
        #driver.find_element(MobileBy.ID,'com.nineyi.shop.s002131:id/memberzone_item_title').click()
        #driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("設定手機條碼載具")').click()
        # phonebarcodecarrier =(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("設定手機條碼載具")')
        # WebDriverWait(driver, 10).until(EC.visibility_of_element_located(phonebarcodecarrier)).click()
        #driver.find_element(MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[5]/android.widget.RelativeLayout/android.widget.TextView[1]').click()
        # time.sleep(3)
        # driver.find_element(MobileBy.ID, "com.nineyi.shop.s002131:id/carrier_edit_text").send_keys("/TD8U65Q")
        # time.sleep(2)
        # driver.find_element(MobileBy.ID, "com.nineyi.shop.s002131:id/dialog_positive_btn").click()
        # home_price_locator = (MobileBy.XPATH, '//android.widget.LinearLayout[@content-desc="CMSProduct2773391"]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView[2]')
        # home_price = (WebDriverWait(driver, 10).until(EC.visibility_of_element_located(home_price_locator))).text
        # print(home_price)
    #
    #     # 点击第一个新品进商品详情页
    #     pageInfo_locator = (MobileBy.XPATH, '//android.widget.RelativeLayout[@content-desc="抢神券"]')
    #     WebDriverWait(driver, 10).until(EC.visibility_of_element_located(pageInfo_locator)).click()
    #     time.sleep(10)
    #
    #     #  判断是否有活动，倒计时上方文案	 com.suning.mobile.ebuy:id/tv_flash_sale_time_down_name
    #     time_text_locator = (MobileBy.XPATH, "com.suning.mobile.ebuy:id/tv_flash_sale_time_down_name")
    #     if "距" in WebDriverWait(driver, 10).until(EC.visibility_of_element_located(time_text_locator)).text:
    #         # 获取详情页商品活动价格
    #         pageInfo_gbprice_locator = (MobileBy.ID, 'com.suning.mobile.ebuy:id/tv_flash_sale_price')
    #         pageInfo_gbprice = (
    #             WebDriverWait(driver, 10).until(EC.visibility_of_element_located(pageInfo_gbprice_locator))).text
    #         print(pageInfo_gbprice)
    #
    #         # 断言首页价格等于详情页商品活动价格
    #         assert home_price == pageInfo_gbprice, f"预期价格为{home_price}，实际结果为{pageInfo_gbprice}"
    #     else:
    #         # 获取详情页商品价格前¥符号
    #         pageInfo_price_label_locator = (MobileBy.ID, 'com.suning.mobile.ebuy:id/tv_ord_price_lable')
    #         pageInfo_price_label = (
    #             WebDriverWait(driver, 10).until(EC.visibility_of_element_located(pageInfo_price_label_locator))).text
    #
    #         # 获取详情页商品价格
    #         pageInfo_price_locator = (MobileBy.ID, 'com.suning.mobile.ebuy:id/tv_ord_price_value')
    #         pageInfo_price = (
    #             WebDriverWait(driver, 10).until(EC.visibility_of_element_located(pageInfo_price_locator))).text
    #
    #         # 因为详情页价格符号和价格是分开的，所以相加得到完整详情页价格
    #         page_price = pageInfo_price_label + pageInfo_price
    #         print(page_price)
    #
    #         # 断言首页价格等于详情页价格
    #         assert home_price == page_price, f"预期价格为{home_price}，实际结果为{page_price}"