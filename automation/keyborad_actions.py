from playwright.sync_api import Page
from locater import HomePage

class keyborad_action(HomePage):
    def __init__(self,page :Page):
        super().__init__(page)

    def page_login(self):
        self.page.goto(self.base_url)
        self.page.wait_for_selector('#email').fill("rakp.gmail.com")
        self.page.wait_for_timeout(3000)
        self.next = self.page.locator("#enterimg")
        self.next.click()
        #self.page.wait_for_selector(3000)

    def press_enter(self):
        self.page_login()
        self.firstname=self.page.locator("//input[@placeholder='First Name']")
        self.firstname.fill("rakesh")
        self.page.wait_for_timeout(3000)
        self.firstname.press("Enter")
        self.page.wait_for_timeout(5000)
        self.lastname=self.page.locator("//input[@placeholder='Last Name']")
        self.lastname.type("prasad")
        self.page.wait_for_timeout(3000)
        self.lastname.press("Tab")
        self.page.wait_for_timeout(3000)



from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    new_cnt=browser.new_context()
    page=new_cnt.new_page()

    p1=keyborad_action(page)
    p1.press_enter()
