from selenium.webdriver import Chrome, ChromeOptions


class ChromeDriver:
    _CHROME_DEFAULT_OPTIONS = ["--no-sandbox", "--disable-dev-shm-usage", "--headless"]
    _CHROME_EXECUTABLE_PATH = "chromedriver"

    def __init__(self, options: list[str] = []):
        self.options = ChromeOptions()
        for option in self._CHROME_DEFAULT_OPTIONS + options:
            self.options.add_argument(option)
        self.driver = Chrome(
            options=self.options
        )
        self.soup = None

    def __enter__(self):
        return self.driver

    def __exit__(self, exc_type, exc_value, tb):
        self.driver.quit()
