from radio_check import Login
from playwright.sync_api import sync_playwright
from alert_button import handle_alert
from window_handle import handle_window



with sync_playwright() as p:
    # when the automation is doing in single window page is enough
    browser = p.chromium.launch(headless=False)
    #page = browser.new_page()              #page is created with new page


    ### when the automation using multiple window contenx is required to store the pages
    context = browser.new_context()
    page = context.new_page()               #page is created with new context



######################### Test Cases ###############################

    # Create an instance of the Login class
    # login_instance = Login(page)
    # login_instance.pagelogin()

    #test for alert ok button
    # alrt_case= handle_alert(page)
    # alrt_case.ok_alert()

    #test for dismiss and print message
    # alrt_cnsl=handle_alert(page)
    # alrt_cnsl.cnsl_alrt()

    #store the handle message
    # dialog_msg=handle_alert(page)
    # dialog_msg.print_alrt_msg()

    ## window handling
    window_hndl= handle_window(page)
    window_hndl.switch_window()
