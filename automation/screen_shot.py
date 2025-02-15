import logging

from playwright.sync_api import Page
from locater import HomePage


class screen_shot(HomePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def login(self):
        self.page.goto(self.base_url)
        #self.page.wait_for_timeout(3000)
        self.email.fill("rakp@gmail.com")
        #self.page.wait_for_timeout(3000)
        self.enter.click()

    def current_screen_shot(self):      #this will take the creenshot of visiable creen
        self.login()
        self.page.screenshot(path=r"C:\Users\Rakesh P\PycharmProjects\playwright\pythonProject\automation\images\rakp.png")

    def full_screen(self):              # this will take complete creenshot
        self.login()
        self.page.screenshot(path=r"C:\Users\Rakesh P\PycharmProjects\playwright\pythonProject\automation\images\full.png",full_page=True)

    def clip_screenshot(self):      #baseed on dimesion we can take screenshot
        self.login()
        self.page.screenshot(path=r"C:\Users\Rakesh P\PycharmProjects\playwright\pythonProject\automation\images\clip.png",clip={"x":0,"y":0,"width": 800, "height": 600})

    def no_backgrou(self):
        self.login()
        self.page.screenshot(path=r"C:\Users\Rakesh P\PycharmProjects\playwright\pythonProject\automation\images\nobmg.png",omit_background=True)

    def type_screenshot(self):      #we can take a acreen shot with required formate with required quality
        self.login()
        self.page.screenshot(path=r"C:\Users\Rakesh P\PycharmProjects\playwright\pythonProject\automation\images\type.jpeg",type="jpeg",quality=10)




from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()


############ calling function ##########
    test1=screen_shot(page)
    test1.type_screenshot()
