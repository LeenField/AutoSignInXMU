import os
# 方便延时加载
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException

# 模拟浏览器打开网站
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')#　让Chrome在root权限下跑
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('blink-settings=imagesEnabled=false')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
browser = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)

def xmu():
    browser.get("https://ids.xmu.edu.cn/authserver/login?service=https://xmuxg.xmu.edu.cn/login/cas/xmu")
    browser.maximize_window()
    
    try:
        browser.find_element_by_xpath(
            "//*[@id='username']").send_keys(os.environ['XMU_USER'])
        browser.find_element_by_xpath(
            "//*[@id='password']").send_keys(os.environ['XMU_PASSWORD'])
        browser.find_element_by_xpath("//*[@type='submit']").click()
        time.sleep(10)

        try:
            browser.find_element_by_xpath("//*[@class='app_child box_flex'][1]").click()
            time.sleep(10)

            try:
                now_handle = browser.current_window_handle   #获取当前窗口的句柄
                all_handles = browser.window_handles   #获取到当前所有的句柄,所有的句柄存放在列表当中
                print(browser.title)  #获取切换后的标题
                '''获取非最初打开页面的句柄'''
                for handles in all_handles:
                    if now_handle != handles:
                        browser.switch_to_window(handles)
                browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div[3]/div[2]").click()
                time.sleep(10)
                try:
                    # js="window.scrollTo(0,document.body.scrollHeight)"
                    # browser.execute_script(js)
                    # browser.find_element_by_xpath("//*[@class='form-save']").click()
                    if("日志" in browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div/button").text):
                        print("成功到达表单")
                    # browser.find_element_by_xpath("//*[@class='form-control dropdown-toggle'][12]").click()
                    # browser.find_element_by_xpath("//*[@class='btn-content placeholder'][3]").click()
                    time.sleep(10)

                    try:
                        # 用edge的debug模式居然不显示Xpath，chrome的有，浪费一堆时间。。。
                        # 点击 "本人是否承诺所填报的全部内容均属实"
                        browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div/div[3]/div/div[22]/div/div/div").click()
                        time.sleep(10)
                        # browser.find_element_by_xpath("//*[@title='请选择'][3]").click()
                        # browser.find_element_by_xpath("//div[@class='form-control dropdown-toggle'][4]").click()
                        # browser.find_element_by_xpath("//*[@title='是 Yes']").click()
                        # 点击"是 Yes"
                        browser.find_element_by_xpath("/html/body/div[8]/ul/div/div[3]/li/label").click()
                        time.sleep(10)

                        try:
                            # 点击保存按钮
                            # browser.find_element_by_xpath("//*[@class='form-save']").click()
                            browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div/span/span").click()
                            time.sleep(10)

                            try:                        
                                confirm_alert = browser.switch_to.alert
                                print(confirm_alert.text)
                                # 处理弹窗，确认提交
                                confirm_alert.accept()
                                time.sleep(10)

                            # 已签到的 不会有弹窗
                            except NoAlertPresentException as e:
                                print ("NoAlertPresentException!")
                                print("已签到"+str(e))  


                        except NoSuchElementException as e:
                            print ("NoSuchElementException!")
                            print("签到代码在 提交表单 存在异常"+str(e))  

                    except NoSuchElementException as e:
                        print ("NoSuchElementException!")
                        print("签到代码在 表单点击下拉菜单中 存在异常"+str(e))  

                except NoSuchElementException as e:
                    print ("NoSuchElementException!")
                    print("签到代码在 切换表单到 我的表单 存在异常"+str(e))  

            except NoSuchElementException as e:
                print ("NoSuchElementException!")
                print("签到代码在 后台页面点击跳转 存在异常"+str(e))      

        except NoSuchElementException as e:
            print ("NoSuchElementException!")
            print("签到代码在 登录 存在异常"+str(e))
            
    except NoSuchElementException as e:
        print ("NoSuchElementException!")
        print("签到代码在 登录表单 存在异常"+str(e))

if __name__ == '__main__':
    xmu()
    # 脚本运行成功,退出浏览器
    browser.quit()
