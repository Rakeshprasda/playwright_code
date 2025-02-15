from playwright.sync_api import Page
from locater import HomePage

class table_data(HomePage):
    def __init__(self, page :Page):
        super().__init__(page)

    def page_login(self):
        self.page.goto("https://www.techlistic.com/2017/02/automate-demo-web-table-with-selenium.html",timeout=120000)
        self.page.wait_for_timeout(60000)

    def table_info(self):
        self.page_login()
        self.table=self.page.wait_for_selector("//table[@id='customers']")
        rows= self.table.query_selector_all("tr")
        print(len(rows))
        columns=self.table.query_selector_all("td")
        print(len(columns))
        for i in rows:
            columns=i.query_selector_all("td")
            for j in columns:
                text=j.text_content()
                print(text)
                if text=="Microsoft":
                    break                  #break just will break the inner loop, and continue the outer loop
                if text == "Adobe":
                    return                  # return will completly stop the lopp


    def table2_info(self):
        self.page_login()
        self.table2=self.page.locator("//table[@id='customers']")           #when we use locator function we cant use query selctior functon
        rows=self.table2.locator("tr").all()
        print("total rows : {}".format(len(rows)))
        columns = self.table2.locator("th").all()
        print("total colums : {}".format(len(columns)))


from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()

    p1=table_data(page)
    p1.table2_info()
