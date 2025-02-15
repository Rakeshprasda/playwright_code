from playwright.sync_api import Page
from locater import HomePage


class Login(HomePage):  # Class names should follow PascalCase
    def __init__(self, page: Page):
        super().__init__(page)

    def pagelogin(self):
        self.page.goto(self.base_url)
        self.email.fill("rakp@gmail.com")
        self.page.wait_for_timeout(3000)
        self.enter.click()
        self.page.wait_for_timeout(3000)
        print(self.page.title())
        self.female.click()                         #to select radio button we can use click
        self.page.wait_for_timeout(3000)
        self.male.check()                           #to select radio button we can use check
        self.page.wait_for_timeout(3000)
        if self.male.is_checked():
            print("select male option")
        else:
            print("select female option")
        self.page.wait_for_timeout(3000)
        try:
            self.cricket.check()
            self.page.wait_for_timeout(3000)
            if self.cricket.is_checked():
                print("cricket is selected")
            else:
                print("cricket is not selected")
        except Exception as e:
            print(f"not able to click on cricket due to {e}")
        finally:
            self.page.close()