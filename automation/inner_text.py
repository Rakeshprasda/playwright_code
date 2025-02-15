from playwright.sync_api import Page
from locater import HomePage
import time


class inner_text(HomePage):
    def __init__(self,page :Page):
        super().__init__(page)

    def login(self):
        self.page.goto(self.base_url)
        self.page.wait_for_selector('#email').fill("rakp.gmail.com")
        self.page.wait_for_timeout(3000)
        self.next = self.page.locator("#enterimg")
        self.next.click()
        self.page.wait_for_timeout(3000)

# get the inner text of the multiple element
    def all_element(self):
        self.login()
        self.input=self.page.query_selector_all("a")
        print(len(self.input))
        for i in self.input:
            print(i.inner_text())

#to collect all the atribute value of the link element
    def get_atribute(self):
        try:
            self.login()
        except Exception as e:
            print(e)

        try:
            self.input=self.page.query_selector_all("a")
            print(len(self.input))
        except Exception as e:
            print(e)

        for i in self.input:
            print(i.get_attribute("href"))

    def collect_all(self):
        self.login()
        self.page.wait_for_timeout(3000)
        self.page.locator("//div[@id='msdd']").click()
        self.page.wait_for_timeout(3000)
        self.lng=self.page.locator("//ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content ui-corner-all']//li")
        count= self.lng.count()
        for i in range(count):
            text= self.lng.nth(i).inner_text()
            print(text)
            if text == "Portuguese":
                self.lng.nth(i).click()
                print(f"click on the {text}")
                break







from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    ctn=browser.new_context()
    page=ctn.new_page()

    p1=inner_text(page)
    p1.collect_all()
    time.sleep(10)
    # logging.info("take rest 10 sec before start the nex text")
    # p1.all_element()