import pytest
from base import BaseTest

class Test_Page(BaseTest):
    def setUp(self):
        url = 
        self.driver = self.setUpDriver()
        self.driver.get(url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    @pytest.mark.smoke
    def test_method_name(self):
        //Write your methods here