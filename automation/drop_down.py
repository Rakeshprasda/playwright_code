from playwright.sync_api import Page
from locater import HomePage


class drop_down(HomePage):
    def __init__(self, page :Page):
        super().__init__(page)

    def page_login(self):
        self.page.goto(self.base_url)
        self.page.wait_for_selector('#email').fill("rakp.gmail.com")
        print("entered email")
        self.page.wait_for_timeout(3000)
        self.next = self.page.locator("#enterimg")
        self.next.click()

    def label(self):
        self.page_login()
        self.page.wait_for_timeout(3000)
        self.page.select_option("select#Skills",label="Corel Word Perfect")
        print("selected cprel word")
        self.page.wait_for_timeout(3000)

    def select_index(self):
        self.page_login()
        self.page.wait_for_timeout(3000)
        self.page.select_option("select#Skills",index=10)
        self.page.wait_for_timeout(3000)

    def select_arg(self):
        self.page_login()
        self.option= self.page.locator("select#Skills > option")
        self.select_opt = self.option.nth(20).get_attribute("value")
        self.page.select_option("select#Skills",value=self.select_opt)
        print("select dorpdown by value")
        self.page.wait_for_timeout(9000)





from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    p1=drop_down(page)
    p1.select_arg()
