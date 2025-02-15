from playwright.sync_api import Page
from locater import HomePage

class file_handle(HomePage):
    def __init__(self, page:Page):
        super().__init__(page)

    def file_upload(self):
        self.page.goto(self.fileupload_url)
        self.page.wait_for_timeout(3000)
        upload_location = self.page.locator("//input[@id='input-4']")
        file_upload = r"C:\Users\Rakesh P\PycharmProjects\playwright\pythonProject\automation\files\rakp.txt"
        upload_location.set_input_files(file_upload)
        self.page.wait_for_timeout(5000)

    def file_download(self):
        self.page.locator(self.filedownload_url)
        self.page.wait_for_timeout(3000)
        self.page.locator("//textarea[@id='textbox']").type("rakesh is working in akamai")
        self.page.locator("//button[@id='createTxt']").click()
        self.page.wait_for_timeout(3000)
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    ctn = browser.new_context()
    page = ctn.new_page()

    p1 = file_handle(page)
    p1.file_upload()













