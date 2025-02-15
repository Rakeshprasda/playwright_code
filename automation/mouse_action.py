from playwright.sync_api import Page
from locater import HomePage


class mouse_action(HomePage):
    def __init__(self, page :Page):
        super().__init__(page)

    def page_login(self):
        self.page.goto(self.base_url)
        self.page.wait_for_selector('#email').fill("rakp.gmail.com")
        self.page.wait_for_timeout(3000)
        self.next = self.page.locator("#enterimg")
        self.next.click()

    def mouse_hover(self):
        self.page_login()
        self.page.wait_for_timeout(3000)
        self.page.locator("//a[text()='Widgets']").hover()
        self.page.wait_for_timeout(5000)
        self.page.locator("//a[text()=' Slider ']").click()
        self.page.wait_for_timeout(5000)

    def double_click(self):
        self.page_login()
        self.page.wait_for_timeout(3000)
        self.page.locator("(//*[text()='Register'])[3]").dblclick()
        self.page.wait_for_timeout(5000)

    def right_click(self):
        self.page_login()
        self.page.wait_for_timeout(3000)
        self.page.locator("(//*[text()='Register'])[3]").click(button="right")
        self.page.wait_for_timeout(5000)


from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser= p.chromium.launch(headless=False)
    new_context=browser.new_context()
    page=new_context.new_page()

    p1=mouse_action(page)
    p1.right_click()