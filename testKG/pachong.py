from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# 设置 Chrome 浏览器的选项
chrome_options = Options()
chrome_options.add_argument("--headless")  # 设置无头模式，不显示浏览器窗口
chrome_options.add_argument("--disable-gpu")

# 使用 webdriver-manager 自动下载和管理 ChromeDriver
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

# 打开网页
url = "https://www.autohome.com.cn/352/"
driver.get(url)

# 等待页面加载
time.sleep(3)  # 等待 3 秒钟，让页面完全加载

# 查找页面中的品牌元素
car_brands = driver.find_elements(By.CLASS_NAME, "brand-model-name")  # 选择器需要根据实际页面调整

# 打印品牌信息
if car_brands:
    for brand in car_brands:
        print("品牌：", brand.text)
else:
    print("未找到任何汽车品牌数据，请检查选择器或网页内容")

# 关闭浏览器
driver.quit()
