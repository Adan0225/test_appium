# -*- coding: utf-8 -*-
# @Time  : 2022/6/23 19:12
# Author : 拒绝内卷的小测试

from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestClass:
    def setup(self):
        # 创建⼀个字典,⽤于存储设备和应⽤信息
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "11.0.0",
            "deviceName": "eqb6w4zldmmvvwln",
            "appPackage": "com.suning.mobile.ebuy",
            "appActivity": "com.suning.mobile.ebuy.host.InitialActivity"
        }

        # 与appium session之间建⽴联系，括号内为appium服务地址
        global driver
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        # 进入app，点击同意按钮
        agree_locator = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("同意")')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(agree_locator)).click()
        # 点击我知道了按钮
        know_locator = (MobileBy.ID, 'com.suning.mobile.ebuy:id/home_new_person_delete_iv')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(know_locator)).click()
        time.sleep(10)

        # 滑动屏幕，露出新品tab
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        driver.swipe(int(x * 0.5), int(y * 0.5), int(x * 0.5), int(y * 0.1), duration=500)

        # 点击新品tab
        newcomm_locator = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("新品")')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(newcomm_locator)).click()
        time.sleep(3)

    def test_001(self):
        # 获取首页新品第一个商品名称
        home_name_locator = (MobileBy.ID, 'com.suning.mobile.ebuy:id/product_name_tv_1')
        home_name = (WebDriverWait(driver, 10).until(EC.visibility_of_element_located(home_name_locator))).text
        print(home_name)

        # 点击第一个新品进商品详情页
        pageInfo_locator = (MobileBy.ID, 'com.suning.mobile.ebuy:id/product_iv_1')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(pageInfo_locator)).click()
        time.sleep(10)

        # 获取详情页商品名称
        pageInfo_name_locator = (MobileBy.ID, 'com.suning.mobile.ebuy:id/tv_goodsdetail_goods_name')
        pageInfo_name = (WebDriverWait(driver, 10).until(EC.visibility_of_element_located(pageInfo_name_locator))).text
        print(pageInfo_name)

        # 断言首页商品名称等于详情页商品名称
        assert home_name == pageInfo_name, f"预期名称为{home_name}，实际结果为{pageInfo_name}"

    def test_002(self):

        # 获取首页新品第一个商品价格
        home_price_locator = (MobileBy.ID, 'com.suning.mobile.ebuy:id/product_price_tv_1')
        home_price = (WebDriverWait(driver, 10).until(EC.visibility_of_element_located(home_price_locator))).text
        print(home_price)

        # 点击第一个新品进商品详情页
        pageInfo_locator = (MobileBy.ID, 'com.suning.mobile.ebuy:id/product_iv_1')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(pageInfo_locator)).click()
        time.sleep(10)

        #  判断是否有活动，倒计时上方文案	 com.suning.mobile.ebuy:id/tv_flash_sale_time_down_name
        time_text_locator = (MobileBy.ID, "com.suning.mobile.ebuy:id/tv_flash_sale_time_down_name")
        if "距" in WebDriverWait(driver, 10).until(EC.visibility_of_element_located(time_text_locator)).text:
            # 获取详情页商品活动价格
            pageInfo_gbprice_locator = (MobileBy.ID, 'com.suning.mobile.ebuy:id/tv_flash_sale_price')
            pageInfo_gbprice = (
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located(pageInfo_gbprice_locator))).text
            print(pageInfo_gbprice)

            # 断言首页价格等于详情页商品活动价格
            assert home_price == pageInfo_gbprice, f"预期价格为{home_price}，实际结果为{pageInfo_gbprice}"
        else:
            # 获取详情页商品价格前¥符号
            pageInfo_price_label_locator = (MobileBy.ID, 'com.suning.mobile.ebuy:id/tv_ord_price_lable')
            pageInfo_price_label = (
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located(pageInfo_price_label_locator))).text

            # 获取详情页商品价格
            pageInfo_price_locator = (MobileBy.ID, 'com.suning.mobile.ebuy:id/tv_ord_price_value')
            pageInfo_price = (
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located(pageInfo_price_locator))).text

            # 因为详情页价格符号和价格是分开的，所以相加得到完整详情页价格
            page_price = pageInfo_price_label + pageInfo_price
            print(page_price)

            # 断言首页价格等于详情页价格
            assert home_price == page_price, f"预期价格为{home_price}，实际结果为{page_price}"