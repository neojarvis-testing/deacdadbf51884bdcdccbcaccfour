import pytest
from base import BaseTest
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_Page(BaseTest):

    def setUp(self):
        url = "https://www.mumzworld.com/en"
        self.driver = self.setUpDriver()
        self.driver.get(url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_method_name(self):

        wait = WebDriverWait(self.driver, 15)
        actions = ActionChains(self.driver)

       # 2. Hover over "Bath"
        bath_section = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='radix-:R1p5apjsq:-trigger-radix-:R8dp5apjsq:']")))
        actions.move_to_element(bath_section).perform()
        print("Hovered over 'Bath'")

        # 3. Take screenshot
        # Screenshot.capture_screenshot(self.driver)

        # 4. Click on "Bath Tubs" under "Bath Tubs & Accessories"
        bath_tubs = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//li[normalize-space()='Bath Tubs']")))
        bath_tubs.click()
        print("Clicked on 'Bath Tubs'")

        # 5. Click on "Sale" label under Filters
        sale_filter = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='3-6 mo-36440']")))
        sale_filter.click()
        print("Clicked on '3-6' filter")

        time.sleep(2)  # allow products to reload

        # 6. Click the first product
        first_product = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@class='ProductCard_productName__Dz1Yx'])[1]")))
        first_product.click()
        print("Clicked first product")

        # 7. Click "Add to Bag"
        add_to_bag = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add to Cart']")))
        add_to_bag.click()
        print("Clicked 'Add to Bag'")

        # 8. Click "View Cart" from pop-up
        view_cart = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@title='View Cart']")))
        view_cart.click()
        print("Clicked 'View Cart'")
