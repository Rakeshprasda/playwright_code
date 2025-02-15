from playwright.sync_api import Page

class HomePage:
    base_url="https://demo.automationtesting.in/"
    arlt_url="https://demo.automationtesting.in/Alerts.html"
    swt_window = "https://demo.automationtesting.in/Windows.html"
    fileupload_url = "https://demo.automationtesting.in/FileUpload.html"
    filedownload_url= "https://demo.automationtesting.in/FileDownload.html"

    def __init__(self,page: Page):
        self.page: Page=page

        self.email=self.page.locator("#email")
        self.enter=self.page.locator("#enterimg")
        self.male=self.page.locator("//input[@value='Male']")
        self.female=self.page.locator("//input[@value='FeMale']")
        self.cricket=self.page.locator("//input[@value='Cricket']")
        self.movie=self.page.query_selector("//input[@value='Movies']")
        self.hockey=self.page.query_selector("//input[@value='Hockey']")


        #alert page#
        self.alert_ok=self.page.locator("//a[@href='#OKTab']")
        self.alert_btn=self.page.locator("//button[@class='btn btn-danger']")
        self.alert_cnl=self.page.locator("//a[@href='#CancelTab']")
        self.alrt_cnl_btn=self.page.locator("//button[@class='btn btn-primary']")


        ####### handle window page #################
        self.window_link = self.page.locator("//button[contains(text(), ' click ')]")







