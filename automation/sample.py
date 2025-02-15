from playwright.sync_api import Page
from locater import HomePage

class rakp(HomePage):
    def __init__(self,page :Page):
        super().__init__(page)
        self.context = page.context

    def wnd(self):
        self.page.goto(self.swt_window)
        self.page.wait_for_timeout(3000)
        self.window_link.click()
        self.page.wait_for_timeout(3000)


        self.total_wnd = self.context.pages
        print(len(self.total_wnd))
        for i in self.total_wnd:
            print(i)


        self.new_page= self.total_wnd[1]
        self.new_page.bring_to_front()
        print(self.new_page.title())
        self.page.screenshot(path=r"C:\Users\Rakesh P\PycharmProjects\playwright\pythonProject\automation\images\image.png",full_page=True)
        self.page.wait_for_timeout(3000)

        self.old_page = self.total_wnd[0]
        self.old_page.bring_to_front()
        print(self.old_page.title())
        print(self.page.context.cookies())
        self.page.wait_for_timeout(3000)


from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    bro= p.chromium.launch(headless=False)
    ctn = bro.new_context()
    page = ctn.new_page()
    p1=rakp(page)
    p1.wnd()
