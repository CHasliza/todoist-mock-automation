class BasePage:

    PAGE_LOAD_WAIT = 5

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(self.PAGE_LOAD_WAIT)