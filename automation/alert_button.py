from playwright.sync_api import Page
from locater import HomePage
test_alert=[]


def handle_dialog(dialog):
    msg=dialog.message
    test_alert.append(msg)
    dialog.accept()


class handle_alert(HomePage):
    def __init__(self, page :Page):
        super().__init__(page)

    def ok_alert(self):
        self.page.goto(self.arlt_url)
        self.page.wait_for_timeout(3000)
        self.alert_ok.click()
        self.page.wait_for_timeout(3000)
        self.alert_btn.click()                          #if we are not giving any ok 0r cacncel it will automaticaly click on first action
        self.page.wait_for_timeout(3000)

    def cnsl_alrt(self):                    # we cant store the dialog message but we can print
        self.page.goto(self.arlt_url)
        self.page.wait_for_timeout(3000)
        self.alert_cnl.click()
        self.page.wait_for_timeout(3000)
        #alert action(event is "dialog" for alert action)
        self.page.on("dialog", lambda dialog : dialog.accept())            #to click on ok use accept
        #self.page.on("dialog", lambda raki : raki.dismiss())          #to click on cancel use dismiss
        msg=self.page.on("dialog", lambda msg: print(msg.message))         # to print the message use message
        self.alrt_cnl_btn.click()
        print(msg)
        self.page.wait_for_timeout(3000)

    def print_alrt_msg(self):
        self.page.goto(self.arlt_url)
        self.page.wait_for_timeout(3000)
        self.alert_cnl.click()
        self.page.wait_for_timeout(3000)
        self.page.on("dialog", handle_dialog)
        self.page.wait_for_timeout(3000)
        print(test_alert)







