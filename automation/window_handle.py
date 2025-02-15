from playwright.sync_api import Page
from locater import HomePage

class handle_window(HomePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.context = page.context                     # this is for assign the content in class

    def switch_window(self):
        self.page.goto(self.swt_window)
        self.page.wait_for_timeout(3000)
        self.window_link.click()
        self.page.wait_for_timeout(3000)

        ## to find how many windos in context
        self.total_page = self.context.pages
        print(len(self.total_page))
        for i in self.total_page:
            print(i)

        self.new_page = self.total_page[1]
        self.new_page.bring_to_front()
        print(self.new_page.title())
        self.new_page.wait_for_timeout(3000)
        #self.new_page.close()

        self.old_page = self.total_page[0]
        self.old_page.bring_to_front()
        self.page.wait_for_timeout(3000)
        print(self.page.title())

        self.page.close()




